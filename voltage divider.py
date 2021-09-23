def setvalue(a):
    a=str(a)
    a=a[:a.index('.')+3]
    a=float(a)
    if a<1000:
        return str(a)
    elif a>999:
        return str(a/1000)+'k'
    elif a>999999:
        return str(a/1000000)+'M'

def adjcurrent(a):
    if a<1:
        i=0
        while(1):
            a*=10
            i+=1
            if a>=1 and i%3==0:
                a=str(a)
                if i//3==1: return (a[:a.index('.')+3]+'m')
                elif i//6==2: return (a[:a.index('.')+3]+'u')
                elif i//9==2: return (a[:a.index('.')+3]+'n')
                break
    return str(a)

v=int(input("Enter potential of higher side: "))
r=input("Enter the value of resistors in the branch: ").split()
R=[]
for x in r:
    if 'k' in x:
        R.append(float(x[:-1])*1000)
    elif 'M' in x:
        R.append(float(x[:-1])*1000000)
    else:
        R.append(float(x[:-1]))
        
R1=sum(R)

for x in r:
        print((x+' ohm').center(10,' '),end='')

print('\n'+str(v)+'V',end='')
for x in r:
        print('-^^^^^^^-',end='')
        
print('0')
for x in R:
        vd=(v*float(x))/R1
        vd=setvalue(vd)
        a=vd[:vd.index('.')+3]
        print((a+'V').center(10,' '),end='')
I=v/R1
I=adjcurrent(I)
R1=setvalue(R1)
print("\nTotal resistance of the branch: {}Ohm".format(R1))
print("Current flowing in the branch: {}A".format(I))

        
