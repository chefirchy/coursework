import pymorphy2
import string
morph = pymorphy2.MorphAnalyzer()

word = "стали"
p = morph.parse(word)[0]
print(p.normal_form)