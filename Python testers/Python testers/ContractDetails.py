from ibapi.client import *
from ibapi.wrapper import *
from datetime import datetime

port = 7496

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        
        mycontract = Contract()
        
        #mycontract.conId = 589684571
        mycontract.symbol = "912796YH6"
        mycontract.secType = "BILL"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"        
        #mycontract.lastTradeDateOrContractMonth = "202310"

        self.reqContractDetails(reqId=orderId, contract=mycontract)
        
    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        # print(contractDetails.validExchanges)
        attrs = vars(contractDetails)
        print(
            datetime.now().strftime("%H:%M:%S.%f")[:-3],
            "contractDetails.",
            f"reqId:{reqId}",
            "\n",
            "\n".join(f"{name}: {value}" for name, value in attrs.items()),
            contractDetails.contract.conId
        )

    def contractDetailsEnd(self, reqId: int):
        print(
            datetime.now().strftime("%H:%M:%S.%f")[:-3],
            "contractDetailsEnd.",
            f"reqId:{reqId}",
        )
        self.disconnect()
        
    def bondContractDetails(self, reqId: int, contractDetails: ContractDetails):
        attrs = vars(contractDetails)
        print(
            datetime.now().strftime("%H:%M:%S.%f")[:-3],
            "bondDetails.",
            f"reqId:{reqId}",
            "\n",
            "\n".join(f"{name}: {value}" for name, value in attrs.items()),
        )

    def error(self, reqId: TickerId, errorCode: int, errorString: str, advancedOrderRejectJson=""):
        return super().error(reqId, errorCode, errorString, advancedOrderRejectJson)
        
app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()
