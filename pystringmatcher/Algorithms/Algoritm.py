from abc import ABC, abstractmethod
from typing import List
from pystringmatcher.Types import Match


class Algorithm(ABC):

    """
    The base Abstract class for implementing string pattern matching algorithm
    """
    @abstractmethod
    def preprocess(self, pattern: str, text: str, *args, **kwargs) -> str:
        """ base abstract preprocessing method """
        raise NotImplementedError

    @abstractmethod
    def run(self, pattern: str, text: str, *args, **kwargs) -> List[Match]:
        """ base abstract matching method """
        raise NotImplementedError
