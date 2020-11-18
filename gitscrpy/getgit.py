import requests
from bs4 import BeautifulSoup
import html5lib

class gitinit:
    
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
    def getuser(self,userd):
        urll="https://github.com/"+self.req
        r=requests.get(urll)
        soup=BeautifulSoup(r.content,'html5lib')
        sdd=soup.find("h1" ,class_="vcard-names pl-2 pl-md-0")
        name=sdd.find_all('span')[0].getText()
        u_name=sdd.find_all('span')[1].getText()
        asd=soup.find(class_="flex-order-1 flex-md-order-none mt-2 mt-md-0")
        dd=asd.find(class_="mb-3")
        followers=dd.find_all('a')[0].find('span').getText().strip(' ')
        following=dd.find_all('a')[1].find('span').getText().strip(' ')
        totstars=dd.find_all('a')[2].find('span').getText().strip(' ')
        asd=soup.find(class_="flex-order-1 flex-md-order-none mt-2 mt-md-0")
        dsdf=soup.find(class_="avatar avatar-user width-full border bg-white")['src']
        repo_num=soup.find(class_="UnderlineNav-body").find('span',class_="Counter").getText()
        rr=""
       
        if userd=="name":
            return(name)
        elif userd=="u_name":
            return(u_name)
        elif userd=="followers":
            return(followers)
        elif userd=="following":
            return(following)    
        elif userd=="star":
            return(totstars)
        elif userd=="img":
            retrun(dsdf)    
        else:
            x="""
            invalid param
            valid params:
               - name       => returns Name.
               - u_name     => returns Username.
               - followers  => returns no of Followers.
               - following  => returns no of Following.
               - star       => return no of stars user haves.
               - img        => returns the user avatar link
            """ 
            return(x)



