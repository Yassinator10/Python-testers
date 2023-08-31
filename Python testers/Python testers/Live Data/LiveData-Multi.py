from decimal import Decimal
from ibapi.client import *
from ibapi.wrapper import *
from datetime import datetime
from ibapi.contract import ComboLeg
from threading import Thread
import time

port = 7496

FUTCONTRACT = []

# request a list of contracts
class contractApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    # Build EClient parameters and Contract Details requests to be sent out
    def nextValidId(self, orderId: OrderId):
        
        mycontract = Contract()
        mycontract.symbol = "CL"
        mycontract.secType = "FUT"
        mycontract.exchange = "NYMEX"
        mycontract.currency = "USD"
        mycontract.multiplier = "1000"

        self.reqContractDetails(reqId=orderId, contract=mycontract)
        
    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        FUTCONTRACT.append(contractDetails.contract)
        

    def contractDetailsEnd(self, reqId: int):
        print(f"total Contracts: {len(FUTCONTRACT)}")
        self.disconnect()

# request market data for that list
class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.contract_counter = 0

    # Build EClient parameters and Contract Details requests to be sent out
    def nextValidId(self, orderId: OrderId):
            
        currentConId = 0
        nextConId = 1
        requestId = 123
        print("LOOP START")
        
        for contract in range(len(FUTCONTRACT)):
            
            if nextConId < len(FUTCONTRACT):
                
                mycontract = FUTCONTRACT[currentConId]

                newThread = Thread(target=self.reqMktData(
                    reqId=requestId,
                    contract=mycontract,
                    genericTickList="",
                    snapshot=False,
                    regulatorySnapshot=False,
                    mktDataOptions=[],
                ))

                newThread.start()

                requestId += 1
                currentConId += 1
                nextConId += 1


    def tickPrice(
        self,
        reqId: TickerId,
        tickType: TickType,
        price: float,
        attrib: TickAttrib,
    ):
        print(
            "tickPrice.",
            f"reqId:{reqId}",
            f"tickType:{tickType}",
            f"price:{price}",
            f"attrib:{attrib}"
        )

    # def tickSnapshotEnd(self, reqId: int):
    #     print(f"tickSnapshotEnd. reqId:{reqId}")


def main():

    app = contractApp()
    app.connect("127.0.0.1", port, 1001)
    app.run()

    time.sleep(3)

    app = TestApp()
    
    app.connect("127.0.0.1", port, 1001)
    app.run()

if __name__ == "__main__":
    main()