from ibapi.client import *
from ibapi.wrapper import *
from ibapi.tag_value import TagValue
from datetime import datetime
import time

port = 7496


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        print(f"nextValidId. orderId={orderId}")
        order_id = orderId

        mycontract = Contract()
        mycontract.symbol = "DIS"
        mycontract.secType = "STK"
        mycontract.currency = "USD"

        # Jefferies algo orders must be direct-routed to JEFFALGO
        mycontract.exchange = "JEFFALGO"

        o = Order()
        o.orderId = order_id
        o.action = "BUY"
        o.orderType = "MKT"
        # o.lmtPrice = 156.00
        o.totalQuantity = 1
        o.tif = "DAY"
        o.orderRef = "vwap_" + params[0] + "_" + str(order_id)
        o.algoStrategy = "Vwap"
        o.algoParams = params[1:]
        return o
        

        params_list = [
            [
                "s0127-10:45_e0127-11:45",
                TagValue("maxPctVol", 0.1),
                TagValue("startTime", "20220127-10:45:00 EST"),
                TagValue("endTime", "20220127-11:45:00 EST"),
                TagValue("allowPastEndTime", 0),
                TagValue("noTakeLiq", 1),
            ],
            [
                "s0128-10:45_e0128-11:45",
                TagValue("maxPctVol", 0.1),
                TagValue("startTime", "20220128-10:45:00 EST"),
                TagValue("endTime", "20220128-11:45:00 EST"),
                TagValue("allowPastEndTime", 0),
                TagValue("noTakeLiq", 1),
            ],
            [
                "sNULL_e0127-11:45",
                TagValue("maxPctVol", 0.1),
                TagValue("endTime", "20220127-11:45:00 EST"),
                TagValue("allowPastEndTime", 0),
                TagValue("noTakeLiq", 1),
            ],
            [
                "sNULL_e0128-11:45",
                TagValue("maxPctVol", 0.1),
                TagValue("endTime", "20220128-11:45:00 EST"),
                TagValue("allowPastEndTime", 0),
                TagValue("noTakeLiq", 1),
            ],
            [
                "sNULL_eNULL",
                TagValue("maxPctVol", 0.1),
                TagValue("allowPastEndTime", 0),
                TagValue("noTakeLiq", 1),
            ],
        ]

        def create_vwap_order(params):



        for p in params_list:
            temp = create_vwap_order(p)
            self.placeOrder(temp.orderId, mycontract, temp)
            order_id += 1
            time.sleep(1)

    def openOrder(
        self,
        orderId: OrderId,
        contract: Contract,
        order: Order,
        orderState: OrderState,
    ):
        print(
            datetime.now().strftime("%H:%M:%S.%f")[:-3],
            "openOrder.",
            f"orderId:{orderId}",
            f"contract:{contract}",
            f"order:{order}",
            # f"orderState:{orderState}",
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
            datetime.now().strftime("%H:%M:%S.%f")[:-3],
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
app.connect("127.0.0.1", port, 1001)
app.run()
