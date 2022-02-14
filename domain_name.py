def domain_name(url):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]

import re
def domain_name(url):
    return re.search("(//|www.)(\w+)[.]", url).group(2)

def domain_name(url):
    return url.split("://")[-1].split(".")[-2]
      
print(domain_name('http://hello.com'))