import hashlib
import os

path='fileList.txt'
file_list = open(path,'w')

lists_files_old = []
lists_files_new = []

lists_files_new = os.listdir('new/')
lists_files_old = os.listdir('old/')

for filename in lists_files_new:
    for filecompare in lists_files_old:
        if filecompare == filename:
            hasher = hashlib.md5()
            with open('new/'+filename, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
                a = hasher.hexdigest()
                #print filename
                #print a

            hasher = hashlib.md5()
            with open('old/'+filecompare, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
                b = hasher.hexdigest()
                #print filecompare
                #print b

            if a != b:
                file_list.write(filecompare+'\n')
    

file_list.close()
