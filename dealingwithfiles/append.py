try:
    # open file
    fileobject=open("mycv.txt", "a")  # TextIOWrapper
except Exception as e:
    print(e)
else:
    print(fileobject)
    # write content to the file
    fileobject.write("#####################################\n")
    fileobject.write("hejhfgakwjgjh\n")
    fileobject.writelines(["iti\n", "python\n", "we need the break\n",
                           "welcome\n"])
    fileobject.close()