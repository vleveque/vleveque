# Python script to split monthly WSPR files by band for subsequent al=nalysis by R

from csv import reader
WSPRout07 = open('C:\\Users\\vleveque\\Downloads\\wsprspots-2022-02_07.csv','w') 
  WSPRout07wtr = csv.writer(WSPRout07)
WSPRout10 = open('C:\\Users\\vleveque\\Downloads\\wsprspots-2022-02_10.csv','w')
  WSPRout10wtr = csv.writer(WSPRout10)
WSPRout14 = open('C:\\Users\\vleveque\\Downloads\\wsprspots-2022-02_14.csv','w')
  WSPRout14wtr = csv.writer(WSPRout14)
WSPRout21 = open('C:\\Users\\vleveque\\Downloads\\wsprspots-2022-02_21.csv','w')
  WSPRout21wtr = csv.writer(WSPRout21)
WSPRout28 = open('C:\\Users\\vleveque\\Downloads\\wsprspots-2022-02_28.csv','w')
  WSPRout28wtr = csv.writer(WSPRout28)
#
with open('C:\\Users\\vleveque\\Downloads\\wsprspots-2022-02.csv','r') as WSPRfile:
    WSPRcsv = reader(WSPRfile)
    for row in WSPRcsv:
     band = row[12]
     if band == 7:
       WSPRout07wtr.writerow(row)
     if band == 10:
       WSPRout10wtr.writerow(row)
     if band == 14:
       WSPRout14wtr.writerow(row)
     if band == 21:
       WSPRout21wtr.writerow(row)
     if band == 28:
       WSPRout28wtr.writerow(row)