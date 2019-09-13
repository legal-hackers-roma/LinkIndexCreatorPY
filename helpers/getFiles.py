from os import listdir, path


## Function getPermittedFilesFromPath

def getPermittedFilesFromPath(path_to_dir):
    ## list files in Directory (List Comprehension Python)
    files = [ file for file in listdir(path_to_dir) if path.isfile(path.join(path_to_dir, file)) ]
    
    ### Equivalent to ###
    # files = []
    # for x in listdir(searchPath):
    #    if path.isfile(path.join(searchPath, x)):
    #       files.append(x)

    permittedFiles = []

    for file in files:
        if file.endswith('.pdf') or file.endswith('.jpeg'):
            permittedFiles.append(file)
    
    permittedFiles.sort()
    
    return permittedFiles