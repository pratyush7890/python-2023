s= "Hello class"
vowels='A E I O U a e i o u'
vc=0
cc=0
for i in s:
    if i in vowels:
        vc+=1
    else:
        cc+=1
print(vc)
print(cc)

