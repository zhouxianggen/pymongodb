# coding: utf8 
from pymongodb import PyMongoDb

m = PyMongoDb(host='192.168.9.226', port=27017, user='admin', pswd='', 
        db='crawler')

#r = m.save({'foo': 'bar'})
#print(r)

print(m.get('col_20190211', '5c614876b446fe075cebf4f1'))
