import re
import io

#patteren=re.compile(r"[+]?91[-.' '][98]\d{2}[-.]\d{4}[-.]\d{4}")
patteren=re.compile(r"[+]?91[-.' '][98]\d{2}[-.]\d{4}[-.]\d{4}")
with io.open("num.txt","r",encoding="utf8") as f1:
     str=f1.read()
     f1.close()
     match=patteren.finditer(str)
     for x in match:
         print(x)
         
         
patteren=re.compile(r"(Mr\.\s|Ms\.\s|Mrs\.\s)?[A-Za-z]+[','][A-Za-z]+")
with io.open("name.txt","r",encoding="utf8") as f1:
     str=f1.read()
     f1.close()
     match=patteren.finditer(str)
     for x in match:
         print(x)
         
         
patteren=re.compile(r"(http://|https://)?(www.)[A-Za-z]+[A-Za-z.]+")
with io.open("url.txt","r",encoding="utf8") as f1:
     str=f1.read()
     f1.close()
     match=patteren.finditer(str)
     for x in match:
         print(x.group(0))
          
patteren=re.compile(r"[A-Za-z]+[._][A-Za-z]+@(yahoo.com|yahoo.in|yahoo.co.in.us)")
with io.open("mail.txt","r",encoding="utf8") as f1:
     str=f1.read()
     f1.close()
     match=patteren.finditer(str)
     for x in match:
         print(x.group(0))  
         
print(help(re.finditer))
         
                 
                 
         
          