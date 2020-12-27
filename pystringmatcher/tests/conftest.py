import pytest
from pystringmatcher.Types import TextFile, Match, TextChunk, Line
from pystringmatcher.Algorithms import RabinKarp


@pytest.fixture()
def text_file_fixture():
    return TextFile(file_path="test.txt")


@pytest.fixture()
def rabin_karp():
    return RabinKarp()


@pytest.fixture()
def match():
    return Match(char_offset=31)


@pytest.fixture()
def lines():
    return [Line(text="aaaa", offset_in_file=0),
            Line(text="bbbb", offset_in_file=4),
            Line(text="cccc", offset_in_file=8)]


@pytest.fixture()
def text_chunk(lines):
    return TextChunk(lines=lines, index=1)


@pytest.fixture()
def line():
    return Line(text="aaaaa", offset_in_file=0)
