pymongodb
![](https://img.shields.io/badge/python%20-%203.7-brightgreen.svg)
========
> python mongodb api 

## `Install`
` pip install git+https://github.com/zhouxianggen/pymongodb.git`

## `Upgrade`
` pip install --upgrade git+https://github.com/zhouxianggen/pymongodb.git`

## `Uninstall`
` pip uninstall pymongodb`

## `Basic Usage`
```python
from pymongodb import PyMongoDb

m = PyMongoDb(host='localhost', port=27017, user='admin', db='crawler')
collection, objectid = m.save({'foo': 'bar'})
print(m.get(collection, objectid))
```
