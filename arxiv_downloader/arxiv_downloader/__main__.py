from os import getenv
from argparse import ArgumentParser
from .download_file import download_file
from .setup_credentials import setup_credentials

parser = ArgumentParser(
    prog="arxiv-downloader",
    description="downloads arxiv files in bulk from s3"
)
parser.add_argument('--creds', type=str,
                    help='path to aws config file', required=False)
parser.add_argument('--destination', type=str,
                    help='directory to download arxiv tars to')
args = parser.parse_args()
credentials_path = args.creds if args.creds is not None else getenv(
    'AWS_CREDENTIALS')
s3resource = setup_credentials(credentials_path)
print(args)
print(download_file('src/arXiv_src_manifest.xml', args.destination, s3resource))
