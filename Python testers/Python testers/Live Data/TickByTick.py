from decimal import Decimal
from ibapi.client import *
from ibapi.wrapper import *
from datetime import datetime
port = 7496


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):

        mycontract = Contract()
        mycontract.conId = 265598
        #mycontract.localSymbol = "ESH3"
        #mycontract.secType = "FUT"
        mycontract.exchange = "SMART"
        #mycontract.currency = "USD"

        self.reqTickByTickData(
            reqId=123,
            contract=mycontract,
            tickType="BidAsk",
            numberOfTicks=1,
            ignoreSize=False
        )

    # whatToShow=BidAsk
    def tickByTickBidAsk(self, reqId: int, time: int, bidPrice: float, askPrice: float, bidSize: int, askSize: int, tickAttribBidAsk: TickAttribBidAsk):
        print(f"reqId: {reqId}, time: {datetime.fromtimestamp(time) }, bidPrice: {bidPrice}, askPrice: {askPrice}, bidSize: {bidSize}, askSize: {askSize}, tickAttribBidAsk: {tickAttribBidAsk}")

    # whatToShow=MidPoint
    def tickByTickMidPoint(self, reqId: int, time: int, midPoint: float):
        print(f"reqId: {reqId}", time, midPoint)

    # # whatToShow=AllLast
    def tickByTickAllLast(self, reqId: int, tickType: int, time: int, price: float, size: int, tickAttribLast: TickAttribLast, exchange: str, specialConditions: str):
        print(f"reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, time: {datetime.fromtimestamp(time)}, price: {price}, size: {size}, tickAttribLast: {tickAttribLast}, exchange: {exchange}, specialConditions: {specialConditions}")

    def tickSnapshotEnd(self, reqId: int):
        print(f"tickSnapshotEnd. reqId:{reqId}")

    def error(self, reqId: TickerId, errorCode: int, errorString: str, tickAttrib):
        print(f"error. reqId:{reqId} code:{errorCode} string:{errorString}")


app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()
