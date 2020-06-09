
lista=[]
carnet=161

for i in range (2,carnet):
    while i !=1:

        if i%2 ==0:
            lista.append(i)
            i=int(i/2)
        else:
            lista.append(i)
            i=int (i*3+1)
print(lista)
archivo=open('collatz.txt','a')
archivo.write('lista')
archivo.close()