from pathlib import Path

from aegisrag.markdown import parse_sections
from aegisrag.markdown import parse_heading

print(parse_heading("# Incident"))
print(parse_heading("## Root Cause"))
print(parse_heading("### Database Configuration"))
print(parse_heading("Normal text"))
print(parse_heading("##No space"))


content = Path(
    "data/documents/test_no_heading.md"
).read_text(encoding="utf-8")
test_content = """# Incident INC-2026-1042

Introduction.

## Root Cause

Database configuration was incompatible.

## Resolution

The deployment was rolled back.
"""

print(parse_sections(test_content))

print(parse_sections(content))