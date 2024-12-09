## Description 
parse_git_index.py and decompresser.py are both used to make git files human-readable 


## parse_git_index.py
parse_git_index.py is used to parse a .git/index file (in binary) and make it readable 
#### Usage and flags 
```
usage: python parse_git_index.py [-h] -i INPUT -o
                          OUTPUT

Parse a .git/index file to a human-readable
format.

options:
  -h, --help            show this help message
                        and exit
  -i INPUT, --input INPUT
                        Path to the input
                        .git/index file
  -o OUTPUT, --output OUTPUT
                        Path to save the parsed
                        output
```


## decompresser.py 
decompresser.py decompresses binary git objects (trees/blobs) files especially gotten from .git/index (and have been already downloaded locally to a designated directory).

It would scan a specified directory/folder for git objects and overwrite any binary git object with the decompressed form of it. 
#### Usage and flags 
```
usage: decompresser.py [-h] -i INPUT

Decompress binary git tree/blob files.

options:
  -h, --help            show this help message
                        and exit
  -i INPUT, --input INPUT
                        Directory containing
                        binary files to
                        decompress.
```

