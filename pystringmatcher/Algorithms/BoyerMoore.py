from .Algoritm import Algorithm
from pystringmatcher.Types import Match


class BoyerMoore(Algorithm):
    """
    Implementation of the BoyerMoore string matching Algorithm
    """

    def preprocess(self, pattern, text, *arg, **kwargs):
        pass

    def run(self, pattern: str, text: str, *arg, **kwargs):
        matches = []
        good_suffix = self.generate_suffix_shift(pattern)
        bad_char = self._generate_bad_char_shift(pattern)
        i = len(pattern) - 1
        while i < len(text) - 1:
            j = 0
            while j < len(pattern) and pattern[len(pattern) - j - 1] == text[i - j - 1]:
                j += 1
            if j == len(pattern):
                # pattern has been found here
                # can be replaced by a counter
                return Match(char_offset=j)
            else:
                t = bad_char.get(text[i - j - 1])
                if t is None:
                    t = 6
                k = good_suffix.get(j)
                if k is None:
                    k = 0

                d1 = t - j

                i += max(d1, k)
        return matches

    # Generate the Bad Character Skip List
    @staticmethod
    def _generate_bad_char_shift(term):
        skip_list = {}
        for i in range(0, len(term) - 1):
            skip_list[term[i]] = len(term) - i - 1
        return skip_list

    # Generate the Good Suffix Skip List
    @staticmethod
    def _find_suffix_position(bad_char, suffix, full_term):
        for offset in range(1, len(full_term) + 1)[::-1]:
            flag = True
            for suffix_index in range(0, len(suffix)):
                term_index = offset - len(suffix) - 1 + suffix_index
                if term_index < 0 or suffix[suffix_index] == full_term[term_index]:
                    pass
                else:
                    flag = False
            term_index = offset - len(suffix) - 1
            if flag and (term_index <= 0 or full_term[term_index - 1] != bad_char):
                return len(full_term) - offset + 1

    def generate_suffix_shift(self, key):
        skip_list = {}
        buffer = ""
        for i in range(0, len(key)):
            skip_list[len(buffer)] = self._find_suffix_position(key[len(key) - 1 - i], buffer, key)
            buffer = key[len(key) - 1 - i] + buffer
        return skip_list
