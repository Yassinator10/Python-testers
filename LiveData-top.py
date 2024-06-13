from decimal import Decimal
from ibapi.client import *
from ibapi.common import TickAttrib, TickerId
from ibapi.wrapper import *
from datetime import datetime
from ibapi.ticktype import TickType, TickTypeEnum
from ibapi.contract import ComboLeg

port = 7496

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
         
        mycontract = Contract()
        mycontract.exchange = "CBOE"
        mycontract.symbol = "XSP"
        mycontract.currency = "USD"
        mycontract.secType = "IND"
       # contract1 = Contract()
        #contract1.symbol = "GOOGL"
        #contract1.secType = "STK"
        #contract1.exchange = "NYSE"
        #contract1.currency = "USD"


        self.reqMarketDataType(4)
        self.reqMktData(
            reqId=orderId,
            contract=mycontract,
            genericTickList="",
            snapshot=False,
            regulatorySnapshot=False,
            mktDataOptions=[],
        )

    def marketDataType(self, reqId: TickerId, marketDataType: int):
        print("This is the Market Data Type requested" , marketDataType)
    
    def tickSize(self, reqId: TickerId, tickType: TickType, size: Decimal):    
         print(f"tickSize. reqId:{reqId}, tickType:{TickTypeEnum.to_str(tickType)}, size:{size}")

    def tickPrice(self, reqId: TickerId, tickType: TickType, price: float, attrib: TickAttrib):
            print(f"tickSize. reqId:{reqId}, tickType:{TickTypeEnum.to_str(tickType)}, Price: {price}")
    
    
    def tickOptionComputation(self, reqId: TickerId, tickType: TickType, tickAttrib: int, impliedVol: float, delta: float, optPrice: float, pvDividend: float, gamma: float, vega: float, theta: float, undPrice: float):
        print(f"tickOptionComputation. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, tickAttrib: {tickAttrib}, ImpVol: {impliedVol}, delta: {delta}, optPrice: {optPrice}, pvDividend: {pvDividend}, gamma: {gamma}, vega: {vega}, theta: {theta}, undPrice: {undPrice}")
        #return super().tickOptionComputation(reqId, tickType, tickAttrib, impliedVol, delta, optPrice, pvDividend, gamma, vega, theta, undPrice)
    
    def tickString(self, reqId: TickerId, tickType: TickType, value: str):
        print("tickString: ", reqId, TickTypeEnum.to_str(tickType), value)
        
    

    
    '''
    def tickPrice(
        self,
        reqId: TickerId,
        tickType: TickType,
        price: float,
        attrib: TickAttrib,
    ):  
        
        print(
            "tickPrice.",
            datetime.now(),
            f"reqId:{reqId}",
            f"tickType:{TickTypeEnum.to_str(tickType)}",
            f"price:{price}",
            f"attrib:{attrib}"
        )
    '''
    

    #def tickGeneric(self, reqId: TickerId, tickType: TickType, value: float):
     #   print(f"tickGeneric:  reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, value: {value}")

    # def tickString(self, reqId: TickerId, tickType: TickType, value: str):
    #     print("tickString: ", reqId, TickTypeEnum.to_str(tickType), value)
        
    # def tickNews(self, tickerId: int, timeStamp: int, providerCode: str, articleId: str, headline: str, extraData: str):
    #     print("tickNews",tickerId, timeStamp, providerCode, articleId, headline, extraData)

    # def tickSnapshotEnd(self, reqId: int):
    #     print(f"tickSnapshotEnd. reqId:{reqId}")
    #     self.disconnect()

    # def error(self, reqId: TickerId, errorCode: int, errorString: str, advancedOrderRejectJson=""):
    #     return super().error(reqId, errorCode, errorString, advancedOrderRejectJson)

    

app = TestApp()
app.connect("127.0.0.1", port, 100)

app.run()
