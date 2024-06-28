from ibapi.client import *
from ibapi.wrapper import *

from datetime import datetime

port = 7496


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):

        mycontract = Contract()
        mycontract.symbol ="AAPL"
        mycontract.currency = "USD"
        mycontract.exchange = "EDGX"
        mycontract.secType = "STK"   
        
        myorder = Order()
        myorder.action = "BUY" #"SELL"
        myorder.totalQuantity = 1
        myorder.orderType = "MKT"
        #myorder.lmtPrice = 210
        myorder.tif = "DAY"
        #myorder.account= "DU2732314"
        
        #myorder.trailingPercent = 0.01
        #myorder.trailStopPrice = 150
        #myorder.duration = ""
        #myorder.auxPrice= 160
        #myorder.goodTillDate = "20230713 15:15:"
        #myorder.auxPrice = 250
        #myorder.whatIf = True
        #myorder.cashQty = 100
        #myorder.outsideRth = True
        #Myorder.auxPrice = 17900
        
        #Order rejected reason this order doest comply to our derivative rules near expiration and policy!
        
        self.placeOrder(orderId, mycontract, myorder)

    def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
        print("openOrder.", orderId, contract, order, orderState)

    def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
        print("orderStatus", "datetime: ",datetime.now(), orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice)


    def execDetails(self, reqId: int, contract: Contract, execution: Execution):
        print(f"reqId: {reqId}, contract: {contract}, execution: {execution}")

    def error(self, reqId: TickerId, errorCode: int, errorString: str, advancedOrderRejectJson=""):
        print("Error", reqId, errorCode, errorString, advancedOrderRejectJson)


app = TestApp()
app.connect("127.0.0.1", port, 2)
app.run()
