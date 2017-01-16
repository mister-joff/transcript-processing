import sys
import glob
import os.path

list_of_files = glob.glob('directoryPath/*.txt')
for file_name in list_of_files:
    print(file_name)

    f= open(file_name, 'r')
    lst = []
    for line in f:
       line.strip()
       line = line.replace('Q: ' ,'*Q:* ')
       line = line.replace('A: ' ,'*A:* ')
       lst.append(line)
    f.close()

    f=open(os.path.join('updated-directoryPath',
    os.path.basename(file_name)) , 'w')

    for line in lst:
       f.write(line)
    f.close()
