import os

def ropen(file_path):
    """ Reading file backwards """
    file = open( file_path, 'r' )
    file_size = os.path.getsize( file_path )
    file_range = range(file_size)

    for i in file_range:
        file.seek(file_range[-i])
        char = file.read(1)
        if char == "\n":
            line = file.readline()
            if len(line) > 1:
                print( line )
