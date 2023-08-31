from asyncio.windows_events import NULL
from decimal import Decimal
from pickle import FALSE, TRUE
from queue import PriorityQueue
from threading import Timer
from ibapi.tag_value import TagValue
from tkinter.tix import Tree
from ibapi.client import *
from ibapi.wrapper import *
from datetime import datetime
from ibapi.contract import *
from ibapi.order_condition import Create, OrderCondition
from ibapi.order_state import *
import time

port = 7496


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        print(f"nextValidId. orderId={orderId}")

        mycontract = Contract()
        # mycontract.conId = 422302967 # TMBR STK
        mycontract.symbol = "AAPL"
        mycontract.secType = "STK"
        mycontract.exchange = "NYSE"
        mycontract.currency = "USD"

        myorder = Order()
        myorder.orderId = orderId
        myorder.orderType = "PEG MID"
        myorder.action = "BUY"
        myorder.lmtPrice = 51.65
        myorder.tif = "DAY"
        #myorder.goodTillDate = "20220928 12:53:02 America/Chicago"
        myorder.totalQuantity = 1
        #myorder.notHeld = False
        #myorder.minTradeQty = 2
        #myorder.midOffsetAtWhole = 10
        #myorder.midOffsetAtHalf = 5

        self.placeOrder(myorder.orderId, mycontract, myorder)

    def marketRule(self, marketRuleId: int, priceIncrements: ListOfPriceIncrements):
        print("Market Rule details: ", marketRuleId, priceIncrements)

    def openOrder(
        self,
        orderId: OrderId,
        contract: Contract,
        order: Order,
        orderState: OrderState,
    ):
        print(
            "openOrder.",
            f"orderId:{orderId}",
            f"contract:{contract}",
            f"order:{order}",
            f"orderState:{orderState}",
        )

    def orderStatus(
        self,
        orderId: OrderId,
        status: str,
        filled: Decimal,
        remaining: Decimal,
        avgFillPrice: float,
        permId: int,
        parentId: int,
        lastFillPrice: float,
        clientId: int,
        whyHeld: str,
        mktCapPrice: float,
    ):
        print(
            "orderStatus.",
            f"orderId:{orderId}",
            f"status:{status}",
            f"filled:{filled}",
            f"remaining:{remaining}",
            f"avgFillPrice:{avgFillPrice}",
            # f"permId:{permId}",
            f"parentId:{parentId}",
            f"lastFillPrice:{lastFillPrice}",
            # f"clientId:{clientId}",
            # f"whyHeld:{whyHeld}",
            # f"mktCapPrice:{mktCapPrice}",
        )
        self.disconnect()

    def error(
        self,
        reqId: TickerId,
        errorCode: int,
        errorString: str,
        advancedOrderRejectJson="",
    ):
        print(
            datetime.now().strftime("%H:%M:%S.%f")[:-3],
            "error.",
            f"reqId:{reqId}",
            f"errorCode:{errorCode}",
            f"errorString:{errorString}",
            f"advancedOrderRejectJson:{advancedOrderRejectJson}",
        )


app = TestApp()
app.connect("127.0.0.1", port, 1002)
app.run()

