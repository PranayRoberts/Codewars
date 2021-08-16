"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""

def domain_name(url):
    
    f=0 #to check if it starts with something in z or not eg: mofos.com 
    z=["https://","http://", "www."]
    for i in z:
        if i in url:
            x=list(url.split(i))
            f=1
    y=list(url.split("."))
    if f==1:
        z=x+y
        res=z[1].split('.')
    else:
        z=y
        res=z[0].split('.')
    
    return res[0]
