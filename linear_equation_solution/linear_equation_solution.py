import numpy as np
import re
from numpy import dtype
value_sol="TRUE"
dic={}
query1=re.compile(r"[0-9]?")
n_eq=input("enter the no of equation")
a=np.empty(1)
for i in range(1,int(n_eq)+1):
    eq=input(f"enter the {i} equation")
    a=np.vstack([a,eq])
     
a=np.delete(a, (0), axis=0)    
print(a) 
 
query=re.compile(r"([0-9]?|[0-9]*)[a-zA-Z+-]")
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
query=re.compile(r"[a-zA-Z]")
li=[]
for i in a:
    

     
 match=query.finditer(str(i))
 for items in match:
     
     items=items.group(0)
     li.append(items)

setl=list(set(li))
if(len(a)>len(setl) or len(a)==len(setl)):
    ap=np.empty([1,len(setl)],dtype=str)
    for j in range(len(dic)):
        cof=[]
        for m in range(len(setl)):
            
            if setl[m] in dic[j]:
             q=re.compile(r"[+-]?([0-9]?|[0-9]*)"+ setl[m])
             var=q.finditer(dic[j])
             for vars in var:
                 vars=vars.group(0)
                 print(vars)
                 if ("+" in vars):
                     if (vars[0].isdigit()or vars[1].isdigit()):
                      print("sign")  
                      q=re.compile(r"[0-9]")
                      conf=q.finditer(vars)
                      for confs in conf:
                          confs=confs.group(0)
                          #print(confs)
                          cof.append(confs)
                     else:
                         confs=1
                         #print(m,vars)
                         
                         cof.append(confs)
                 if ("-" in vars):
                     if (vars[0].isdigit() or vars[1].isdigit()):
                      q=re.compile(r"[0-9]+")
                      conf=q.finditer(vars)
                      for confs in conf:
                          print(vars)
                          print("-ve")
                          confs=(confs.group(0))
                          print("this is"+ confs)
                          confs=int(confs) * -1
                          cof.append(confs)
                     else:
                         confs=-1
                         cof.append(confs)       
                 if((not("-" in vars)) and (not("+" in vars))):
                     strlen=len(vars)
                     if (vars[0].isdigit()):
                      print("no sign")  
                      q=re.compile(r"([0-9]+)")
                      conf=q.finditer(vars)
                      for confs in conf:
                          confs=confs.group(0)
                          #print("confs")
                          cof.append(confs)
                     else:
                         confs=1
                         cof.append(confs)
                         
                 
            else:
             cof.append("0")
             print("not")
        print(cof)
        while '' in cof:
         cof.remove('')          
        ap=np.vstack([ap,cof])
    ap=np.delete(ap,(0),axis=0)     
    print("coefficient is ",end=" ")
    print(setl)
    ap=ap.astype("float64")     
    print(ap)
    
    
    b=np.empty(1)
    for ii in range(len(a)):
        x=a[ii] 
        x=str(x).split("=") 
        x=x[1]
        x=x.replace("']","")
        x=int(x)
        b=np.vstack([b,x])
        c=b[1:]
        c=c.astype("float64")
      
    try:
     sol=np.linalg.solve(ap,c)
     for jj in range(len(setl)):
               v_v=str(sol[jj])
               v_n=str(setl[jj])
               print(f"value of {v_n} is {v_v}") 
    except np.linalg.LinAlgError as e:
     value_sol=="FALSE"   
     print(e)
     print(f"solution not possible due to {e}")
        
    
              
else:
    print("solution not possible variable count is greater than the no of equation")    