from decimal import Decimal
from ibapi.client import *
from ibapi.wrapper import *


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        print("NEXTVALIDID")
        # self.reqPnLSingle(105468, "DU5240685", "", 265598)
        self.reqPnL(orderId, "DU5240685", "")

    def pnlSingle(self, reqId: int, pos: Decimal, dailyPnL: float, unrealizedPnL: float, realizedPnL: float, value: float):
        print("pnlSingle", reqId, pos, dailyPnL, unrealizedPnL, realizedPnL, value)

    def pnl(self, reqId: int, dailyPnL: float, unrealizedPnL: float, realizedPnL: float):
        print("pnl",reqId, dailyPnL, unrealizedPnL, realizedPnL)

    def error(self, reqId: TickerId, errorCode: int, errorString: str, advancedOrderRejectJson=""):
        print("error",reqId, errorCode, errorString, advancedOrderRejectJson)
        
app = TestApp()
app.connect("127.0.0.1", 7496, 1001)
app.run()
