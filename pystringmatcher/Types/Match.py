class Match:
    """
    This Class represents a match object found in the text by the algorithm
    """
    def __init__(self, char_offset: int):
        self._char_offset = char_offset
        self._line_offset = None

    def __repr__(self):
        return "(char_offset={}, line_offset={})".format(self.char_offset, self.line_offset)

    @property
    def char_offset(self) -> int:
        return self._char_offset

    @char_offset.setter
    def char_offset(self, value: int):
        self._char_offset = value

    @property
    def line_offset(self) -> int:
        return self._line_offset

    @line_offset.setter
    def line_offset(self, value: int):
        self._line_offset = value
