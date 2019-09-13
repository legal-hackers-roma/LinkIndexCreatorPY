import sys
from os import listdir, path

### function checkArgv ###
# check if a valid path is passed as argument 
# check if name of attorney is provided 
def checkArgv():
    searchPath = sys.argv[1] if len(sys.argv) >= 2 else None
    attorney = sys.argv[2] if len(sys.argv) >= 3 else None

    if not searchPath:
        print('Devi indicare il percorso di una cartella dove sono contenuti gli allegati')
        quit()

    if not attorney:
        print('Devi indicare il nome e cognome di un avvocato')
        quit()

    if not path.exists(searchPath):
        print('La cartella non esiste')
        quit()
    else:
        print('La cartella esiste')

    return (searchPath, attorney)

    

    
