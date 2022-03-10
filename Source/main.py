# importing required modules

import tkinter as tk 
from tkinter import filedialog
import xlsxwriter

from init_row_data import init_row_data
from compute_B import compute_B
from compute_A import compute_A

# console interface 

print("Power bills data extractor in txt\nver.: 1.0, 10/03/2022\nAuthor: Fellipe Filgueira")
input("Press ENTER to begin...")
print("\nProcessing...")

# load files paths

root = tk.Tk()
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)
filePath = filedialog.askopenfilename(multiple=False) # True to load multiple files

# creating .xlsx object

findPath = filePath[len(filePath)::-1]
findPath = findPath[findPath.find("/"):]
findPath = findPath[len(findPath)::-1]
workbook = xlsxwriter.Workbook(findPath + 'data.xlsx')
worksheet = workbook.add_worksheet('main')
data_dict = init_row_data()
data_headers = list(data_dict.keys())
for itr in range(len(data_headers)): worksheet.write(0, itr, data_headers[itr])

# leitura do arquivo txt

file = open(filePath, 'r', encoding='utf-8') # gera uma lista com os dados do arquivo txt
file_items = file.readlines()

# set lists 

text = [[]]
data = []

# set loop variables

count = 0
j = 0
row = 1

# convert str into list based in break points

for item in file_items:
    if 'Federal' in item:
        text[count].append(item)
        if item != file_items[-1]:
            text.append(list())
            count += 1
    if item[0:2] == '11' or item[0:2] == '12'or item[0:2] == '13' or item[0:2] == '14' and 'Federal' not in item: 
        text[count].append(item)
    else:
        pass

# algorithm loop

while j < len(text):
    if 'B3' in text[j][1]:
        data = init_row_data()
        data = compute_B(j, text, data)
        for i in range(len(list(data))): worksheet.write(row, i, data[list(data)[i]])
        row += 1
    if 'A4' in text[j][1] or 'A3' in text[j][1]:
        data = init_row_data()
        data = compute_A(j, text, data)
        for i in range(len(list(data))): worksheet.write(row, i, data[list(data)[i]])
        row += 1
    if text[j][1][81:83] not in ['B3', 'A3', 'A4'] : 
        print(text[j][1][26:36] + " bill was not correctly identified")
    else:
        pass
    j += 1
    
# close files

workbook.close()
file.close()

# console interface

print("\ndata.xlsx file has been successfully saved!")
input("Press ENTER to finish...")