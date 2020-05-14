import fitz

# TODO: Parse files into text


def parse_file_as_text(filepath):
    fitz.TOOLS.mupdf_display_errors(value=False)
    doc = fitz.open(filepath)
    text = map(lambda x: x.getText(), doc)
    meta = doc.metadata
    results = "".join(text)
    return (results, meta)
