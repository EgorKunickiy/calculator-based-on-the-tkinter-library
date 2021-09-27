import math
def Del_ins(c,res,b):
    pom=c-1
    for i in range(c+1,c-2,-1):
        del b[i]
    b.insert(pom,res)

def Ans(ch,b):
    c=b.index(ch)
    if ch=='^':
        res=b[c-1]**b[c+1]
    elif ch=='*':
        res=b[c-1]*b[c+1]
    elif ch=='/':
        res=b[c-1]/b[c+1]
    elif ch=='+':
        res=b[c-1]+b[c+1]
    else:
        res=b[c-1]-b[c+1]
    Del_ins(c,res,b)

def Calculations(a):
    b=[]
    for i in a:
        if i in('+','-','*','/','^'):
            b.append(i)
        else :
            if '.' in i:
                c=float(i)
                b.append(c)
            else: 
                c=int(i)
                b.append(c)
    while len(b)!=1:
        if '^' in b:
            Ans('^',b)
           
        elif '*' in b:
            if '/' in b:
                c=min(b.index('*'),b.index('/'))
                if b[c]=='*':
                    res=b[c-1]*b[c+1]
                else:
                    res=b[c-1]/b[c+1]
                Del_ins(c,res,b)
            else:
                Ans('*',b)
        elif '/' in b:
            Ans('/',b)
        elif '+' in b:
            Ans('+',b)
        elif '-' in b:
            Ans('-',b)
    return b
