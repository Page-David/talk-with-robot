#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      user
#
# Created:     02/11/2015
# Copyright:   (c) user 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib.request,json,urllib.parse
def getHtml(url):
    return urllib.request.urlopen(url).read()
if __name__=='__main__':
    key='4b130e3d0fa202cb8499327de4ce0bcc'
    api='http://www.tuling123.com/openapi/api?key='+key+'&info='
    while True:
        info=input('我：')
        request=api+urllib.parse.quote(info)
        response=getHtml(request)
        dic_=json.loads(response.decode())
        #print(request)
        print('机器人：'+dic_['text'])
