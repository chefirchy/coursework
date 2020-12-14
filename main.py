# pip install pymorphy2
import pymorphy2
import string

morph = pymorphy2.MorphAnalyzer()

word = "женская"
def tags(word):
    p = morph.parse(word)[0]
    print(p.normal_form)
    print(p.tag.gender)
    print(p.tag)
    return morph.parse(word)
print(tags(word))
