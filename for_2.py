# For

for number in range(1,21):
    if number %2 == 0:
        print('Number %2d is %s' % (number,'even'))
    else:
        print('Number %2d is %s' % (number,'odd'))

###############
        
for candidate in range(2,31):

    for divider in range(2,candidate):
        if candidate % divider == 0:
            print('%2d is not a prime number - divider is %2d' % (candidate,divider))
            break
    else:
        print('%2d is prime!' % (candidate))

