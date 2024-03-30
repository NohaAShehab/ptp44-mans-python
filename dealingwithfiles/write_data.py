
""" w mode if file doesn't exist python will try to create it
when you open file with w mode --> openning file for writing
starting from the beginning of the file
"""
try:
    # open file
    fileobject=open("mycv.txt", "w")  # TextIOWrapper
except Exception as e:
    print(e)
else:
    print(fileobject)
    # write content to the file
    # fileobject.write("#####################################\n")
    # fileobject.write("hejhfgakwjgjh\n")
    # fileobject.writelines(["iti\n", "python\n", "we need the break\n",
    #                        "welcome\n"])
    fileobject.close()