import numpy as np
import re
from sympy.polys.partfrac import apart

n_eq=input('enter the no of equation')
a=np.empty(1)
for i in range(1,int(n_eq)+1):
    eq=input(f"enter the {i}equation")
    a=np.vstack([a,eq])
    
a=np.delete(a,(0),axis=0)    
print(a)
dic={}
query=re.compile(r"([0-9]?[0-9]*)[a-zA-Z+-]")
k=0
for i in a:
    x=''
    match=query.finditer(str(i))
    for items in match:
        items=items.group(0)
        x=x+items
    dic[k]=x 
    k=k+1 
    print(dic) 
    
query=re.compile(r"[a-zA-z]")
li1=[]
for i in dic:
    match=query.finditer(dic[i])
    print(i)
    for items in match:
        items=items.group(0)
        
        li1.append(str(items))
        
#print(li1)    
setl=list(set(li1))  
#print(setl)

if(len(a)>len(setl) or len(a) ==len(setl)) :
    ap=np.empty([1,len(setl)],dtype=str)
    for j in range(len(dic)):
        cof=[]
        for m in range(len(setl)):
            if setl[m] in (dic[j]):
                q=re.compile(r"[+-]?([0-9]?|[0-9]*)"+setl[m])
                var=q.finditer(dic[j])
                for vars in var:
                    vars=vars.group(0)
                    #print(vars)
                    if ('+') in vars:
                        if(vars[0].isdigit() or vars[1].isdigit()):
                            q=re.compile(r"[0-9]+")
                            conf=q.finditer(vars)
                            for confs in conf:
                                confs=confs.group(0)
                                cof.append(confs)
                                
                        else:
                            confs=1
                            cof.append(confs)
        #           
                     
                    if ('-') in vars:
                        if(vars[0].isdigit() or vars[1].isdigit()):
                            q=re.compile(r"[0-9]+")
                            conf=q.finditer(vars)
                            for confs in conf:
                                confs=confs.group(0)
                                confs=int(confs) * (-1)
                                cof.append(confs)
                                
                        else:
                            confs=-1
                            cof.append(confs)

                    if((not('+' in vars)) and (not('-' in vars))):
                        if(vars[0].isdigit()):
                            q=re.compile(r"[0-9]+")
                            conf=q.finditer(vars)
                            for confs in conf:
                                confs=confs.group(0)
                                cof.append(confs)
                            
                        else:
                            confs=1
                            cof.append(confs)
                            
            else:
                cof.append("0")
        #print(cof)        
        ap=np.vstack([ap,cof])
    bp=ap[1:,:]
    ap=np.delete(ap,(0),axis=0)
    
    print("coefficient of",end=',')
    print(setl)
    print(bp)
    ap=ap.astype('float64')
    b=np.empty(1)
    for ii in range(len(a)):
        x=a[ii]
        x=str(x).split('=')
        x=(x[1])
        x=x.replace("']","")
        b=np.vstack([b,x])
        
    b=b[1:]
    b=b.astype(float)
    print(b)
    
    try:
        sol=np.linalg.solve(ap,b)
        for jj in range(len(setl)):
            v_v=str(sol[jj])
            v_r=str(setl[jj])
            print(f"value of {v_r} is {v_v}")
            
    except np.linalg.LinAlgError as e:
        print(e)
        print(f"solution not possible due to {e}")   
        
        
        
else:
    print("solution not possible as no of variable is greater than no of equations")       
        
print(np.allclose(np.dot(ap, sol), b))           