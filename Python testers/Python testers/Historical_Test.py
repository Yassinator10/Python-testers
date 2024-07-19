from socket import timeout
from symtable import Symbol
from ibapi.client import *
from ibapi.wrapper import *
import datetime
from ibapi.tag_value import TagValue
from ibapi.contract import ComboLeg
import threading
datetime.datetime.now()
port = 7496


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        
        mycontract = Contract()
        mycontract.exchange = "CBOE"
        mycontract.secType ="IND"
        mycontract.symbol ="XSP"
        mycontract.currency = "USD"
      
        threading.Thread(target=self.reqHistoricalData(
            reqId=123,
            contract=mycontract,
            endDateTime="",
            #endDateTime="",
            #endDateTime=datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"),
            durationStr="2 D",
            barSizeSetting = "5 mins",
            whatToShow= "TRADES",#"TRADES",
            useRTH=1,
            formatDate=1,
            keepUpToDate=True,
            chartOptions=[],
        )).start()
        
    def historicalDataUpdate(self, reqId: int, bar: BarData):
        print("histUpdate.", reqId, bar)

    def historicalData(self, reqId: int, bar: BarData):
        print(reqId, bar)
        # print(bar.date)


    def historicalDataEnd(self, reqId: int, start: str, end: str):
        print(reqId, start, end)
       

    def error(self, reqId: TickerId, errorCode: int, errorString: str, advancedOrderRejectJson=""):
        print(reqId, errorCode, errorString, advancedOrderRejectJson)

    


app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()
