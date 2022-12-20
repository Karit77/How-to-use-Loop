Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
vocab = {'cat':'แมว','dog':'หมา'}
vocab[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    vocab[0]
KeyError: 0
vocab['cat']
'แมว'
vocab = {'cat':'แมว','dog':'หมา','pig':['หมู','สุกร']}
print(vocab['pig'])
['หมู', 'สุกร']
print(vocab['pig'][0])
หมู
Emc2['ระเบิด'] = 'รังสี'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Emc2['ระเบิด'] = 'รังสี'
NameError: name 'Emc2' is not defined
vocab['orange'] = 'ส้ม'
print(vocab)
{'cat': 'แมว', 'dog': 'หมา', 'pig': ['หมู', 'สุกร'], 'orange': 'ส้ม'}
print(character)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(character)
NameError: name 'character' is not defined
'''
การเก็บค่าในรูปแบบดิก
'''
'\nการเก็บค่าในรูปแบบดิก\n'
