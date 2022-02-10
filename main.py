

read = open("ETP.config","r")
content = read.readlines()
read.close()
start = 1
i=0; 
while(start):
    dummy=content[i].split()
    if(content[i] != "\n" ):
        if dummy[0] != "#":
            print(content[i])
    if(content[i]== "# End of deprecated options\n"): 
            start = 0
    i=i+1
#dummy=content[4].split()
#print(dummy[0])
