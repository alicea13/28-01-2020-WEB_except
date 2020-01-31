mydict = {'Yandex': "lyceum", 'class': "B"}
'''if 'class' in mydict:
    print(mydict["class"])'''


try:
    print(mydict["class"])
except KeyError:
    pass


from collections import  defaultdict

s = defaultdict(lambda: 0)
print(s[224])