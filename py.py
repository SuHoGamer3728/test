fin = open('D:/code/fin.inp/','r',encoding='utf-8')
fout = open('D:/code/fout.out/','w',encoding='utf-8')

n = int(fin.readline())
a = list(fin.read().split())

a.sort()
c = []
b = []
for i in a:
    c.append(i)
for i in range(1,n):
    if a[i-1] == a[i]:
        c.remove(a[i])
for i in c:
    fout.write(f'{i}'' ')
fout.close()