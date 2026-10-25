#!/usr/bin/env python3
"""
Pixabay Image Fetcher - Fetch high-quality free images from Pixabay API
"""
import os
import json
import argparse
import requests
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlencode

PIXABAY_API_BASE = "https://pixabay.com/api/"

class PixabayFetcher:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("PIXABAY_API_KEY")
        if not self.api_key:
            raise ValueError("PIXABAY_API_KEY environment variable or --api-key required")

    def search(self, **params) -> Dict:
        """Search Pixabay for images."""
        params["key"] = self.api_key
        params["image_type"] = params.get("image_type", "photo")
        params["safesearch"] = params.get("safe_search", "true")
        
        # Build query string
        url = f"{PIXABAY_API_BASE}?{urlencode(params)}"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()

    def search_images(self, query: str, category: str = "backgrounds",
                      orientation: str = "horizontal", colors: Optional[str] = None,
                      min_width: int = 1920, min_height: int = 1080,
                      per_page: int = 20, page: int = 1, order: str = "popular",
                      safe_search: bool = True) -> List[Dict]:
        """Search for images with common parameters."""
        params = {
            "q": query,
            "category": category,
            "orientation": orientation,
            "min_width": min_width,
            "min_height": min_height,
            "per_page": min(per_page, 200),
            "page": page,
            "order": order,
            "safesearch": "true" if safe_search else "false"
        }
        if colors:
            params["colors"] = colors
        
        result = self.search(**params)
        return result.get("hits", [])

    def download_image(self, url: str, output_path: Path, filename: str) -> bool:
        """Download a single image."""
        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            output_path.mkdir(parents=True, exist_ok=True)
            filepath = output_path / filename
            
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            return False

    def download_images(self, images: List[Dict], output_dir: Path, 
                        size: str = "largeImageURL") -> Dict:
        """Download multiple images."""
        output_dir.mkdir(parents=True, exist_ok=True)
        results = {"success": [], "failed": []}
        
        for i, img in enumerate(images):
            url = img.get(size) or img.get("largeImageURL") or img.get("webformatURL")
            if not url:
                results["failed"].append({"index": i, "reason": "No URL found"})
                continue
            
            # Generate filename
            photographer = img.get("user", "unknown").replace(" ", "_")
            img_id = img.get("id", i)
            ext = Path(url).suffix or ".jpg"
            filename = f"pixabay_{img_id}_{photographer}{ext}"
            
            if self.download_image(url, Path("."), filename):
                # Move to output dir
                import shutil
                shutil.move(filename, Path(output_dir) / filename)
                results["success"].append({
                    "filename": filename,
                    "photographer": img.get("user"),
                    "tags": img.get("tags"),
                    "url": url
                })
            else:
                results["failed"].append({"index": i, "reason": "Download failed"})
        
        return results


def main():
    parser = argparse.ArgumentParser(description="Pixabay Image Fetcher")
    parser.add_argument("--api-key", help="Pixabay API key (or set PIXABAY_API_KEY env)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Search command
    search_parser = subparsers.add_parser("search", help="Search for images")
    search_parser.add_argument("--query", required=True, help="Search query")
    search_parser.add_argument("--category", default="backgrounds")
    search_parser.add_argument("--orientation", default="horizontal", 
                              choices=["horizontal", "vertical", "all"])
    search_parser.add_argument("--colors", help="Comma-separated colors")
    search_parser.add_argument("--min-width", type=int, default=1920)
    search_parser.add_argument("--min-height", type=int, default=1080)
    search_parser.add_argument("--per-page", type=int, default=20)
    search_parser.add_argument("--page", type=int, default=1)
    search_parser.add_argument("--order", default="popular", choices=["popular", "latest"])
    search_parser.add_argument("--safe-search", action="store_true", default=True)
    search_parser.add_argument("--output", help="Output JSON file")

    # Download command
    download_parser = subparsers.add_parser("download", help="Download images")
    download_parser.add_argument("--urls-file", required=True, help="JSON file with image URLs")
    download_parser.add_argument("--output-dir", required=True, help="Output directory")
    download_parser.add_argument("--size", default="largeImageURL", 
                                choices=["largeImageURL", "webformatURL", "previewURL"])

    args = parser.parse_args()

    fetcher = PixabayFetcher(api_key=args.api_key)

    if args.command == "search":
        images = fetcher.search_images(
            query=args.query,
            category=args.category,
            orientation=args.orientation,
            colors=args.colors,
            min_width=args.min_width,
            min_height=args.min_height,
            per_page=args.per_page,
            page=args.page,
            order=args.order,
            safe_search=args.safe_search
        )
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(images, f, indent=2)
            print(f"Saved {len(images)} results to {args.output}")
        else:
            print(json.dumps(images, indent=2))

    elif args.command == "download":
        with open(args.urls_file) as f:
            images = json.load(f)
        
        fetcher = PixabayFetcher(api_key=args.api_key)
        results = fetcher.download_images(images, Path(args.output_dir), args.size)
        
        print(f"Downloaded: {len(results['success'])}")
        print(f"Failed: {len(results['failed'])}")
        
        if results["failed"]:
            print("Failed downloads:", json.dumps(results["failed"], indent=2))


if __name__ == "__main__":
    main()