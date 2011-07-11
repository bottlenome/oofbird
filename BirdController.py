#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BirdController:
  def __init__(self):
    this.watchData = WatchData()
    this.seller = Seller()
    this.buyer = Buyer()
    this.prophesy = Prophesy()

  def control(self):
    #HoldAction
    holdStocks = Parser.parseHoldStock(WebGetter.getHoldStock())
    holdList = this.watchData.getHoldList()
    if(holdMatch(holdStocks, holdList)):
      #donothing
    else:
      print "Hold stocks does not matched"
      this.watchData.updateHoldList(holdstocks)
    
    #watchAndMakeSellBuyDecision
    watchList = this.watchData.getWatchList()
    watchResult = []
    for i in watchList:
      tmpResult = Parser.parseWatchStock((WebGetter.getStockData(i))
      if(this.seller.sellDecision(tmpResult, i)):
        this.seller.sellAction(tmpResult, i)
      elif(this.buyer.buyDecision(tmpResult, i)):
        this.buyer.sellDecision(tmpResult, i)
      watchResult += tmpResult

    #makeWatchData
    this.watchData.addWatchList(this.prophesy.suggestStock())

    #makeDataModel
    DataModel.addResult(watchResult)

  ## @brief holdMatch function
  #         compare database holdList and sbi holdList
  #  @param [in] holdStocks sbi ID(int) array
  #  @param [in] holdList database ID(int) array
  #  @param [out] boolean true match
  #                         false don't match
  def holdMatch(self, holdStocks, holdList):
    lengthHoldStocks = len(holdStocks)
    lengthholdList = len(holdList)
    if(lengthHoldStocks != lengthholdList):
      return false
    for i in rage(lengthholdList):
      if(holdStocks[i] != holdStocks[i]):
        return false
    return true

