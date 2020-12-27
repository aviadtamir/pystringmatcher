class TestLine:

    def test_size(self, line):
        assert line.size == 5

    def test_end_offset(self, line):
        assert line.end_offset == 5

    def test_text(self, line):
        assert line.text == "aaaaa"

    def test_offset_in_file(self, line):
        assert line.offset_in_file == 0
