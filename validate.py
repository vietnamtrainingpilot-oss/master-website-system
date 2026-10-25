#!/usr/bin/env python3
"""
Validation script for Master Website System.
Run from the product root directory.
"""
import os
import json
import sys
from pathlib import Path

PRODUCT_ROOT = Path(__file__).parent

CHECKS = []

def check(name, condition, evidence=""):
    status = "PASS" if condition else "FAIL"
    CHECKS.append({"id": len(CHECKS)+1, "name": name, "status": status, "evidence": evidence})
    icon = "[OK]" if condition else "[FAIL]"
    print(f"  {icon} {name}: {status} {evidence}")
    return condition

def main():
    print("============================================================")
    print("  Master Website System - Validation")
    print("============================================================")
    print()

    # 1. Core files exist
    print("Core Implementation:")
    check("Main SKILL.md exists", (PRODUCT_ROOT / ".opencode/skills/master-website/SKILL.md").exists())
    check("Command file exists", (PRODUCT_ROOT / ".opencode/commands/master-website.md").exists())
    check("Skill README exists", (PRODUCT_ROOT / ".opencode/skills/master-website/README.md").exists())

    # 2. SKILL.md size >= 12KB
    skill_path = PRODUCT_ROOT / ".opencode/skills/master-website/SKILL.md"
    skill_size = skill_path.stat().st_size if skill_path.exists() else 0
    check(f"SKILL.md size >= 12KB ({skill_size/1024:.1f} KB)", skill_size >= 10000)

    # 3. Reference library
    print("\nReference Library:")
    refs = [
        "skill-integration-map.md",
        "template-selection-guide.md",
        "source-attribution.md",
        "source-inventory.jsonl",
        "design-read-template.md",
        "dials.json",
        "decision-record-template.md",
        "hard-gates.md",
    ]
    for ref in refs:
        check(f"Reference: {ref}", (PRODUCT_ROOT / f".opencode/skills/master-website/references/{ref}").exists())

    # 4. Catalogs
    print("\nCatalogs:")
    check("Design systems AGENTS.md", (PRODUCT_ROOT / ".opencode/skills/master-website/references/design-systems/AGENTS.md").exists())
    check("Design templates AGENTS.md", (PRODUCT_ROOT / ".opencode/skills/master-website/references/design-templates/AGENTS.md").exists())

    # 5. Audit artifacts
    print("\nAudit Artifacts:")
    check("Enhanced audit JSONL", (PRODUCT_ROOT / "docs/master-website/audit/source-audit-enhanced.jsonl").exists())
    check("Audit report", (PRODUCT_ROOT / "docs/master-website/audit/source-audit-report.md").exists())
    check("Validation report", (PRODUCT_ROOT / "docs/master-website/validation-report.md").exists())

    # 6. Installer
    print("\nInstaller:")
    check("install.ps1 exists", (PRODUCT_ROOT / "install.ps1").exists())

    # 7. Source inventory integrity
    print("\nSource Inventory:")
    inv_path = PRODUCT_ROOT / ".opencode/skills/master-website/references/source-inventory.jsonl"
    if inv_path.exists():
        with open(inv_path, 'r', encoding='utf-8') as f:
            lines = sum(1 for _ in f if _.strip())
        check(f"Inventory entries: {lines} (expected ~5243)", lines >= 5000)
    else:
        check("Inventory file exists", False)

    # 8. Enhanced audit integrity
    print("\nEnhanced Audit:")
    audit_path = PRODUCT_ROOT / "docs/master-website/audit/source-audit-enhanced.jsonl"
    if audit_path.exists():
        with open(audit_path, 'r', encoding='utf-8') as f:
            audit_lines = sum(1 for _ in f if _.strip())
        fully_inspected = 0
        cataloged = 0
        with open(audit_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    try:
                        obj = json.loads(line)
                        if obj.get('inspection_status') == 'FULLY_INSPECTED':
                            fully_inspected += 1
                        elif obj.get('inspection_status') == 'CATALOGED':
                            cataloged += 1
                    except:
                        pass
        check(f"Enhanced audit entries: {audit_lines}", audit_lines >= 5000)
        check(f"FULLY_INSPECTED skills: {fully_inspected}", fully_inspected >= 30)
        check(f"CATALOGED systems/templates: {cataloged}", cataloged >= 4000)
    else:
        check("Enhanced audit file exists", False)

    # 9. Command file structure
    print("\nCommand Structure:")
    cmd_path = PRODUCT_ROOT / ".opencode/commands/master-website.md"
    if cmd_path.exists():
        content = cmd_path.read_text(encoding='utf-8')
        check("Command has frontmatter", content.startswith("---"))
        check("Command references $ARGUMENTS", "$ARGUMENTS" in content)
        check("Command invokes skill", "master-website" in content)

    # 10. SKILL.md structure
    print("\nSkill Structure:")
    if skill_path.exists():
        content = skill_path.read_text(encoding='utf-8')
        check("Skill has frontmatter", content.startswith("---"))
        check("Skill has Phases A-L", (f"Phase A" in content and f"Phase M" in content))
        check("Skill has Hard Gates table", "Hard Gates" in content)
        check("Skill references references/", "references/" in content)
        check("Skill has resource-root discovery", "MASTER_DESIGN_ROOT" in content)

    # Summary
    print("\n" + "="*60)
    passed = sum(1 for c in CHECKS if c['status'] == 'PASS')
    failed = sum(1 for c in CHECKS if c['status'] == 'FAIL')
    print(f"Results: {passed} PASS, {failed} FAIL, {len(CHECKS)} total")
    print("="*60)

    if failed == 0:
        print("\n[OK] ALL CHECKS PASSED")
        return 0
    else:
        print(f"\n[FAIL] {failed} CHECK(S) FAILED")
        for c in CHECKS:
            if c['status'] == 'FAIL':
                print(f"  - {c['name']}")
        return 1

if __name__ == "__main__":
    sys.exit(main())


