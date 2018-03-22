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
    print("==========processing==========")
    #print("Pages:",numOfPages)
    """try using numpy for list operations below"""
    for pages in range(pages,numOfPages):
        pdfObject = pdfreader.getPage(pages)
        wordsInPage = re.findall(r'\w+',pdfObject.extractText())
        for words in wordsInPage:
            listOfWords.append(words.lower())
        totalWord += int(len(wordsInPage))
    #print("words:", totalWord)
    commanWords=(collections.Counter(listOfWords).most_common(10))
    timeToReadBookInminutes=divmod(totalWord,200)
    finalTime=divmod(timeToReadBookInminutes[0],60)

    print(f"The book has - \n {numOfPages} : no. of pages, \n {totalWord} : no. of words, \n The most common words in "
          f"the book are : \n {commanWords}")
    print(f"As per the average read speed of a person(200words/min), it would take {finalTime[0]}hours, {finalTime[1]} minutes to complete this book")



def wordsFromTextFile(path):
    words = re.findall(r'\w+', open(path).read().lower())
    print("The book has these many words ",len(words))
    print(collections.Counter(words).most_common(10))



wordsFromPDFfile(r"C:\Users\akshdesh.ORADEV\Documents\books\python\fluent-python-2015-.pdf")
#wordsFromTextFile(r"C:\Users\akshdesh.ORADEV\Documents\books\python\newFile.txt")
#wordsFromTextFile(r"D:\findWords.txt")

"Improvements -" \
"> find the percentage of the occurance of the comman word"