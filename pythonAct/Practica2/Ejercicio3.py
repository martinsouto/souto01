tam=['Auto', '123', 'Viaje', '50', '120']
lis=[]
for i in tam:
    if i.isdecimal():
        x=[int(i)]
        lis=lis+x
lis.sort()
for i in range(len(lis)):
    lis[i]=str(lis[i])
print(lis)