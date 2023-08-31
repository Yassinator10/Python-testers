from ibapi.client import *
from ibapi.wrapper import *

port = 7496

class TestApp(EClient, EWrapper):

    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        self.reqOpenOrders()

    def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
        print("openOrder: ",orderId, contract, order, orderState)

    def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
        print("openStatus: ",orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice)


app = TestApp()
app.connect("127.0.0.1", port, 0)
app.run()
