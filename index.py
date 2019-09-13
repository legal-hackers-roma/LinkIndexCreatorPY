import sys
from os import path
import mammoth

from helpers.checkArgv import checkArgv
from helpers.getFiles import getPermittedFilesFromPath
from helpers.createLinksArray import createLinksArray
from helpers.createIndexTemplate import createIndexTemplate
from helpers.convert_to_pdf import convert_to_pdf
from helpers.createDocxIndex import createDocxIndex

# save arguments into tuple
args = checkArgv()
folder = args[0]
attorney = args[1]

# get Permitted files from folder's path (args[0])
files = getPermittedFilesFromPath(folder)

# creates links array
linksArray = createLinksArray(files)

# creates html index
html = createIndexTemplate(linksArray, attorney, folder)

# converts html to pdf (TO BE TESTED)
convert_to_pdf(html, path.join(folder, '00_indice_atti_documenti.pdf'))


