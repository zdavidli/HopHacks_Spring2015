 
'''
Created on Jan 26, 2015
'''

import os, time, datetime

#data
WhiteList_zip = []
WhiteList_del = []
BlackList = []

ZIP_AGE = 120
DEl_AGE = 300

ZipFileEndings = []
DelFileEndings = []

RunInterval = 600

__RUN = True

loadData()
for each entry in WhiteList_delete:
    DelDir(entry)
for each entry in WhiteList_zip:
    ZipDir(entry)

def DelDir(curDir):

    for each file in curDir: #NEED SOME WAY OF ITERATING HERE
        if (shouldDel(file)):
            #delete the file

    for each dir in curDir: #NEED ANOTHER WAY OF ITERATING HERE
    	if (WhiteList_del.contains(dir)):
    		WhiteList_del.remove(dir)

        if (!BlackList.contains(dir) and !WhiteList_zip.contains(dir)):
            DelDir(dir)

#similar method for ZipDir
def ZipDir(curDir):


#checks if the file should be deleted, default is True
#False if: not a recognized file ending, or on a list other than WhiteList_Del
def shouldDel(file):
    curTime = datetime.datetime.now()
    accessTime = os.stat(file).st_atime
    if (curTime - accessTime < DEL_AGE):
        return False

    if ((file in BlackList) or (file in WhiteList_Zip.contains)):
        return False

def shouldZip(file):


def loadData():
    #load each global var from disk
