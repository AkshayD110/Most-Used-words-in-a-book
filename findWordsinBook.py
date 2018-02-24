import numpy
import collections
import PyPDF2
import re

def wordsFromPDFfile(path):
    pdffileObj = open(path, 'rb')
    listOfWords = []
    totalWord = 0
    pdfreader = PyPDF2.PdfFileReader(pdffileObj)
    numOfPages = pdfreader.getNumPages()
    pages = 1
    print("Pages:",numOfPages)
    """try using numpy for list operations below"""
    for pages in range(pages,numOfPages):
        pdfObject = pdfreader.getPage(pages)
        wordsInPage = re.findall(r'\w+',pdfObject.extractText())
        for words in wordsInPage:
            listOfWords.append(words.lower())
        totalWord += int(len(wordsInPage))
    #print(pdfObject.extractText())
    #numpyArray = numpy.array(listOfWords)
    #words = re.findall(r'\w+', pdfObject.extractText())
    print("words:", totalWord)
    print(collections.Counter(listOfWords).most_common(10))

def wordsFromTextFile(path):
    words = re.findall(r'\w+', open(path).read().lower())
    print(type(words))
    print("words",len(words))
    print(collections.Counter(words).most_common(10))


wordsFromPDFfile(r"C:\Users\akshdesh.ORADEV\Documents\books\python\fluent-python-2015-.pdf")
#wordsFromTextFile(r"C:\Users\akshdesh.ORADEV\Documents\books\python\newFile.txt")
wordsFromTextFile(r"D:\findWords.txt")

