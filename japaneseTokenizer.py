'''
Created on 2017/02/01

@author: Brian
'''

def breakSentences(japaneseString):
    stringIndex = 0
    newString = ''
    stringList = []
    deleteChar = ['「','」',' ','\t']
    
    for char in deleteChar:
        if char in japaneseString:
            japaneseString = japaneseString.replace(char, '')
    
    while stringIndex < len(japaneseString):
        if japaneseString[stringIndex] not in '。？！':
            newString += japaneseString[stringIndex] 
            stringIndex += 1
        else:
            newString += japaneseString[stringIndex]
            stringList.append(newString)
            newString = ''
            stringIndex += 1
    
    return stringList