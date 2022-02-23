
import json
import os
import re
from typing import FrozenSet, List


class I18NLogParser:

    def parse_log_file(self, log_file: str) -> FrozenSet[str]:
        keys = set()

        if not os.path.exists(log_file):
            print(f'File {log_file} not found')
            return keys

        # Value of key 'KEY' is not a string or function
        key_pattern = re.compile(r"Value of key '([^']+)' is not a string or function")

        with open(log_file, 'r') as f:
            for line in f.readlines():
                for match in key_pattern.finditer(line):
                    keys.add(match.group(1))

        return keys

    def parse_log_files(self, log_files: List[str]) -> FrozenSet[str]:
        keys = set()

        for log_file in log_files:
            keys = keys.union(self.parse_log_file(log_file))

        return keys

    def write_keys(self, keys: FrozenSet[str], lang_files: List[str]):
        for lang_file in lang_files:
            lang_file_keys = dict()
            if os.path.exists(lang_file):
                lang_file_keys = json.load(open(lang_file, 'r'))

            for key in keys:
                if key not in lang_file_keys:
                    lang_file_keys[key] = ''

            json.dump(lang_file_keys, open(lang_file, 'w'), indent=4, ensure_ascii=False)
