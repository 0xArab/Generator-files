import os , glob



""" // Create a file in the specified path """
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


# 
# 
Paths = []
def SaveFolder(Number_folders , Name_folders , Path): 
    global Paths
    for getNumber in range(1 , Number_folders + 1 ):
        StringFormat = f"{getNumber}-{Name_folders}"
        Paths.append(os.path.join(Path, StringFormat))
        path = os.path.join(Path, StringFormat)
        os.mkdir(path)
    return Paths

def getDirctory():
    for getPath in range(len(Paths)):
        filename = str(getPath) + "." + str(Name_folder) + ".txt" 
        with open(os.path.join(Paths[getPath] , filename), 'a+') as temp_file:
             temp_file.write(Name_folder)
            

SaveFolders(Number_folder , Name_folder , Name_path)
getDirctory()
def main():
    print('''
      - 1 CreateFiles ? 
      - 2 CreateFolders & Files ?
    ''')
    Number = int(input(" -: "))
    if Number == 1 :
        EnterNumber = int(input("Enter Passe Number : "))
        EnterYourPath =  str(input(" Enter Your Path : "))
        EnterNameFolder = str(input(" Folder Name : "))
        EnterNameFile= str(input(" Enter Your File Name : "))
        EnterTypeFile = str(input(" Enter Type File : "))
    else:
        Number_folder = int(input("please Enter number Folder : "))
        Number_Files = int(input("please Enter number Files : "))
        Name_folder = str(input("Enter name folder : "))
        Name_path = str(input("Enter name path : "))
        
if __name__ == '__main__':
   main()
SaveFiles(EnterNumber ,  EnterNameFolder , EnterYourPath )


       
    

