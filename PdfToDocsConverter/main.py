from pdf2docx import Converter

pdfFile = "sample.pdf"
docxFile = "sample.docx"

cv = Converter(pdfFile)
cv.convert(docxFile)
cv.close()