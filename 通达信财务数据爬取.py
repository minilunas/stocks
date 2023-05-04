import pandas as pd
import re
import os
from pytdx.reader import HistoryFinancialReader

def getName(fname):
    # Define the regular expression pattern to match the date
    pattern = r'cw(\d+)\.zip'

    # Search for the pattern in the source file name
    match = re.search(pattern, fname)

    # Extract the date from the match object
    dateStr = match.group(1)
    return dateStr


def fin2csv_data(dirname,fname,targetDir):

    # Continue with the rest of the code to read the data and write it to the csv file
    readData = HistoryFinancialReader().get_df(dirname+os.sep+fname)
    if readData is not None:
        fname = getName(fname)   
        if fname.startswith('20'):
            # print(dirname+os.sep+fname)
            # Use the date as the file name for the output csv file
            
            ifile=open(targetDir+fname+'.csv','w')

            # print(readData)
            # Use pandas to write the readData to a csv file
            readData.to_csv(targetDir+fname+'.csv')
    




pathdir='D:\\new_tdx\\vipdoc\\cw'
targetDir='d:\\python\\解析通达信数据\\财务数据\\'
# Use os.path.join to join the pathdir and the file name
# Use os.path.splitext to split the file name and extension
# Check if the extension is .zip using an if statement
# Only call fin2csv_data if the extension is .zip

for f in os.listdir(pathdir):
    if os.path.splitext(f)[1] == '.zip':
        fin2csv_data(pathdir,f, targetDir)
else:
    print ('The for '+pathdir+' to '+targetDir+'  loop is over')
