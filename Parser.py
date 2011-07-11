#!/usr/bin/env python
# -*- coding: utf-8 -*-

import BeautifulSoup
from Stock import Stock

## @brief SBIparserClass
#         recieve html and return DataClass
#  @date 2011/7/7 makeout
class Parser:
  def __init__(self):
    #donothing

  ## @brief HoldStocksParser
  #         return HoldStockDataClass
  #  @param [in] html Sbi's one holdStock page html
  #  @param [out] holdStocks ID(int) array
  #         For compare database hold list and sbiholdlist
  def parseHoldStock(self, html):
    holdStocks = []
    soup = BeautifulSoup.BeautifulSoup(html)
    plice = soup.findAll('tr',bgcolor="#eceaf9")
    plice += soup.findAll('tr',bgcolor="#f9f9f9")
    for i in range(len(plice)//3):
      idTags = plice[3*i]
      self.holdStocks.append(idTags.find('td', colspan="4")
    holdStocks.sort()
    return holdStocks

