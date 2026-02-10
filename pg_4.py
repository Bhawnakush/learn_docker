import os
folder=input("please provide list of foler name: ").split()
for folder in folder:
    
    files=os.listdir(folder)
    print("==== lisiting fies for the folder -"+folder)

    for file in files:
        print(file)


#os talks to the operating system and in os listdir  print the file in 
