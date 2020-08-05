import os
def returnDir():
    dirs =['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
    for recyDir in dirs:
        if os.path.isdir(recyDir):
            return recyDir
    return None

print(returnDir())