# task 1
a=input()
a=a.replace(" ","")
b=''
x=0
for i in a[::-1]:
    b+=i
for i in range(len(a)):
    if a[i]!=b[i]:
        x+=1
if x>0:
    print('it`s not palindrome')
else:
    print('it`s palindrome')
# task 2
text=input()
reg=input(f'pls input with{","} or {"_"}:   ')
reg_l=[]
a=''
for i in reg+' ':
    if i== "," or  i==" ":
        reg_l.append(a)
        a=''
    else:
        a+=i
print(reg_l)
for i in reg_l:
    print(i)
    text=text.replace(i, i.upper())
print(text)
# task 3
text=input()
res=0
for i in text:
    if i=='.':
        res+=1
print(res)