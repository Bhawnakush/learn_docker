import os
folder=input("please provide list of foler name: ").split()
for folder in folder:
    try:

     files=os.listdir(folder)
    except FileNotFoundError: 
     print("==== lisiting fies for the folder -"+folder)
    except PermissionError:
       break


    for file in files:
        print(file)


#os talks to the operating system and in os listdir  print the file in 
