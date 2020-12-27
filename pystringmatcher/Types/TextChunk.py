from cached_property import cached_property
from .Line import Line
from typing import List
from . import Match


class TextChunk:
    """
    This Class represents a chunk of text derived from the original text file input
    """
    def __init__(self, lines: List[Line], index: int):
        self._lines = lines
        self._index = index

    @property
    def index(self) -> int:
        return self._index

    @property
    def lines(self) -> List[Line]:
        return self._lines

    @property
    def number_of_lines(self) -> int:
        return len(self.lines)

    @property
    def size(self) -> int:
        return len(self.text)

    @cached_property
    def text(self) -> str:
        return "".join([line.text for line in self.lines])

    @property
    def chunk_file_start_offset(self) -> int:
        return self.lines[0].offset_in_file

    @property
    def chunk_file_end_offset(self) -> int:
        last_line = self.lines[len(self.lines) - 1]
        return last_line.offset_in_file + last_line.size

    def find_matches_in_chunk(self, pattern: str, text: str, algorithm) -> List[Match]:
        matches = algorithm.run(pattern=pattern, text=text)
        return [self._normalize_match_to_file(match) for match in matches]

    def _normalize_match_to_file(self, match: Match) -> Match:
        """
        :param match: the match object found by the algorithm
        :return: the input match object, with updated properties, normalized to the scale of the input
                 text file measures
        """
        match.char_offset = match.char_offset + self.chunk_file_start_offset
        for line in self.lines:
            if match.char_offset >= line.offset_in_file:
                if match.char_offset < line.end_offset:
                    match.line_offset = self.lines.index(line) + (self.index * self.number_of_lines)
        return match
