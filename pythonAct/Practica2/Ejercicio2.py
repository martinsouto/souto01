tam = ['im1 4.14', 'im2 13.15', 'im3 6.34', 'im4 410.134']
lis=[]
for i in tam:
    lis1=i.split(' ')
    x=[float(lis1[1])]
    lis.extend(x)
lis.sort()
print(lis)