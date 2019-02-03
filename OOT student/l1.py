list1 = ["a","b","c","d","e","f","g","h","i"]
list2 = []
f = open('file1.txt','w')
for i in list1:
    f.write(i)
    f.write("\n") 


f.close()

f = open('file2.txt','r')
for i in list1:
    a = f.readline()
    list2.append(a)


for i in list1:
    print i
