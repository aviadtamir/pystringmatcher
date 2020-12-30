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

    @staticmethod
    def find_matches(matcher):
        """
        The Method responsible for running the matching algorithm on the text chunk it receives,
        the matcher runs the algorithm concurrently on every pattern searched using a concurrent.futures.ThreadPoolExecutor
        :return: None
        """
        for pattern in matcher.patterns:
            matcher.matches[pattern] = matcher.text_chunk.find_matches_in_chunk(pattern, matcher.text_chunk.text,
                                                                                matcher.algorithm)
        return matcher

    @property
    def matches(self) -> Dict:
        return self._matches

    @property
    def patterns(self) -> List[str]:
        return self._patterns

    @property
    def algorithm(self):
        return self._algorithm

    @property
    def text_chunk(self):
        return self._text_chunk
