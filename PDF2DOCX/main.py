from pdf2docx import Converter


pdf_path = input("Enter the file name and extension, such as sample.pdf : ")
docx_path = "output.docx"

while True:
    try:
        cv = Converter(pdf_file=pdf_path)
        cv.convert(docx_filename=docx_path)
        cv.close()
        break
    except:
        print("File not found or another error!")
        pdf_path = input("Enter the file name and extension, such as sample.pdf : ")
