# For

persons = ['Ola','Ania','Bobek','Bożenka','Andrzej']
domain = 'mycompany.com'

for person in persons:
    email = person + '@' + domain
    print('Email for\t', person, 'is\t', email)
else:
    print('--- end of the list ---')

# Nested for

for x in range(1,6):
    line = str(x)
    for y in range(1,6):
        line += ('\t%2d' % (x*y))
    print(line)
        
