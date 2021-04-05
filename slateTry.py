import slate3k as slate
readFileNamePDF = 'jarPhysReadFile.pdf'
with open(readFileNamePDF,'rb') as f:
    extracted_text = slate.PDF(f)
    f.close()

for x in range(0,len(extracted_text)):
    print(x)