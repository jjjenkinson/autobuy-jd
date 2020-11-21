import time
import re
import requests
import socket,getpass
from JDAutoBuyTool import sendError
import JDAutoBuyTool as jd

# print('time.asctime() = {}'.format(time.asctime()))

# print('time.time() = {}'.format(time.time()))
# print('time.time() = {}'.format(time.time()))
# print('username = {}, hostname = {}'.format(getpass.getuser(),socket.gethostname()))

infilename = './Please fill out this document.txt'
fp = open(infilename, 'r', encoding='utf-8')
cont = fp.read()
pattern = re.compile("'(.*)'")
contRe = pattern.findall(cont)
# print('contRe = ',contRe)
contRe = contRe[2:]
fp.close()
url =contRe
# print(url)
for i in url:
    skuId = i.split('skuIds=')[1].split('%2C')[2]
    skuIdUrl = 'https://item.jd.com/' + skuId + '.html'
    print('skuIdUrl = {}'.format(skuIdUrl))

    mysession = requests.session()
    mysession.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Accept": "*/*",
        "Connection": "keep-alive"
        }
    
    response = mysession.get(i)
    # print('response = ',response.text)  #
    j = response.text.find(str(skuId))
    # print(response.text.find(str(skuId)))
    # print(len(str(skuId)))
    # print(response.text[j:j+len(str(skuId))])
    tmp = response.text.split(str(skuId))[1]
    m = tmp.find('{')
    n = tmp.find('}')
    tmp = tmp[m:n+1]
    print(m,n)
    print(tmp)

dict1 = {
    'a' : 12,
    'b' : 23
}
print(dict1)


