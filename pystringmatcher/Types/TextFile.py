import os
import pathlib
from multiprocessing.pool import Pool
from typing import List

from cached_property import cached_property


from .Line import Line
from . import TextChunk


class TextFile:
    """
    This class represents a text file input got from the user
    """

    def __init__(self, file_path: str):
        self._file_path = file_path

    @cached_property
    def lines(self) -> List[Line]:
        try:
            lines = []
            file_offset = 1
            with open(self._file_path, "r") as _file:
                for line in _file:
                    lines.append(Line(text=line, offset_in_file=file_offset))
                    file_offset += len(line)
            return lines
        except FileNotFoundError as e:
            # if the file wasn't found, notify the caller and handle the exception
            raise e

    @property
    def size(self) -> int:
        try:
            return pathlib.Path(self._file_path).stat().st_size
        except FileNotFoundError as e:
            # if the file wasn't found, notify the caller and handle the exception
            raise e

    @cached_property
    def text(self) -> str:
        return "".join([line.text for line in self.lines])

    def divide_into_chunks(self, num_of_lines_each_chunk: int) -> List[TextChunk]:
        """
        This method divides the text file into multiple chunks
        :param num_of_lines_each_chunk: the maximum number of lines in each chunks,
               if the total number of lines in the file % num_of_lines_each_chunk != 0 than the last chunk will
               get all the left lines(< num_of_lines)
        :return: a list of TextChunk Objects
        """
        return [TextChunk(lines=self.lines[i:i + num_of_lines_each_chunk], index=i + 1) for i in
                range(0, len(self.lines), num_of_lines_each_chunk)]

    @staticmethod
    def find_matches(chunks, patterns, algorithm):
        from pystringmatcher.Objects.Matcher import Matcher
        from pystringmatcher.Objects.Aggregator import Aggregator
        pool = Pool(processes=os.cpu_count())
        matchers = []

        for chunk in chunks:
            matcher = Matcher(text_chunk=chunk, patterns=patterns, algorithm=algorithm)
            matchers.append(matcher)
        matchers = pool.map(Matcher.find_matches, matchers)
        aggregator = Aggregator(matchers=matchers)
        return aggregator.aggregate_matches()

