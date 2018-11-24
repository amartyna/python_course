# Pętla_1

i = 1
imax = 10

while i <= imax :
    print(i , 'I like Python')
    i+=1
else:
    print('Now i =',i)
    print('------------------------')

# Pętla_2
# Zanjdź trzy kolejne rosnące liczby

values = [10,24,43,12,48,12,11,98,28,19,27,49,74,22]
i = 0
max = len(values) - 2

while i < max :
    print(i,':', values[i], values[i+1], values[i+2])

    if values[i] < values[i+1] and values[i+1] < values[i+2]:
        print('\tFound: ', values[i], values[i+1], values[i+2])
    
    i+=1







    
