from pathlib import Path


def readfilandfolder():
         path = Path('D:\\aiml red and white')
         items = list(path.rglob('*'))
         for i, item in enumerate(items):
                 print(f"{i+1} :{item}")

def createfileandfolder():
        try:
            readfilandfolder()
            filename = input("enter the file name you want to create")
            p=Path(filename)
            if not p.exists:
                with open(p,"w") as fs:
                    data=input("what you want to write in this file:")
                    fs.write(data)
                    print(f"File is create sucessfully")

            else:
                    print("this file is alrady exists")
        except Exception as err:
          print(f"an error occured as {err}")
                 

def updatefile():
        try:
                readfilandfolder()
                name = input("tell which you want to update")
                p = Path(name)
                if p.exists and p.is_file():
                        print("press 1 for change name of file")
                        print("press 2 for over write data of your file ")
                        print("press 3 for appending some content in file")
                        res = int(input("tell your response:-"))

                if res == 1:
                        name2= input("tell your new file name:-")
                        p2=Path(name2)
                        p.rename(p2)
                if res==2:
                        with open(p,'a') as fs:
                                data =input("enter your content which add in your file ")
                                fs.write(" "+data)

        except Exception as err:
               print(f"some error is occured in this {err} ")

def deletefile():
        readfilandfolder()
        name=input("which file you can delete")
        p=Path(name)

        if p.exists() and p.is_file():
                p.unlink()
                print("file is deleted sucessfully")
        else:
               print("this file is not exists")
               

print("enter 1 for read")
print("enter 2 for create")
print("enter 3 for update")
print("enter 4 for deletion")
userinput = int(input(":-"))

if userinput == 1:
        readfilandfolder()

if userinput == 2:
         createfileandfolder()


if userinput == 3:
         updatefile()

if userinput == 4:
       deletefile()