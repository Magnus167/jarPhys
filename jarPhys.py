import PyPDF2, os
import docx

   # Get all the PDF filenames.
readFileNamePDF = 'jarPhysReadFile.pdf'
readFileNameDOC = 'jarPhysReadFile.docx'

def createCombinedFileDOC(rfName=readFileNameDOC):
    docFiles = []
    for filename in os.listdir('.'):
        if filename.endswith('.doc') or filename.endswith('.docx'):
            docFiles.append(filename)
    for filename in docFiles:
        doc = docx.Document(filename)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
    

def createCombinedFilePDF(rfName=readFileName):
    pdfFiles = []   
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            pdfFiles.append(filename)
    pdfFiles.sort(key=str.lower)
    pdfWriter = PyPDF2.PdfFileWriter()
    for filename in pdfFiles:
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            for pageNum in range(0, pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
    pdfOutput = open(rfName ,'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()


"""
searchFile -- >
    pdfFileObj = open(readFileNamePDF, 'rb')
    searchText = []
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for pageNum in range(0, pdfReader.numPages)
            searachText.append(pageObj.extractText(pageNum))

    strip numbers
    create sentences
    create paragraphs
    search within sentence = stcScore
    search within para = paraScore
    create similarity tree using stcScore, paraScore

    return pageNumbers, docName, match text, paraScore, stcScore

"""