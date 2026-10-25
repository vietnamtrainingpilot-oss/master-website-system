#!/usr/bin/env python3
"""
Validation script for Master Website Skill (skill-only structure).
Run from the skill root directory.
"""
import os
import json
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).parent

CHECKS = []

def check(name, condition, evidence=""):
    status = "PASS" if condition else "FAIL"
    CHECKS.append({"id": len(CHECKS)+1, "name": name, "status": status, "evidence": evidence})
    icon = "[OK]" if condition else "[FAIL]"
    print(f"  {icon} {name}: {status} {evidence}")
    return condition

def main():
    print("============================================================")
    print("  Master Website Skill - Validation (Skill-Only Structure)")
    print("============================================================")
    print()

    # 1. Core files exist
    print("Core Implementation:")
    check("Main SKILL.md exists", (SKILL_ROOT / "SKILL.md").exists())
    check("Skill README exists", (SKILL_ROOT / "README.md").exists())

    # 2. SKILL.md size >= 10KB (skill-only is smaller)
    skill_path = SKILL_ROOT / "SKILL.md"
    skill_size = skill_path.stat().st_size if skill_path.exists() else 0
    check(f"SKILL.md size >= 10KB ({skill_size/1024:.1f} KB)", skill_size >= 10000)

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
        check(f"Reference: {ref}", (SKILL_ROOT / f"references/{ref}").exists())

    # 4. Catalogs
    print("\nCatalogs:")
    check("Design systems AGENTS.md", (SKILL_ROOT / "references/design-systems/AGENTS.md").exists())
    check("Design templates AGENTS.md", (SKILL_ROOT / "references/design-templates/AGENTS.md").exists())

    # 5. Phase files (A-M)
    print("\nPhase Playbooks:")
    for phase in "ABCDEFGHIJKLM":
        phase_file = f"phase-{phase.lower()}-{'intake' if phase=='A' else 'research' if phase=='B' else 'design-direction' if phase=='C' else 'design-system' if phase=='D' else 'template' if phase=='E' else 'implement' if phase=='F' else 'animation' if phase=='G' else 'engineering' if phase=='H' else 'browser' if phase=='I' else 'test' if phase=='J' else 'fix' if phase=='K' else 'deliver' if phase=='L' else 'video'}.md"
        check(f"Phase {phase} playbook", (SKILL_ROOT / f"references/{phase_file}").exists())

    # 5. Specialty guides
    print("\nSpecialty Guides:")
    guides = ["pptx-guide.md", "docs-guide.md", "brand-guide.md", "animation-guide.md", "video-guide.md"]
    for guide in guides:
        check(f"Guide: {guide}", (SKILL_ROOT / f"references/{guide}").exists())

    # 6. Source skills reference
    print("\nSource Skills Reference:")
    skills_dir = SKILL_ROOT / "references/skills"
    if skills_dir.exists():
        skill_count = len([d for d in skills_dir.iterdir() if d.is_dir()])
        check(f"Source skills count: {skill_count} (expected 169)", skill_count >= 160)
    else:
        check("Source skills directory exists", False)

    # 6. Installer
    print("\nInstaller:")
    check("install.ps1 exists (optional)", (SKILL_ROOT / "install.ps1").exists())

    # 7. Command Structure
    print("\nCommand Structure:")
    cmd_path = SKILL_ROOT / "commands/master-website.md"
    if cmd_path.exists():
        content = cmd_path.read_text(encoding='utf-8')
        check("Command has frontmatter", content.startswith("---"))
        check("Command references \$ARGUMENTS", "$ARGUMENTS" in content)
        check("Command invokes skill", "master-website" in content)
    else:
        check("Command file exists (optional)", False)

    # 8. Skill Structure
    print("\nSkill Structure:")
    if (SKILL_ROOT / "SKILL.md").exists():
        content = (SKILL_ROOT / "SKILL.md").read_text(encoding='utf-8')
        check("Skill has frontmatter", content.startswith("---"))
        check("Skill has Phases A-M", "Phase A" in content and "Phase M" in content)
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

if __name__ == '__main__':
    sys.exit(main())

