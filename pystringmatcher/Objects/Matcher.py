import os
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict

from pystringmatcher.Algorithms import Algorithm
from pystringmatcher.Types import TextChunk


class Matcher:
    """
    The Matcher class responsible for running the string matching algorithm
    """
    def __init__(self, text_chunk: TextChunk, patterns: List[str], algorithm: Algorithm):
        self._text_chunk = text_chunk
        self._patterns = patterns
        self._algorithm = algorithm
        self._matches = {}

    def find_matches(self):
        """
        The Method responsible for running the matching algorithm on the text chunk it receives,
        the matcher runs the algorithm concurrently on every pattern searched using a concurrent.futures.ThreadPoolExecutor
        :return: None
        """
        with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
            for pattern in self._patterns:
                self._matches[pattern] = ((executor.submit(self._text_chunk.find_matches_in_chunk, pattern,
                                                           self._text_chunk.text, self._algorithm).result()))

    @propertys
    def matches(self) -> Dict:
        return self._matches

    @property
    def patterns(self) -> List[str]:
        return self._patterns
