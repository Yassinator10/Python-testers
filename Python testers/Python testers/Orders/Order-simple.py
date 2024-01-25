from ibapi.client import *
from ibapi.wrapper import *

from datetime import datetime

port = 7496


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):

        mycontract = Contract()
        #mycontract.exchange = "SMART"
        mycontract.conId = 265598
       
        mycontract.exchange = "SMART"
        #mycontract.currency = "USD"

        
        #mycontract.primaryExchange = "ISLAND"
        # mycontract.localSymbol = "ESH3"
        # mycontract.tradingClass = "SPXW"
        # mycontract.lastTradeDateOrContractMonth = "20230202"
        # mycontract.right = "P"
        # mycontract.strike = 4150

        myorder = Order()
        myorder.action = "BUY"
        myorder.totalQuantity = 1
        myorder.orderType = "MKT"
        myorder.tif = "DAY"
        #myorder.duration = ""
        #myorder.auxPrice= 160
        #myorder.goodTillDate = "20230713 15:15: FUCKKK"
        #myorder.auxPrice = 250
        #myorder.lmtPrice = 575.6
        #myorder.whatIf = True
        #myorder.cashQty = 100000
        #myorder.notHeld = True
        myorder.transmit = True

        self.placeOrder(orderId, mycontract, myorder)

    def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
        print("openOrder.", orderId, contract, order, orderState)

    # def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
    #     print("orderStatus", "datetime: ",datetime.now(), orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice)
    

app = TestApp()
app.connect("127.0.0.1", port, 1234)
app.run()

