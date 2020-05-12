from os.path import join, abspath, split
from glob import glob
import xml.etree.ElementTree as ET


def parse_index(xml_file):
    root = ET.parse(xml_file)
    parsed_file = dict(((i.find('filename').text, {
        'size': i.find('size').text,
        'md5sum': i.find('md5sum').text
    }) for i in root.findall('file')))
    return parsed_file


def diff_manifest(manifest, directory):
    files = set(map(abspath, glob(join(directory, '**'), recursive=True)))
    return (i for i in manifest.keys() if join(directory, i) not in files)
