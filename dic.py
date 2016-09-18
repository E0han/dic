#dictionary by 0han
#coding:utf-8
import requests
import bs4
import os
import time
import sys

def createlog():
    form="%Y-%m-%d %X"
    hr="========"
    f=open("C:/Users/Owner/Dropbox/python/py/dic/log.txt", 'a', encoding='utf-8')
    f.write('\n'+hr+'\n'+time.strftime(form,time.localtime())+'\n'+hr)
    f.close()

print("===============================\n=有道词典 命令行版v1.1 by 0han=\n===============================\n")
print("输入'q'可退出程式\n")
createlog()
while True:
    rooturl='http://www.youdao.com/w/'
    url=input("请输入词语：")
    f=open("C:/Users/Owner/Dropbox/python/py/dic/log.txt", 'a', encoding='utf-8')
    if url=="q":
        print("log日志已储存 谢谢使用")
        f.close()
        sys.exit()
    else:
        finurl=rooturl+url
        headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36')
        res={}
        try:
            response = requests.get(finurl)
            soup = bs4.BeautifulSoup(response.text,'html.parser')
            word=soup.select('.keyword')[0].get_text()
            tran=soup.select('.trans-container > ul > li')[0].get_text()
            print('翻译:'+tran)
            res['word']=word
            res['翻译']=tran
            f.write('\n'+str(res))
            f.close() 
        except IndexError:
            print("好像没找到这个词，请重新输入")