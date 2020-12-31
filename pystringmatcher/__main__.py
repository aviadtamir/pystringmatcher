import argparse
import logging
import os
from multiprocessing.pool import Pool
from pystringmatcher.Objects import Aggregator
from pystringmatcher.Algorithms import RabinKarp
from pystringmatcher.Objects import Matcher
from pystringmatcher.Types import TextFile


def validate_arg(arg):
    if not arg:
        logging.error(f"incorrect or missing parameter, use -h or --help params for usage instructions")
        exit(1)
    return arg


def init_args():
    logging.basicConfig(format='[X] - [%(levelname)s]   %(message)s', level=logging.DEBUG)
    parser = argparse.ArgumentParser(description='Finding text patterns in input text file')
    parser.add_argument("-f", "--file", dest="file_path", help="the input file to search the patterns in")
    parser.add_argument("-p", "--patterns", dest="patterns",
                        help=r"the pattern\s to search in the file separated by ,")
    parser.add_argument("-n", "--num-lines", dest="num_lines_per_chunk", type=int,
                        help="the number of lines per chunk of text from the input file, default=1", default=1)
    return parser.parse_args()


def main():
    args = init_args()
    file_path = validate_arg(args.file_path)
    patterns = validate_arg(args.patterns)
    num_lines_per_chunk = validate_arg(args.num_lines_per_chunk)
    try:
        text_file = TextFile(file_path=file_path)
        algorithm = RabinKarp()
        chunks = text_file.divide_into_chunks(num_of_lines_each_chunk=num_lines_per_chunk)
        patterns = patterns.split(",")
        logging.info(f"[X] - Start finding the patterns : {patterns} in the file: {file_path}")
        matches = text_file.find_matches(chunks=chunks, patterns=patterns, algorithm=algorithm)
        if matches:
            logging.info("Found matches")
            logging.info(matches)
            return
        logging.info("No matches were found")
    except FileNotFoundError:
        logging.error(f"The file: {file_path} was not found and may not exist")
    except KeyboardInterrupt:
        logging.info("Cancelled by user")


if __name__ == "__main__":
    main()
