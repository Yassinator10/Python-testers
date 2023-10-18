from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.contract import ComboLeg
from ibapi.order import Order
from ibapi.tag_value import TagValue
import threading
import time

CONID1 = 495512552
CONID2 = 533620665

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
                
    def nextValidId(self, orderId):
        super().nextValidId(orderId)
        self.nextValidOrderId = orderId
        print("NextValidId:", orderId)

def websocket_con():
    app.run()
    
app = TradingApp()      
app.connect("127.0.0.1", 7496, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

def comboFutContract(symbol,conID,action,sec_type="BAG",currency="USD",exchange="SMART"):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.currency = currency
    contract.exchange = exchange

    leg1 = ComboLeg()
    leg1.conId = CONID1 
    leg1.ratio = 1
    leg1.action = "BUY"
    leg1.exchange = "CME"
    
    leg2 = ComboLeg()
    leg2.conId = CONID2 
    leg2.ratio = 1
    leg2.action = "BUY"
    leg2.exchange = "CME"
  
    contract.comboLegs = []
    contract.comboLegs.append(leg1)
    contract.comboLegs.append(leg2)
    return contract

    
def limitOrder(direction,quantity,lmt_price):
    order = Order()
    order.action = direction
    order.orderType = "REL + LMT"
    order.totalQuantity = quantity
    order.lmtPrice = lmt_price
    #order.account = "DU2372888"
    #order.auxPrice = .02
    
    order.smartComboRoutingParams = []
    order.smartComboRoutingParams.append(TagValue("NonGuaranteed", "1"))
    return order

order_id = app.nextValidOrderId
app.placeOrder(order_id,comboFutContract("ES",[CONID1,CONID2],["BUY","BUY"]),limitOrder("BUY",1,4500)) 
time.sleep(5)