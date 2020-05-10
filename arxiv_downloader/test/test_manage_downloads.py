import pytest
from os.path import join, abspath, dirname
from arxiv_downloader import parse_index


def test_list_files():
    targets = {"src/arXiv_src_9909_001.tar": {
        "md5sum": "9d3a7f34f1ac44ad3f495201e24dac90",
        "size": "213668821"},
        "src/arXiv_src_9910_001.tar": {
        "md5sum": "2f3cb5f12de7f8d7051bff7d0efdf2dd",
        "size": "244741133"},
        "src/arXiv_src_9911_001.tar": {
        "md5sum": "af128903c94a5db15b6b5bfbe472ca2f",
        "size": "221549097"},
        "src/arXiv_src_9912_001.tar": {
        "md5sum": "fb6b0f55935636c4d92445e1f4d47391",
        "size": "233445958"}
    }
    with open(join(dirname(abspath(__file__)), 'test_out/test_diff/arXiv_src_manifest.xml'), 'r') as manifest:
        outputs = parse_index(manifest)
        assert outputs == targets
