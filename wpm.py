from msvcrt import getch
from os import system
from random_sentence import SentenceNow as sn

#gonna calculate wpm soon

#create random sentence, then split into list
wordsplit=[]
words=sn()
for f in words:
    wordsplit.append(f)

#display words for the first time
print words

#loop
while True:

    #get key press with getch
    key = chr(ord(getch()))

    #if the key is the one we are looking for, continue onward
    if key == wordsplit[0]:
        wordsplit=wordsplit[1:]
        thestring=""
        for f in wordsplit:
            thestring+=str(f)
        system("cls")
        print thestring
