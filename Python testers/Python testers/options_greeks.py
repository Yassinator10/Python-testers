from ibapi.client import *
from ibapi.wrapper import *
from datetime import datetime



class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId:int):
        print("connected")
        self.start()

    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson):
        print("Error: ", reqId, " ", errorCode, " ", errorString)
    '''
    def tickSize(self, reqId: TickerId, tickType: TickType, size: Decimal):
        print(f"tickSize. reqId:{reqId}, tickType:{TickTypeEnum.to_str(tickType)}, size:{size}")

    def tickGeneric(self, reqId: TickerId, tickType: TickType, value: float):
        print(f"tickGeneric:  reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, value: {value}")

    def tickString(self, reqId: TickerId, tickType: TickType, value: str):
        print("tickString: ", reqId, TickTypeEnum.to_str(tickType), value)

    def tickNews(self, tickerId: int, timeStamp: int, providerCode: str, articleId: str, headline: str, extraData: str):
        print("tickNews",tickerId, timeStamp, providerCode, articleId, headline, extraData)
    '''
    def tickOptionComputation(self, reqId: TickerId, tickType: TickType, tickAttrib: int, impliedVol: float, delta: float, optPrice: float, pvDividend: float, gamma: float, vega: float, theta: float, undPrice: float):
        print(f"tickOptionComputation. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, tickAttrib: {tickAttrib}, ImpVol: {impliedVol}, delta: {delta}, optPrice: {optPrice}, pvDividend: {pvDividend}, gamma: {gamma}, vega: {vega}, theta: {theta}, undPrice: {undPrice}")
    def tickSnapshotEnd(self, reqId: int):
        print(f"tickSnapshotEnd. reqId:{reqId}")
        self.disconnect()

    def stop(self):
        self.disconnect()
        print("disconnected")

    def start(self):
        contract = Contract()

        contract.conId = 680710765
        contract.exchange = "SMART"


        self.reqMktData(210, contract, "", False, False, [])


def main():
    app = TestApp()
    app.connect('127.0.0.1', 7496, 123)
    #Timer(3, app.stop).start()
    app.run()


if __name__ == "__main__":
    main()