import argparse

from log_parser import I18NLogParser

parser = argparse.ArgumentParser()
parser.add_argument(
    '--log_file', dest='log_file', action='append',
    required=True, help='Log file to parser'
)
parser.add_argument(
    '--lang_file', dest='lang_file', action='append',
    required=True, help='JSON language files with the keys to translate'
)


if __name__ == '__main__':
    options = parser.parse_args()
    log_parser = I18NLogParser()
    keys = log_parser.parse_log_files(options.log_file)
    log_parser.write_keys(keys, options.lang_file)
