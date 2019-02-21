import os
from os import scandir, getcwd
from os import listdir
import re
def ls(donde,filext = '.png'):
    lstFiles = []
    os.chdir(donde)
    ruta = os.walk("./") 
    for root, dirs, files in ruta:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if(extension == filext):
                if re.match('[H-L]{2}\d',nombreFichero):
                    lstFiles.append(nombreFichero+extension)
    return lstFiles
def lsimg(donde,filext = '.png'):
    lstFiles = []
    os.chdir(donde)
    ruta = os.walk("./") 
    for root, dirs, files in ruta:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if(extension == filext):
                if re.match('^\d',nombreFichero):
                    lstFiles.append(nombreFichero+extension)
    return lstFiles    