from typing import Dict


class Aggregator:
    """
    The aggregator class that aggregates the all matches from the matcher objects
    """
    def __init__(self, matchers):
        self._matchers = matchers
        self._aggregated_matches = {}

    def aggregate_matches(self):
        """
        The method of aggregating the matches from all the matcher objects
        :return: None
        """
        for matcher in self._matchers:
            for pattern in matcher.patterns:
                if self._aggregated_matches.get(pattern):
                    # if the pattern already exists -> extend its matches list entry
                    if matcher.matches.get(pattern):
                        self._aggregated_matches[pattern].extend(matcher.matches[pattern])
                else:
                    # if the pattern doesn't already exists -> create its matches list entry
                    if matcher.matches.get(pattern):
                        self._aggregated_matches[pattern] = matcher.matches[pattern]
        return self.aggregated_matches

    @property
    def aggregated_matches(self) -> Dict:
        return self._aggregated_matches
