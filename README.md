![badge](https://github.com/aviadtamir/pystringmatcher/workflows/pystringmatcher%20CI%5cCD/badge.svg)
[![PyPI version fury.io](https://badge.fury.io/py/pystringmatcher.svg)](https://pypi.python.org/pypi/pystringmatcher/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pystringmatcher.svg)](https://pypi.python.org/pypi/pystringmatcher/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/aviadtamir/pystringmatcher)
# pystringmatcher

## description
a small utility tool for finding substrings and text patterns in an input file
by dividing the file into chunks and processing them concurrently
## installation:
```bash
pip install pystringmatcher
```

### usage:
* using the python module
```bash
python -m py pystringmatcher -h

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
from concurrent.futures import ThreadPoolExecutor

from pystringmatcher.Objects import Aggregator
from pystringmatcher.Algorithms import RabinKarp
from pystringmatcher.Objects import Matcher
from pystringmatcher.Types import TextFile


try:
    file_path = r"/path/to/file.txt"
    text = TextFile(file_path=file_path) # raises FileNotFoundError if the file doesn't exist 
    algorithm = RabinKarp() # implemented in package in .Algorithms
    chunks = text.divide_into_chunks(num_of_lines_each_chunk=1000)
    matchers = []
    patterns = "alpha,beta,charlie,delta".split(",")
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        for chunk in chunks:
            matcher = Matcher(text_chunk=chunk, patterns=patterns, algorithm=algorithm)
            matchers.append(matcher)
            executor.submit(matcher.find_matches)
    aggregator = Aggregator(matchers=matchers)
    aggregator.aggregate_matches()
    if aggregator.aggregated_matches:
        print(f"Found matches")
        print(aggregator.aggregated_matches)
except FileNotFoundError:
    print(f"The file: {file_path} was not found and may not exist")
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
        
        
    




    







```