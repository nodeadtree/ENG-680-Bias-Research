import fitz

# TODO: Parse files into text


def parse_file_as_text(filepath, collectors=None):
    doc = fitz.open(filepath)
    text = map(lambda x: x.getText(), doc)
    results = "".join(text)
    # return map(lambda x: x(results), collectors)
    return results
