import logging

def parse_heading(line : str):
    if not line.startswith("#"):
        return None

    stripped = line.lstrip("#")

    if not stripped.startswith(" "):
        return None
    
    title = line.lstrip("#").strip()
    level = len(line) - len(line.lstrip("#"))

    return level, title

def finish_section(section):
    section["content"] = "\n".join(section.pop("lines")).strip()
    return section

def parse_sections(content : str):
    sections = []
    current_section = None
    in_code_block = False

    for line in content.splitlines():

        if line.startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            if current_section is None:
                current_section = {"level": 0, "title": None, "lines": []}
            current_section ["lines"].append(line)
            continue
        else:

            heading = parse_heading(line)

        if heading is not None:
            if current_section is not None:
                sections.append(finish_section(current_section))

            level, title = heading
            current_section = {"level": level, "title": title, "lines": []}

        elif current_section is None:

            current_section = {"level": 0, "title": None}

            current_section["lines"] = []

            current_section["lines"].append(line)

        else:
            current_section["lines"].append(line)

    if current_section is not None:
        if in_code_block:
            if current_section["title"] is None:
                logging.warning(f"Unclosed code fence detected, trace them at: {current_section['lines']}")
            else:
                logging.warning(f"Unclosed code fence detected: {current_section['title']}")
        sections.append(finish_section(current_section))
        

    return sections


# content_1 = "Some intro text.\n\n## Setup\n\nMore text."
# content_2 = "```python\n# not a heading\nx = 1\n```\n\nSome text after."
# print(parse_sections(content_1))
# print(parse_sections(content_2))

# content_unclosed = "## Notes\n\n```python\ndef broken():\n    return 1\n\nSome text after."

# print(parse_sections(content_unclosed)) 