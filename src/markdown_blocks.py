def markdown_to_blocks(markdown):
    splitted_lines = markdown.split("\n\n")
    new_lines = []
    for line in splitted_lines:
        stripped = line.strip()
        if stripped:
            new_lines.append(stripped)
    return new_lines
