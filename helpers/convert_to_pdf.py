# import xhtml2pdf
#from xhtml2pdf import pisa
from weasyprint import HTML


def convert_to_pdf(htmlSource, output):
    # open output file
    # resultFile = open(output, 'w+b')

    # convert to PDF
    # res = pisa.CreatePDF(
    #    htmlSource,
    #    dest=resultFile
    #)

    # resultFile.close()

    HTML(string=htmlSource).write_pdf(output)
    
