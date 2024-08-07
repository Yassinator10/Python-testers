from socket import timeout
from symtable import Symbol
from ibapi.client import *
from ibapi.wrapper import *
import datetime
from ibapi.tag_value import TagValue


port = 7496


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        
        mycontract = Contract()
        mycontract.localSymbol = "SPX   240517P05220000"
        
        mycontract.secType = "OPT"
        
        mycontract.exchange = "SMART"
        
        
        self.reqHistoricalData(
            reqId=123,
            contract=mycontract,
            endDateTime="",
            durationStr= "100 S",
            barSizeSetting = "1 secs",
            whatToShow= "BID_aSK",
            useRTH=0,
            formatDate=1,
            keepUpToDate=False,
            chartOptions=[],
        )
        

    def historicalData(self, reqId: int, bar: BarData):
         print("DATA", reqId, bar)

    def historicalDataUpdate(self, reqId: int, bar: BarData):
        print("UPDATE: ", reqId, bar)
        # self.cancelHistoricalData(reqId)
        
    def historicalDataEnd(self, reqId: int, start: str, end: str):
        print("historicalDataEnd")

    def error(self, reqId: TickerId, errorCode: int, errorString: str, advancedOrderRejectJson=""):
        print(reqId, errorCode, errorString, advancedOrderRejectJson)

app = TestApp()
app.connect("127.0.0.1", port, 101)
app.run()
 
