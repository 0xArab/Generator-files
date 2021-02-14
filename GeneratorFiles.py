import os 

EnterNumber = int(input("Enter Passe Number : "))
EnterYourPath =  str(input(" Enter Your Path : "))
EnterNameFolder = str(input(" Folder Name : "))
EnterNameFile= str(input(" Enter Your File Name : "))
EnterTypeFile = str(input(" Enter Type File : "))

""" // Create a file in the specified path ""
def CreatePath(dirfile , namefolder ):
    """ : Here will create the folder & file """
    path = os.path.join(dirfile, namefolder)
    return os.mkdir(path)  

""" // : save file/s in folder/s """
def SaveFiles(Number , NameFolder , Path):
    if not Number and NameFolder:
       return " - [Error] Nothing - You did not enter any value  - :("
    else:
     Create = CreatePath(Path , NameFolder)
     for Loop in range(0 , Number + 1 ):
        filename = str(EnterNameFile) + "." + str(Loop) + "." + EnterTypeFile 
        with open(os.path.join(Path + str("\\") + EnterNameFolder , filename), 'a+') as temp_file:
            temp_file.write(EnterNameFile)


SaveFiles(EnterNumber ,  EnterNameFolder , EnterYourPath )


       
    

