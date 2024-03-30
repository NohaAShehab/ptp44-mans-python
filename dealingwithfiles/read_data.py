

try:
    # open file
    fileobject=open("names.txt", "r")  # TextIOWrapper
except Exception as e:
    print(e)
else:
    print(fileobject)
    #read data
    dataa= fileobject.read()  # read file content into one string
    print(dataa, type(dataa))
    """ reset pointer to the beginning of the file """
    fileobject.seek(0)
    "read file line by line and put them to a list "
    lines = fileobject.readlines()  # list
    print(lines)
    """ reset pointer"""
    fileobject.seek(0)
    """ read line by line """
    data =[]  # list
    for l in fileobject:
        data.append(l)  # append line to the list
    print(data)
    # close the file
    fileobject.close()