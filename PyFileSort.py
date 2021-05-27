import os
import shutil

filetypes = []


def mainmenu():
    print("\n" + "------Downloads Organizer------")
    inputdir = input("Please type directory: ")
    if os.path.exists(inputdir):
        os.chdir(inputdir)
        global cwd
        cwd = os.getcwd()
        scanfiles()
        makefolders()
        movingfiles()
        print("\n"+ "Organizing " + cwd)
        print("\n" + "Directory organized!")
        quit()
    else:
        print("\n" + "Error: Invalid Directory!" + "\n")
        mainmenu()


# Scans files and appends filetype to a list
def scanfiles():
    with os.scandir(cwd) as entries:
        for entry in entries:
            if entry.is_file():
                entry = entry.name
                f = entry.split('.')
                if f[0] != "":
                    filetypes.append(f[1])


# Scans directory and makes folders for each file extension in filetypes list if folder doesn't exist
def makefolders():
    for ftype in filetypes:
        if not os.path.exists(ftype):
            os.makedirs(ftype)


# Scans all files with at least one character before filetype and moves them to matching folder
def movingfiles():
    with os.scandir(cwd) as fentries:
        for fentry in fentries:
            if fentry.is_file():
                fentry = fentry.name
                x = fentry.split('.')
                if x[0] != "":
                    shutil.move(fentry, os.path.join(cwd, x[1]))


mainmenu()
