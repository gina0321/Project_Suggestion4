#!/usr/bin/env python3

"""
Project Suggestion 4:

Filter sequences
Write a python program with which you are able to filter sequences from any sequence file based on an input list of sequence IDs. Consider that header lines can be complex and long, because they sometimes contain more information than just their sequence IDs. Include an option in your program to alphabetically order your Gene IDs. When choosing this project, we can provide you with a database and input list.

For this project the provided database and input list were used. 
To run the program your terminal should therefor look like this: python GinaF_Suggestion4_Code.py Project4_IDlist.txt Project4_database.fasta
You will then get asked, if you want your outputfile at the end to be sorted or not.
Type "NO" and the outputfile will have the same order as the ID list.
Type "YES" and the outputfile will be alphabetically ordered (first uppercase letters A...Z, then lowercase letters a...z)
You will be shown how many IDs were in the input list and how many of them could be found and therefor are in the outputlist.
With the provided data you should have 22 elements as input and all of them can be found in the output file.
Last but not least you will receive the output.txt file containing the filtered sequences.

"""

import re
#read input from command line
import sys
IDlist_file = sys.argv[1]
database_file = sys.argv[2]

#read the sequence IDs from the txt file
ID = open(IDlist_file, "r")
ID_content=ID.read()
ID_list = ID_content.split("\n")
ID_count=len(ID_list) #as a check whether all IDs from input were found
ID_count2=0

#read the database from the fasta file
data = open(database_file, "r")
data_content=data.readlines()
di = {}
seq_ID="" #key
seq="" #value

#Ask the user if the Gene IDs should be alphabetically ordered
ordered = input("Do you want the Gene IDs to be ordered? Please type YES or NO.")
while ordered.upper() != "YES" and ordered.upper() != "NO":
    ordered = input("Please type YES or NO.")

# save sequence ID as key and sequence as value in dictionary
for line in data_content: 
    if line.startswith(">"):
        chunk= line.split(" ")
        seq_ID=chunk[0].replace("\n", "").replace(">", "")
        
    else:
        seq=seq + line.strip()
    if seq != "":
        di[seq_ID]=seq
        seq=""
        
data.close()
file = open("output.txt", "w")
#if not orderd
if ordered.upper() == "NO":
    #find IDs from IDlist in dictionary and write IDs with corresponding sequence in a file
    for line in ID_list:
        for key in di:
            if key == line:
                file.write(">" + key + "\n" + di[key] + "\n")
                ID_count2 = ID_count2 + 1 
            else:
                continue
                
#if ordered
else:
    #first sort id_list
    ID_list.sort()
    #same as above
    for line in ID_list:
        for key in di:
            if key == line:
                file.write(">" + key + "\n" + di[key] + "\n")
                ID_count2 = ID_count2 + 1
                
            else:
                continue
file.close()
#to remove any empty line at the end of the outputfile
file = open("output.txt", "r")
lastline= file.readlines()
#print(lastline)
file.close()
file = open("output.txt", "w")
lastline[-1]=lastline[-1].replace("\n", "")

for item in lastline:
    file.write(item)


#output section
print("There are " + str(ID_count) + " elements as Input.")#prints how many IDs as input
print("There are " + str(ID_count2) + " elements as Output.")#prints how many IDs are in output

file.close()  
ID.close()


