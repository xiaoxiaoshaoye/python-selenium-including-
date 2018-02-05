# coding=utf-8
import  urllib
import  urllib.request
import  urllib.response
import  re
import codecs

import  unicodedata

def getHtml(url):
    # 如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
    # 主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询
    #   headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}


    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
    rep =urllib.request.Request(url=url, headers=headers)


    response = urllib.request.urlopen(rep)
    html = response.read().decode("utf-8")#decode("ascii").encode("utf-8") decode("ascii").encode("utf-8")

    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)#re.compile() 可以把正则表达式编译成一个正则表达式对象.
    html = html.decode('utf-8') #python3之后，需要转码
    imglist = re.findall(imgre,html)#re.findall() 方法读取html 中包含 imgre（正则表达式）的数据。
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'D:/1.jpg')#直接将远程数据下载到本地
        x+=1


html = getHtml('http://www.douban.com/')# http://test.yunengzhe.com:846/tools/file/download/2184
print(html,end='')
# print(getImg(html))