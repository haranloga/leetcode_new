myData = "I'm sample data to be written to a file"
f = open("files/py.txt", "a")
f.write(myData)
f.close()