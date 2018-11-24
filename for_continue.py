fruits = ['apple', 'banana', 'cherry', 'app@le.pl', 'ban!na', 'ch@rry']

domain = 'myfruits.com'

emails = []

'''
for fruit in fruits:

    if '@' in fruit:
        emails.append(fruit)
    else:
        email = fruit+'@'+domain
        emails.append(email)
'''

for fruit in fruits:

    if '@' in fruit:
        emails.append(fruit)
        continue

    email = fruit+'@'+domain
    emails.append(email)


for email in emails:
    print(email)


