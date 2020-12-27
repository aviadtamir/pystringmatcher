import pytest


class TestAlgorithms:

    @pytest.mark.parametrize("text, pattern,  num_matches, matches_char_offsets, matches_line_offsets",
                             [
                                 ("abcdefghijkl", "ab", 1, [0], [1]),
                                 ("abcdefghasdfgcvgbn", "a", 2, [0, 8], [1]),
                                 ("abcdefghijklmnop", "w", 0, [], []),
                                 ("""abcdefghijklmnopqrstuv""", "h", 1, [7], [2])
                             ])
    def test_rabin_karp_algorithm(self, rabin_karp, text, pattern, num_matches, matches_char_offsets,
                                  matches_line_offsets):
        matches = rabin_karp.run(text=text, pattern=pattern)
        assert len(matches) == num_matches
        for i, match in enumerate(matches):
            if matches_char_offsets:
                assert match.char_offset == matches_char_offsets[i]
