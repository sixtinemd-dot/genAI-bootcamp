#Python - I/O

#old school way, explicty close the file after using it - using close method

# file_obj = open("file_name.txt", "w")
# your code
# file_obj.close()

#new way, use with statement
import os

# with open("secrets.txt", "r") as file_obj: #file not found error
    # your code
    # print(file_obj.read())

# solution for the error = use os module to give the full path to the file
dir_path = os.path.dirname(os.path.realpath(__file__))

# with open(dir_path + "/secrets.txt", "r") as file_obj: #file not found error
    # your code
    # print(file_obj.read())

#EXERCICE

with open(dir_path + '/starwars.txt', 'r') as f:
    txt_list = f.readlines()
    for line in txt_list:
        print(line)
    print("end of document")

    #print(txt_list[4])

    #print(txt_list[:5])

    temp =[] #step 1
    for name in txt_list: #step 2
        temp.append(list(name)) #step3

    print(temp)

    # list comprehension (backwards)

    temp = [list(name) for name in txt_list if name == "Darth\n"]
    print(temp)

    """ counts = {"Darth" : 0, "Luke" : 0, "Lea" : 0}
    for name in txt_list:
        if name == "Darth":
            counts["Darth"] += 1
        if name == "Luke":
            counts["Luke"] += 1
        if name == "Lea":
            counts["Lea"] += 1

    print(counts) """

    # better way: 

    full_txt_str = "".join(txt_list)
    counts = {"Darth" : full_txt_str.count("Darth"), 
              "Luke" : full_txt_str.count("Luke"), 
              "Lea" : full_txt_str.count("Lea")}
    
    print(counts)

with open(dir_path + '/starwars.txt', 'r+') as f:
    f.seek(0, os.SEEK_END)  
    f.write("\nSixtine")
    print("succesfully added")

    txt_list = f.readlines()
    modified_content = []
    for name in txt_list:
        if name == "Luke\n":
             modified_content.append("Luke SkyWalker\n")
        else:
             modified_content.append(name)
    
    print(modified_content)

with open(dir_path + '/starwars.txt', 'w', encoding="utf-8") as f:
    f.seek(0)
    f.writelines(modified_content)
    print("SkyWalker was added")
