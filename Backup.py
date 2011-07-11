#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import commands
import httplib,urllib
import mechanize
import BeautifulSoup
from  pit import Pit

url = 'k.sbisec.co.jp'
top = '/bsite/visitor/top.do'
login = '/bsite/visitor/loginUserCheck.do'
holdStock = '/bsite/member/acc/holdStockList.do'

class Stock:
  def __init__(self,id,plice):
    self.id = id
    self.plice = plice
  def show(self):
    print "id:" + self.id
    print "plice:" + self.plice

class HoldStock:  
  
  def __init__(self):
    self.data = []
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open('https://' + url + login)
    br.select_form(nr=0)
    idPass = Pit.get('oofbird')
    br['username'] = idPass['login']
    br['password'] = idPass['password']
    br.submit()
    r = br.open('https://' + url + holdStock)
    tmp = r.read()
    soup = BeautifulSoup.BeautifulSoup(tmp)
    plice = soup.findAll('tr',bgcolor="#eceaf9")
    plice += soup.findAll('tr',bgcolor="#f9f9f9")
    for i in range(len(plice)//3):
      self.data.append(self.returnStock(plice[3*i], plice[3*i+1]))

    for i in self.data:
      i.show()

  def returnStock(self,idTags,pliceTags):
    self.id = idTags.find('td', colspan="4")
    self.plice = pliceTags.findAll('td')
    return Stock(self.id.contents[0], self.plice[1].contents[0])


htmlheader = '''Content-Type: text/html; charset=UTF8
Pragma: no-cache
Cache-Control: no-cache
Expires: 0

'''
html = '''<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF8">
  <STYLE TYPE="text/css">
  <!--
  body,font,tr,td { font-size: 10pt }
  small { font-size: 9pt }
  -->
  </STYLE>
  
  <title>LikeLoveless</title>
</head>
<body bgcolor="#000000" text="#ffffff" link="#8888ff" vlink="#8888CC">
'''

htmlfooter='''
</body>
</html>

'''
html = htmlheader + html
html += '<br>'

html += htmlfooter
print html

print HoldStock()

