import boto3
import botocore


def download_file(key, dlpath, s3resource):
    dlpath = dlpath[:-1] if dlpath.endswith('/') else dlpath
    try:
        s3resource.meta.client.download_file(
            Bucket='arxiv',
            Key=key,
            Filename=dlpath + "/" + key.split('/')[-1],
            ExtraArgs={'RequestPayer': 'requester'}
        )
    except Exception as exception:
        raise exception

