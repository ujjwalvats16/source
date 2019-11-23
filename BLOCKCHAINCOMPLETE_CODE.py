import hashlib
import datetime



class block():
    def __init__(self,data,id,x):
        self.data=data
        self.id=id
        self.x=x
        self.hash=self.gethash()
        
    def gethash(self):
        i=0
        while(1):
            es=(data+str(i)).encode()
            hs=(hashlib.sha256(es)).hexdigest()
            if(hs[:5]=="".zfill(5)):
                break
            
            i=i+1
            
        return hs 
    
    def printblock(self):
        if(id==0):
            bid="GENESIS BLOCK"
            prevhash="none"
        else:
            bid=self.id
            lastblock=self.x[-1]
            prevhash=lastblock["hash"]
        b={"id":bid,"hash":self.hash,"data":self.data,"prevhash":prevhash,"tstamp":datetime.datetime.now().strftime("%y-%m-%d %H-%M-%S")}
        self.x.append(b)
        return (self.x)
    
x=[] 
id=0
while(1): 
     
    data=input("enter the data ")
    if (data=="stop"):
        break
    else:
     Block=block(data,id,x)
     completeblockchain=Block.printblock()
     print(completeblockchain)
    id=id+1
     
print("the final blockchain is ",completeblockchain)      
      
    