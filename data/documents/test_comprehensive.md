## Introduction

This is a short intro section that easily fits inside a single chunk.

## Setup Instructions

This section has multiple paragraphs and is intentionally long enough that it will not fit inside a single small chunk, forcing the chunker to split it into more than one piece using its greedy paragraph packing logic.

Here is a second paragraph in this same section, also fairly long, adding more content so that the total length of this section clearly exceeds a small max chunk size like one hundred and fifty characters.

Here is a third paragraph, just to make sure there is enough content for the splitting logic to actually produce three or more chunks from this one section alone.

## Code Example

```python
def greet(name):
    return f"Hello, {name}"
```

This closed code block should be preserved as plain text and not misread as containing any headings.

## Unclosed Section

```text
def broken():
    return "this fence never closes"


Save this as `data/documents/test_comprehensive.md`.

Before running it, Priyansh — predict, section by section:
- `## Introduction`: how many chunks?
- `## Setup Instructions`: roughly how many chunks, given three paragraphs and a small `max_chunk_size` like 150?
- `## Code Example`: how many chunks, and does the code text survive intact inside it?
- `## Unclosed Section`: does the warning fire? What title does it report?

Write your predictions, then run `run_pipeline(Path("data/documents/test_comprehensive.md"), max_chunk_size=150, overlap=20)` and compare.