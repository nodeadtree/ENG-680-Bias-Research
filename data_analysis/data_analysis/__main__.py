from os.path import join, abspath
from glob import glob
from collections import Counter
from argparse import ArgumentParser
from multiprocessing import Pool
from .collectors import strict_preprocessor
from .parser import parse_file_as_text
from json import dump


def parse_and_lemmatize(document):
    try:
        raw, meta = parse_file_as_text(document)
        corpus = strict_preprocessor(raw)
        count = Counter(corpus)
        return {'meta': meta, 'counted': count}
    except Exception as e:
        return {'error': str(e)}


def get_rough_numeric_data(target, output, result_size=1000):
    files = set(map(abspath, glob(join(target, '**/*.pdf'), recursive=True)))
    with Pool() as p:
        results = list()
        dump_count = 0
        for i in p.imap(parse_and_lemmatize, files, 100):
            if len(results) > result_size:
                dump_count += 1
                fname = join(output, f'computed_data_{dump_count}')
                with open(fname, 'w') as f:
                    print(f'wrote data to {fname}')
                    dump(results, f)
                results = list()
            else:
                results.append(i)
        else:
            fname = join(output, f'computed_data_{dump_count+1}')
            with open(fname, 'w') as f:
                print(f'wrote data to {fname}')
                dump(results, f)


arg_parser = ArgumentParser(
    prog="data_analysis",
    description="data analysis portion for eng680 project"
)
arg_parser.add_argument('--target', type=str, help='files to examine')
arg_parser.add_argument('--output', type=str, help='where to put results')
args = arg_parser.parse_args()

get_rough_numeric_data(args.target, args.output)
