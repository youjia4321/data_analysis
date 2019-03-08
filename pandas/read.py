#! /usr/bin/env python
#coding=utf-8
# -*- coding:utf-8 -*-
import xlrd

def main():
    xlsFile = xlrd.open_workbook("/home/xjm/Desktop/projects/DataAnalysis/1.xls")
    sheets = xlsFile.sheet_names()
    print("xls has %d sheets" % xlsFile.nsheets)
    for sheetName in sheets:
        printSheet(xlsFile, sheetName)
    
def printSheet(oXls, sheetName):
    sheetIsEmpty = True
    tmpSheet = oXls.sheet_by_name(sheetName)
    tmpLine = ""

    for row in range(tmpSheet.nrows):
        for col in range(tmpSheet.ncols):
            if tmpSheet.cell(row, col).value != None:
                sheetIsEmpty = False
                try:
                    tmpLine += str(tmpSheet.cell(row, col).value) + "\t"
                except:
                    tmpLine += tmpSheet.cell(row, col).value + "\t"
        tmpLine += "\n"

    if sheetIsEmpty == False:
        print('sheet name:%s' % sheetName)
        print(tmpLine)

if __name__ == "__main__":
    main()
