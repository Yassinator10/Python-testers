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
        mycontract.exchange = "CFE"
        mycontract.conId = 644107697
       

        threading.Thread(target=self.reqHistoricalData(
            reqId=123,
            contract=mycontract,
            endDateTime="20240401 23:59:59 UTC",
            #endDateTime="",
            #endDateTime=datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"),
            durationStr= "20 D",
            barSizeSetting = "30 mins",
            whatToShow= "TRADES",#"TRADES",
            useRTH=0,
            formatDate=1,
            keepUpToDate=False,
            chartOptions=[],
        )).start()
        '''
        threading.Thread(self.reqHistoricalData(
            reqId=456,
            contract=mycontract,
            # endDateTime="20230208 10:47:01 US/Eastern",
            endDateTime="",
            # endDateTime=datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"),
            durationStr= "3600 S",
            barSizeSetting = "15 mins",
            whatToShow= "TRADES",
            useRTH=1,
            formatDate=1,
            keepUpToDate=True,
            chartOptions=[],
        )).start()
    '''
    def historicalDataUpdate(self, reqId: int, bar: BarData):
        print("histUpdate.", reqId, bar)

    def historicalData(self, reqId: int, bar: BarData):
        print(reqId, bar)
        # print(bar.date)


    def historicalDataEnd(self, reqId: int, start: str, end: str):
        print(reqId, start, end)
        self.disconnect()

    def error(self, reqId: TickerId, errorCode: int, errorString: str, advancedOrderRejectJson=""):
        print(reqId, errorCode, errorString, advancedOrderRejectJson)



app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()

