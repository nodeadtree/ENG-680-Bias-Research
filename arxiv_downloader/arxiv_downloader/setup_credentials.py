from os import getenv
import boto3
import configparser


def setup_credentials(path=None):
    """
    Creates S3 resource + sets configuration to enable download
    Shamelessly ripped off this medium article:
        http://briennakh.me/notes/bulk-arxiv-download
    """
    configs = configparser.ConfigParser()
    configs.read([path])
    s3resource = boto3.resource(
        's3',
        aws_access_key_id=configs['default']['aws_access_key_id'],
        aws_secret_access_key=configs['default']['aws_secret_access_key'],
        region_name='us-east-1'  # Same as arxiv bucket
    )
    return s3resource
