![badge](https://github.com/aviadtamir/pystringmatcher/workflows/pystringmatcher%20CI%5cCD/badge.svg)
[![PyPI version fury.io](https://badge.fury.io/py/pystringmatcher.svg)](https://pypi.python.org/pypi/pystringmatcher/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pystringmatcher.svg)](https://pypi.python.org/pypi/pystringmatcher/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/aviadtamir/pystringmatcher)
# pystringmatcher

## description
a small utility tool for finding substrings and text patterns in an input file
the tool is cutting the text in the file into chunks and processes every chunk in a separate process
using python's multiprocessing module

## installation:
```bash
pip install pystringmatcher
```

### usage:
* using the python module
```bash
python -m py pyringmatcher -h

Finding text patterns in input text file

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_PATH, --file FILE_PATH
                        the input file to search the patterns in
  -p PATTERNS, --patterns PATTERNS
                        the pattern\s to search in the file separated by ,
  -n NUM_LINES_PER_CHUNK, --num-lines NUM_LINES_PER_CHUNK
                        the number of lines per chunk of text from the input file
```

* or by using the included console script

```bash
stringmatcher -h 
```
* In your own program

```python
import os
from multiprocessing.pool import Pool

from pystringmatcher.Objects import Aggregator
from pystringmatcher.Algorithms import RabinKarp
from pystringmatcher.Objects import Matcher
from pystringmatcher.Types import TextFile


try:
    text = TextFile(file_path="/path/to/file")
    algorithm = RabinKarp()
    chunks = text.divide_into_chunks(num_of_lines_each_chunk=1000)
    patterns = "alpha,beta,charlie,delta,echo,foxtrot".split(",")
    print(f"[X] - Start finding the patterns : {patterns} in the file: {text}")
    matches = text.find_matches(chunks=chunks, patterns=patterns, algorithm=algorithm)

    if matches:
        print("Found matches")
        print(matches)

    print("No matches were found")
except FileNotFoundError:
    print(f"The file: {text} was not found and may not exist")
``` 
* Implementing your own matching algorithm
```python

from pystringmatcher.Algorithms import Algorithm
from pystringmatcher.Types import Match


class MyAlgorithm(Algorithm):
    
    def preprocess(self, pattern, text, *args, **kwargs):
        """some preprocess logic goes here if needed"""
    
    def run(self, pattern, text, *args, **kwargs):
        matches = []
        """the mathcing algorithm logic goes here
        for any match: matches.append(Match(char_offset=start_index_of_match)) 
        """         
        return matches
        
```