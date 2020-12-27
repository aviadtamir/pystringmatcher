import pytest

from pystringmatcher.Types import TextFile


class TestTextFile:

    def test_lines(self, text_file_fixture):
        assert len(text_file_fixture.lines) == 7
        assert [line.text.replace("\n", "") for line in text_file_fixture.lines] == ["asdaffh", "asdasd", "fghgfggg",
                                                                                     "xcbxcnbx",
                                                                                     "xcvtwrhhrwbvnmv", "vbmvbnm",
                                                                                     "vbmvbmvbm"]

    def test_size(self, text_file_fixture):
        assert text_file_fixture.size == 66

    def test_text(self, text_file_fixture):
        assert text_file_fixture.text == r"""asdaffh
asdasd
fghgfggg
xcbxcnbx
xcvtwrhhrwbvnmv
vbmvbnm
vbmvbmvbm"""

    @pytest.mark.parametrize("num_lines_per_chunk, num_chunks",
                             [(7, 1),
                              (1, 7),
                              (3, 3)]
                             )
    def test_divide_to_chunks(self, text_file_fixture, num_lines_per_chunk, num_chunks):
        chunks = text_file_fixture.divide_into_chunks(num_lines_per_chunk)
        assert len(chunks) == num_chunks
        for chunk in chunks:
            assert chunk.number_of_lines <= num_lines_per_chunk

    def test_file_not_found(self):
        t = TextFile(r"/test/test.txt")
        with pytest.raises(FileNotFoundError):
            t.text

        with pytest.raises(FileNotFoundError):
            t.size
