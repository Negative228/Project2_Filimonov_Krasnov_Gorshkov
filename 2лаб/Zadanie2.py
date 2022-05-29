import random
import os
import pickle
from shutil import copyfile

#3
n1 = int(input("n1 = "))
n2 = int(input("n2 = "))
m = int(input("m = "))

with open("txt.txt",'w+') as f:
    for i in range(random.randint(n1,n2)):
        f.write(str(random.randint(-m,m)) + " ")

#17
try:        
    os.rename("txt.txt","abc.txt")
except FileExistsError:
    print("Файл abc уже существует")

#22
with open("abc.txt",'r') as f:
    arr = list(map(int,f.readline().split()))
    
with open("newtxt.txt",'w+') as f:
    temp = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > 0:
            if arr[i-1]>0:
                temp+=arr[i]
            else:
                f.write(str(temp) + " ")
                temp = arr[i]
        elif arr[i] < 0:
            if arr[i-1]<0:
                temp+=arr[i]
            else:
                f.write(str(temp) + " ")
                temp = arr[i]
        else:
            if arr[i-1]!=0:
                f.write(str(temp) + " ")
                temp = arr[i]
    f.write(str(temp))
            
#24
copyfile("newtxt.txt","newtxt2.txt")

with open("newtxt2.txt",'r') as f:
    arr24 = list(map(int,f.readline().split()))

max_ = max(arr24)
min_ = min(arr24)
maxi = arr24.index(max_)
mini = arr24.index(min_)

arr24[maxi], arr24[mini] =arr24[mini], arr24[maxi]

with open("newtxt2.txt",'w+') as f:
    for i in arr24:
        f.write(str(i)+ " ")

#34
with open("newpickle.pkl",'wb') as f:
    newset = {random.randint(1,33) for i in range(random.randint(1,33))}
    pickle.dump(newset,f)
with open("newpickle.pkl",'rb') as f:
    picklearr = pickle.load(f)
print(picklearr)
