#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
from pit import Pit

url = 'k.sbisec.co.jp'
top = '/bsite/visitor/top.do'
login = '/bsite/visitor/loginUserCheck.do'
holdStock = '/bsite/member/acc/holdStockList.do'

class WebGetter:
  def __init__():
    #donothing

  def getHoldStock(self):
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
    return r.read()

  def getStockData(self, watchStock):
    #donothing

  def limitSell(self, stockID, price, count):
    #donothing

  def sell(self, stockID, count):
    #donothing

  def limitBuy(self, stockID, price, count):
    #donothing

  def buy(self, stockID, count):
    #donothing


