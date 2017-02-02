'''
Created on 2017/02/01

@author: Brian
'''
import openpyxl
import os

def exportToExcel(fileName, stringList):
    os.chdir('D:\\PythonScripts\\Japanese Sentence Miner')
    workbook = openpyxl.Workbook()
    #workbook = openpyxl.load_workbook(fileName + '.xlsx')
    sheet = workbook.get_sheet_by_name('Sheet')
    
    #rowNumber = 1
    
    for rowNumber, sentence in enumerate(stringList):
        try:
            if sheet['A' + str(rowNumber + 1)].value != None:
                print('Contains string...')
                continue
        except TypeError:
            sheet['A' + str(rowNumber + 1)] = sentence
        
    workbook.save(fileName + '.xlsx')