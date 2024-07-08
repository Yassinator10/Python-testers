from ibapi.client import *
from ibapi.wrapper import *
from datetime import datetime

port = 7496


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):

        self.reqSecDefOptParams(  
            reqId=123,
            
            underlyingSymbol="ES",
            futFopExchange="CME",  #Only for FOP
            underlyingSecType="FUT",
            underlyingConId="568550526",
        )

    def securityDefinitionOptionParameter(
        self,
        reqId: int,
        exchange: str,
        underlyingConId: int,
        tradingClass: str,
        multiplier: str,
        expirations: SetOfString,
        strikes: SetOfFloat,
    ):
        print(
            "securityDefinitionOptionParameter.",
            f"reqId:{reqId}",
            f"exchange:{exchange}",
            f"underlyingConId:{underlyingConId}",
            f"tradingClass:{tradingClass}",
            f"multiplier:{multiplier}",
            f"expirations:{expirations}",
            f"strikes:{strikes}",
        )

    def securityDefinitionOptionParameterEnd(self, reqId: int):
        print(f"securityDefinitionOptionParameterEnd. reqId:{reqId}")


app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()
