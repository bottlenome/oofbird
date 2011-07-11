#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Stock:
  def __init__(self,id,plice):
    self.id = id
    self.plice = plice
  
  def show(self):
    print "id:" + self.id
    print "plice:" + self.plice
  
  def returnStock(self,idTags,pliceTags):
    self.id = idTags.find('td', colspan="4")
    self.plice = pliceTags.findAll('td')
    return Stock(self.id.contents[0], self.plice[1].contents[0])

