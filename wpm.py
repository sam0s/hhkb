from msvcrt import getch
from os import system
from random_sentence import SentenceNow as sn

wordsplit=[]
words=""
thestring="freeze"
def newWord(words,wordsplit):
    wordsplit=[]
    words=sn()
    for f in words:
        wordsplit.append(f)
    system("cls")
    print words
    return words,wordsplit
words,wordsplit=newWord(words,wordsplit)

thestring=""
for f in wordsplit:
    thestring+=str(f)


while True:

    #get key press with getch
    

    if len(thestring) == 0:
        thestring=""
        words,wordsplit=newWord(words,wordsplit)
        for f in wordsplit:
            thestring+=str(f)
    key = chr(ord(getch()))
    #if the key is the one we are looking for, continue onward
    if len(thestring) != 0:
        if key == wordsplit[0]:
            wordsplit=wordsplit[1:]
            thestring=""
            for f in wordsplit:
                thestring+=str(f)
            system("cls")
            print thestring
            print len(thestring)

    
            
