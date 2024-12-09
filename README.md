## Description 
parse_git_index.py and decompresser.py are both used to make git files human-readable 

## parse_git_index.py
parse_git_index.py is used to parse a .git/index file (in binary) and make it readable 
#### usage and flags 
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
