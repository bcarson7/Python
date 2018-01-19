import csv, os

csvRows = []
csvFileObj = open('test.csv')
readerObj = csv.reader(csvFileObj)
for row in readerObj:
    if readerObj.line_num == 1:
        continue  #skip first row
    csvRows.append(row)
csvFileObj.close()

csvFileObj = open(os.path.join('test.csv'), 'w', newline='')
csvWriter = csv.writer(csvFileObj)
for row in csvRows:
    csvWriter.writerow(row)
csvFileObj.close()
