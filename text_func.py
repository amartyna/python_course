line = 'this IS a very STRANGE text'
print('ile razy występuje e: ',line.count('e'))
print('na ktory miejscu e: ', line.find('e'))
print('na ktory miejscu (od prawej) e: ', line.rfind('e'))

print('na ktory miejscu e: ', line.index('e'))
print('na ktory miejscu e: ', line.find('p'))

print('e' in line)

line = """this is long
text and should
be presented in console"""

print(line)
print(line.count('\n'))
print('__________________________________')


import string

print(string.ascii_letters)





