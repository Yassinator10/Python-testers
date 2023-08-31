from ibapi.client import *
from ibapi.wrapper import *
import datetime

port = 7496


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):

        mycontract = Contract()
        # mycontract.conId = 265598
        # mycontract.exchange = "ISLAND"
        # mycontract.currency = "USD"

        # Forex Contract
        # mycontract = Contract()
        # mycontract.symbol = "AUD"
        # mycontract.secType = "CASH"
        # mycontract.exchange = "IDEALPRO"
        # mycontract.currency = "USD"

        # Stock Contract
        mycontract = Contract()

        mycontract.symbol = "FMS"
        mycontract.secType = "STK"
        mycontract.currency = "USD"
        mycontract.exchange = "SMART"

        # FUT Contract
        # mycontract = Contract()
        # mycontract.localSymbol = "NQH3"
        # mycontract.secType = "FUT"
        # mycontract.exchange = "CME"
        # mycontract.currency = "USD"

        self.reqHistoricalTicks(
            reqId=123,
            contract=mycontract,
            startDateTime="",
            endDateTime="20230208 05:48:01 US/Eastern",
            numberOfTicks=100,
            whatToShow="BID_ASK",
            useRth=0,
            ignoreSize=True,
            miscOptions=[],
        )

    def historicalTicksLast(
        self, 
        reqId: int, 
        ticks: ListOfHistoricalTickLast, 
        done: bool,
    ):
        for tick in ticks:
            print(
                "historicalTicksLast.", 
                f"reqId:{reqId}", 
                datetime.datetime.fromtimestamp(tick.time),
                f"ticks:{tick.price}"
            )

    def historicalTicksBidAsk(
        self, 
        reqId: int, 
        ticks: ListOfHistoricalTickBidAsk, 
        done: bool,
    ):
        for tick in ticks:
            print(
                "historicalTicksLast.", 
                f"reqId:{reqId}", 
                datetime.datetime.fromtimestamp(tick.time),
                f"ticks:{tick}"
            )

    def historicalTicks(
        self, 
        reqId: int, 
        ticks: ListOfHistoricalTick, 
        done: bool,
    ):
        for tick in ticks:
            print(
                "historicalTicksLast.", 
                f"reqId:{reqId}", 
                datetime.datetime.fromtimestamp(tick.time),
                f"ticks:{tick.price}"
            )


app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()
