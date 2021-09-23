def setvalue(a):
    if a<1000:
        return str(a)
    elif a>999:
        return str(a/1000)+'k'
    elif a>999999:
        return str(a/1000000)+'M'

def adjcurrent(i,j,a):
    if i%3==0:
        j+=1
        if j==1: ch='m'
        elif j==2: ch='u'
        elif j==3: ch='n'
        
    if a<1:
        a*=10
        i+=1
        adjcurrent(i,j,a)
        
    
            
    

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
i=0
j=0
ch=''
adjcurrent(i,j,I)

print("\nTotal resistance of the branch: ",R1,'Ohm')
print("Current flowing in the branch: ",I,ch,"A")

        
