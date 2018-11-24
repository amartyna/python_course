# Zadanie kwadraty liczb

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i = 0
max = len(numbers) - 1

while i < max :
    print(i,':',numbers[i], numbers[i+1])

    if numbers[i]*numbers[i] == numbers[i+1]:
        print('\tFOUND: ', numbers[i], '=', numbers[i+1])
    
    i+=1
