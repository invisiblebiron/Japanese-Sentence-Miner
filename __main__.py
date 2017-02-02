# -*- coding: utf-8 -*-
'''
Created on 2017/02/01

@author: Brian
'''
import japaneseTokenizer
import excelExport
import datetime
import time
import pyperclip


if __name__ == '__main__':
    pass

unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y_%m_%d'))
excelFileName = 'MinedStrings_' + date



japaneseString = pyperclip.paste().strip().replace(" ","")



currentList = japaneseTokenizer.breakSentences(japaneseString)

#print(currentList)
excelExport.exportToExcel(excelFileName, currentList)

    


