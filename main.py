# pip install pymorphy2
import pymorphy2
import PyQt5
import string
import json
import re


morph = pymorphy2.MorphAnalyzer()

word = input()
word = re.split('[^a-zа-яё]+', word, flags=re.IGNORECASE)
print(word)
def tags(word):
    p = morph.parse(word)[0]
    print(p.normal_form)
    print(p.tag.gender)
    print(p.tag)
    #return morph.parse(word)
print(tags(word))

s = input()

lst = s.replace('.', ' ').split()
for word in lst:
    print(tags(word))
