Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
L=['a', 'b', 'c', 'd']
L[1]
'b'
L[4]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    L[4]
IndexError: list index out of range
L[1]=L[0]
L[0]
'a'
L[1]
'a'
L[4]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    L[4]
IndexError: list index out of range
D= {'a': 123, 7:'bob', (7.8, 45): [], 1.2. {XXX. : }}
SyntaxError: ':' expected after dictionary key
D= {'a': 123, 7:'bob', (7.8, 45): [], 1.2:{XXX. : }}
SyntaxError: invalid syntax
D= {'a': 123, 7:'bob', (7.8, 45): [], 1.2: {XXX. '?' }}
SyntaxError: invalid syntax
D= {'a': 123, 7:'bob', (7.8, 45): [], 1.2: {'XXX': '?' }}
D[7]
'bob'
del D[7]
D
{'a': 123, (7.8, 45): [], 1.2: {'XXX': '?'}}
D['a'] = 567
D
{'a': 567, (7.8, 45): [], 1.2: {'XXX': '?'}}
s = 'hello'
s = 'boh?'
s
'boh?'
D1 = dict()
D1
{}
D
{'a': 567, (7.8, 45): [], 1.2: {'XXX': '?'}}
D['b'] = 7989
D
{'a': 567, (7.8, 45): [], 1.2: {'XXX': '?'}, 'b': 7989}
len[D]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    len[D]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> len(D)
4
>>> 'a' in D
True
>>> D['ccc']
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    D['ccc']
KeyError: 'ccc'
>>> L
['a', 'a', 'c', 'd']
>>> L[8]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    L[8]
IndexError: list index out of range
>>> D.get('ccc')
>>> bob = D.get('ccc')
>>> bob
>>> type(bob)
<class 'NoneType'>
>>> bob = D.get('a', 'not present')
>>> bob
567
>>> D
{'a': 567, (7.8, 45): [], 1.2: {'XXX': '?'}, 'b': 7989}
>>> D,popitem()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    D,popitem()
NameError: name 'popitem' is not defined
>>> D.popitem()
('b', 7989)
>>> D
{'a': 567, (7.8, 45): [], 1.2: {'XXX': '?'}}
>>> D.popitem()
(1.2, {'XXX': '?'})
>>> D.pop('a')
567
>>> D
{(7.8, 45): []}
>>> D[(7.8, 45)].append(12)
