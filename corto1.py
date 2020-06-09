def par (num):  #de el valor
    if num%2 ==0:
        num = int(num/2)
    else:
        num= int((num*3)+1)
    return num

conteo =0
while contero != 1:
    for i in range (2, 161):
    print(par(i))
        
