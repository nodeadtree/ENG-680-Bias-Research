from .download_file import download_file
from .setup_credentials import setup_credentials

print(download_file('src/arXiv_src_manifest.xml', setup_credentials()))
