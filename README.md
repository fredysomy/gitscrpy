# git_py
```python
import requests
from bs4 import BeautifulSoup
import html5lib

class Mainywe:
    
    def __init__(self,name):
        self.req=name
        global url
        url="https://github.com/{}?tab=repositories"
    def getrepo(self,no):
        r=requests.get(url.format(self.req))
        soup=BeautifulSoup(r.content,'html5lib')
        a=soup.find(id="user-repositories-list")
        z=a.find_all('li')
        yo={}
        er=[]
        
        for i in range(0,no):
            s=z[i]
            
            try:
                y=s.find('a')
                x=y['href']
                try:
                    ur=[]
                    sds=s.find('a',class_="muted-link mr-3").getText()
                    

                    j=s.find('p').getText()
                    name=y.getText()
                    url2="https://github.com"+x
                    k={'name':name.strip(),'description':j.strip(),'url':url2,"stars":sds.strip()}
                    er=er+[k]
                except:
                    ur=[]
                    h=y.getText()
                    y="https://github.com"+x
                    k={'name': h.strip(),'url':y,"stars":sds.strip()}
                    er=er+[k]
                
            except:
                print("none")
            
        return er

```
