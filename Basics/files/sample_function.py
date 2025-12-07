def storeFile(file,append):
    f = open(file, 'a')
    f.write(append)
    f.close()
    f = open(file, 'r') 
    contents = f.read()
    f.close()
    return contents

# Variable to store the filename
fileVar = "files/py.txt"
append ="hello there"

contents = storeFile(fileVar,append)
print(contents)