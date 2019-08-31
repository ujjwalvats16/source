import os
import io

import datetime

     

 
with io.open('output.txt','a',encoding='utf-8') as f1:
 for files in os.walk('c:\\',topdown=True):
     if len(files)>0:
         for paths in files:
             #print(type(paths))
             if('list' in str(type(paths))):
              for k in range(len(paths)):
                   
                 data=str(files[0]+'\\'+str(paths[k])+'\n')
                 data=data.replace(r'\\','\\')
                 
                 f1.write(data)
             else:    
              #print(paths,end='#')   
              f1.write(paths+'\n')
          
 f1.close()
with io.open('newoutput.txt','a',encoding='utf8') as f3:
    with io.open('output.txt')as f2:
        dataf=f2.read()
        dataf=str(dataf)
        dataf=dataf.split('\n')
        for line in dataf:
         if len(line) >0:
          try:   
           x=(os.stat(line))
           print(x)
           ctime = x.st_ctime
           mtime = x.st_mtime
           atime = x.st_atime
           timestamp_cstr = datetime.datetime.fromtimestamp(ctime).strftime('%Y-%m-%d')
           timestamp_mstr = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
           timestamp_astr = datetime.datetime.fromtimestamp(atime).strftime('%Y-%m-%d')
          except:
           timestamp_cstr='ERROR'
           timestamp_mstr='ERROR'
           timestamp_astr='ERROR'
          
             
    
         
         
          datarow=line+','+timestamp_cstr+','+timestamp_mstr+','+timestamp_astr+','+str(x.st_size)+','+datetime.datetime.today().strftime("%Y-%m-%d")+'\n'
          f3.write(datarow)
    f2.close() 

    f3.close()