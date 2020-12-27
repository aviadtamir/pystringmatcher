class TestTextChunk:

    def test_number_of_lines(self, text_chunk):
        assert text_chunk.number_of_lines == 3

    def test_size(self, text_chunk):
        assert text_chunk.size == 12

    def test_text(self, text_chunk):
        assert text_chunk.text == "aaaabbbbcccc"

    def test_offsets(self, text_chunk):
        assert text_chunk.chunk_file_start_offset == 0
        assert text_chunk.chunk_file_end_offset == 12
