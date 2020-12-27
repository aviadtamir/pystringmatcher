from .Algoritm import Algorithm
from pystringmatcher.Types import Match


class RabinKarp(Algorithm):
    alpha_len = 2097152
    """
        Implementation of the BoyerMoore string matching Algorithm
    """

    def preprocess(self, pattern, text, *args, **kwargs):
        pass

    def calc_hash(self, pattern, prime):
        hash_val = 0

        for char in pattern:
            hash_val = (self.alpha_len * hash_val + ord(char)) % prime

        return hash_val

    def recalc_hash(self, old_hash, old_char, new_char, h, prime):
        new_hash = old_hash - (ord(old_char) * h)
        new_hash = (new_hash * self.alpha_len) + ord(new_char)
        new_hash = new_hash % prime

        if new_hash < 0:
            new_hash = new_hash + prime

        return new_hash

    def run(self, pattern, text, *args, **kwargs):
        prime = 101
        matches = []
        pl = len(pattern)
        tl = len(text)
        h = pow(self.alpha_len, pl - 1)

        # hash value of pattern
        pattern_hash = self.calc_hash(pattern, prime)
        # first window hash
        win_hash = self.calc_hash(text[:pl], prime)

        # windows sliding
        for i in range(0, tl - pl - 1):
            if pattern_hash == win_hash:
                if pattern == text[i: i + pl]:
                    matches.append(Match(char_offset=i))
            ## next window hash val
            win_hash = self.recalc_hash(
                old_char=text[i],
                old_hash=win_hash,
                new_char=text[i + pl],
                h=h,
                prime=prime
            )

        return matches
