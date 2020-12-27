class Line:
    """
    The Class that represents a line of text with its properties
    """
    def __init__(self, text, offset_in_file):
        self._text = text
        self._offset_in_file = offset_in_file

    @property
    def size(self) -> int:
        return len(self._text)

    @property
    def end_offset(self) -> int:
        return self._offset_in_file + self.size

    @property
    def text(self) -> str:
        return self._text

    @property
    def offset_in_file(self) -> int:
        return self._offset_in_file
