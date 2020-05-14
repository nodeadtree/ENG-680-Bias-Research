import pytest
from os import getenv
from data_analysis import parse_file_as_text, strict_pre_processor


"""
This should be set pointing to some pdf to test with
Would provide pdf, but licenses spooky and me no lawyer
"""
_URI = getenv('DATA_ANALYSIS_TARGET')


def test_strict_preprocessor():
    corpus, metadata = parse_file_as_text(_URI)
    processed = strict_pre_processor(corpus)
    print(processed)
    assert False
