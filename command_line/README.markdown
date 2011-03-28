# Command-Line tools
These are my simple command-line tools written in Python just for fun :)).

## pygrep
Simple grep like functionality written in Python just for fun!

### Usage:
    1) ps aux |pygrep -r '[a-Z0-9]+'
    -> returns all lines back where matches the pattern

    2) ps aux |pygrep -r 'some string' -s ':' -o '0,1,2,3'
    -> match all lines which contain the pattern after that split result by ':' and print result list keys in -p argument 
### Example:
    echo 'How are you? ... Get out!' |pygrep -r 'are' -s '' -o '0,1' # returns: How are