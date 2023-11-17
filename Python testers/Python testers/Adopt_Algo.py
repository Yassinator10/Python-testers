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

port = 7497

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        contract = Contract()
        contract.conId = 14894064
        contract.exchange = "SMART"
        
        order = Order()
        order.action = "BUY"
        order.totalQuantity = 8
        order.orderType = "MKT"
        order.lmtPrice = 3
        order.algoStrategy = "Adaptive"
        order.account = "DU2372888"

        order.algoParams = []
        order.algoParams.append(TagValue("adaptivePriority", "Normal"))
        #order.algoParams.append(TagValue("startTime", "20231018 15:15:00 US/Eastern"))
        #order.algoParams.append(TagValue("endTime", "20231018 15:30:00 US/Eastern"))
        #order.algoParams.append(TagValue("allowPastEndTime",int(0)))
        #order.algoParams.append(TagValue("noTakeLiq", int(0)))

        #order.algoParams.append(TagValue("monetaryValue", monetaryValue))
        time.sleep(2)
        self.placeOrder(orderId, contract, order)

        # def marketRule(self, marketRuleId: int, priceIncrements: ListOfPriceIncrements):
        #     print("Market Rule details: ", marketRuleId, priceIncrements)

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
            # f"orderState:{orderState}",
            # "\n",
            # f"Margin Values: \n",
            # f"initMarginBefore: {orderState.initMarginBefore}; initMarginAfter: {orderState.initMarginAfter};initMarginChange: {orderState.initMarginChange}; \n",
            # f"maintMarginBefore: {orderState.maintMarginBefore }; maintMarginAfter: {orderState.maintMarginAfter};maintMarginChange: {orderState.maintMarginChange}; \n",
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
            f"parentId:{parentId}",
            f"lastFillPrice:{lastFillPrice}",
        )
    
    def openOrderEnd(self):
        pass

app = TestApp()
app.connect("127.0.0.1", port, 1006)
app.run()
