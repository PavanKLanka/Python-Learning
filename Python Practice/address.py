book = {}
book['tom'] = {
    'name':'Tom',
    'age':25,
    'phone':564646,
    'address':'New York'
}
book['bob'] = {
    'name':'Tom',
    'age':15,
    'phone':45654,
    'address':'York'
}
import json
s=json.dumps(book)
print(s)
with open('e://data//book.txt','w') as f:
    f.write(s)


