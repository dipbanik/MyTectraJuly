f1var=open(r'C:\Users\Admin\Desktop\assigment\file_assignments\Python_Assignment_1\data.txt','r')
data=f1var.readlines()
new=data[0:]
l1=[]
for i in new:
    res=i.split('#')
    l1.append(res)
l2=[]

for j in l1:                        #unique
    if j not in l2:
        (l2.append(j))    
print(l2)



la=len(l2)
print(la)
for d in range(1,la):
    for e in range(1,la-d):
        if(l2[e][4]>l2[e+1][4]):
            temp=l2[e]              #ascending salary
            l2[e]=l2[e+1]
            l2[e+1]=temp
for k in l2:
    m='#'.join(k)
    print(m)
f1var.close()



        
        



        


    











