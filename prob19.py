with open('document1.txt','r') as f:
    a=list(eval(f.readline()))
print(a)
with open('document2.txt','w') as f:
    print(a.count('a'))
    print(a.count('b'))
    print(a.count('oa'))