![badge](https://github.com/aviadtamir/pystringmatcher/workflows/pystringmatcher%20CI%5cCD/badge.svg)
[![PyPI version fury.io](https://badge.fury.io/py/pystringmatcher.svg)](https://pypi.python.org/pypi/pystringmatcher/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pystringmatcher.svg)](https://pypi.python.org/pypi/pystringmatcher/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/aviadtamir/pystringmatcher)
# pystringmatcher

## description
a small utility tool for finding substrings and text patterns in an input file

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
