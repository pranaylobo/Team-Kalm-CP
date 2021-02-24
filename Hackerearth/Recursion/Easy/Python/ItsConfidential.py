import sys

def middle_char(txt):
    
    if len(txt)>0:

        mid = txt[(len(txt)-1)//2]
        int_mid=txt.index(mid)

        sys.stdout.write(mid)
       
        middle_char(txt[:int_mid])
        middle_char(txt[int_mid+1:])

        

        


# text="abc"
# mid1 = text[(len(text)-1)//2]
# middle_char(text)


x=int(input())

for i in range(0,x):
    x1=int(input())
    middle_char(str(input()))



