from ibapi.client import *
from ibapi.wrapper import *
from ibapi.contract import *
from ibapi.order_state import *

port = 7496


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        # Bull Put Spread
        parentContract = Contract() 
        parentContract.symbol = "SPX" # SPX OPT
        parentContract.secType = "BAG"
        parentContract.exchange = "SMART"
        parentContract.currency = "USD"

        sellChild = ComboLeg() 
        sellChild.conId = 581281393 # 3840 P SELL
        sellChild.exchange = "SMART"
        sellChild.ratio = 1
        sellChild.action = "SELL"

        buyChild = ComboLeg() 
        buyChild.conId = 581281376 # 3820 P Buy
        buyChild.exchange = "SMART"
        buyChild.ratio = 1
        buyChild.action = "BUY"

        parentContract.comboLegs = []
        parentContract.comboLegs.append(sellChild)
        parentContract.comboLegs.append(buyChild)

        # 3840 Contract
        c3820 = Contract()
        c3820.conId = 581281393
        c3820.exchange = "SMART"


        bullStop = Order()
        bullStop.orderId = orderId
        bullStop.action = "BUY"
        bullStop.orderType = "STP"
        bullStop.auxPrice = -4.50
        bullStop.totalQuantity = 1
        bullStop.ocaGroup = "TestOCA_", orderId
        bullStop.ocaType = 3

        self.placeOrder(orderId, parentContract, bullStop)

        bullStpLmt = Order()
        bullStpLmt.orderId = orderId + 1
        bullStpLmt.action = "BUY"
        bullStpLmt.orderType = "STP LMT"
        bullStpLmt.auxPrice = -4.45
        bullStpLmt.lmtPrice = -4.40
        bullStpLmt.totalQuantity = 1
        bullStpLmt.ocaGroup = "TestOCA_", orderId
        bullStpLmt.ocaType = 3

        self.placeOrder(bullStpLmt.orderId, parentContract, bullStpLmt)

        o3840S = Order()
        o3840S.orderId = orderId+2
        o3840S.action = "SELL"
        o3840S.orderType = "STP"
        o3840S.auxPrice = 27.60
        o3840S.totalQuantity = 1
        o3840S.ocaGroup = "TestOCA_", orderId
        o3840S.ocaType = 3

        self.placeOrder(o3840S.orderId, c3820, o3840S)

        o3840SL = Order()
        o3840SL.orderId = orderId+3
        o3840SL.action = "SELL"
        o3840SL.orderType = "STP LMT"
        o3840SL.auxPrice = 27.50
        o3840SL.lmtPrice = 27.50
        o3840SL.totalQuantity = 1
        o3840SL.ocaGroup = "TestOCA_", orderId
        o3840SL.ocaType = 3

        self.placeOrder(o3840SL.orderId, c3820, o3840SL)


app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()
