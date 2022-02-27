import os
import shutil
import glob

def ext_convert(fname, basename):
    newfilename=os.path.basename(basename)
    if os.path.splitext(fname)[1] == ".drl":
        shutil.copy(fname, basename+"\\"+newfilename+".TXT")
    elif os.path.splitext(fname)[1] == ".gbl":
        shutil.copy(fname, basename+"\\"+newfilename+".GBL")
    elif os.path.splitext(fname)[1] == ".gbs":
        shutil.copy(fname, basename+"\\"+newfilename+".GBS")
    elif os.path.splitext(fname)[1] == ".gbp":
        shutil.copy(fname, basename+"\\"+newfilename+".GBP")
    elif os.path.splitext(fname)[1] == ".gbo":
        shutil.copy(fname, basename+"\\"+newfilename+".GBO")
    elif os.path.splitext(fname)[1] == ".gtl":
        shutil.copy(fname, basename+"\\"+newfilename+".GTL")
    elif os.path.splitext(fname)[1] == ".gts":
        shutil.copy(fname, basename+"\\"+newfilename+".GTS")
    elif os.path.splitext(fname)[1] == ".gtp":
        shutil.copy(fname, basename+"\\"+newfilename+".GTP")
    elif os.path.splitext(fname)[1] == ".gto":
        shutil.copy(fname, basename+"\\"+newfilename+".GTO")
    elif os.path.splitext(fname)[1] == ".gm1":
        shutil.copy(fname, basename+"\\"+newfilename+".GML")

if __name__ == "__main__":
    target = input("Garbar data directory:")
    x = glob.glob(target+"\\*.*")
    if len(x) == 0:
        print("No garbar data")
        exit(1)
    name = os.path.commonprefix(x)
    if not os.path.exists(name):
        os.makedirs(name)

    for fname in x:
        ext_convert(fname, name)

        

    


