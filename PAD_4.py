import urllib

'''
import urllib
dir(urllib)
from urllib import request
dir(request)
resp = request.urlopen('http://example.com')
type(resp)
dir(resp)
resp.code - kod
resp.length - rozmiar
resp.peek() - kawałek
data = resp.read() - całość
type(data)
len(data) - rozmiar
html = data.decode('UTF-8') - dekodowanie
type(html)

Once you read response python close the connection

# https://www.youtube.com/watch?v=LosIGgon_KM

from urllib import parse
dir(parse)

params = {'v': 'LosIGgon_KM'}
querystring = parse.urlencode(params)

url = 'https://www.youtube.com/watch' + '?' + querystring
resp = request.urlopen(url)
resp.isclosed() - czy zamknięte
resp.code
html = resp.read().decode('utf-8')
html[:500]
'''

import json

'''
json_file = open('path', 'r', encoding='utf-8')
file = json.loads(json_file)
json_file.close()

value = {'json': 'json'}
tron = json.loads(value) - converts to dict

json.dumps(tron, ensure_ascii=False) - to string i żeby nie wróciło kodowanie

---------------
--- create dict:

movie2 = {}
movie2['title'] = 'Minority Report'
movie2['director'] = 'Sztiwen Szpilberg'

Write it to the file:

file2 = open('path', 'w', encoding='utf-8')
json.dump(movie2, file2, ensure_ascii=False)
file2.close()

'''

# FILES

f = open('path')

''' to read the contents '''
text = f.read()
f.close()

print(text)

''' BETTER APPROACH  dont need to close and handle exeption'''
try:   
    with open('path\to\file.txt') as fobj:
        read = fobj.read()
except FileNotFoundError:
    text = None

''' Write to file:  (w will override existing)'''

oceans = ['Pacific', 'Atlantic', 'Indian']

with open('oceans.txt', 'w') as f:
    for ocean in oceans:
        f.write(ocean)
        f.write('\n')

    # lub:

    for ocean in oceans:
        print(ocean, file=f)

''' For Not overriding a file '''

with open('oceans.txt', 'a') as f:
    print(23*'=', file=f)
    print('These are 5 oceans', file=f)



