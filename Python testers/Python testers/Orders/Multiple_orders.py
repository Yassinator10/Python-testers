from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order
import threading
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
                
    def nextValidId(self, orderId):
        #super().nextValidId(orderId)
        self.nextValidOrderId = orderId
        #print("NextValidId:", orderId)    #remove the # if you'd also like nextvalidID to be printed in Python when reqIds(-1) is called  

def websocket_con():
    app.run()
    
app = TradingApp()      
app.connect("127.0.0.1", 7496, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

def Ticker(symbol,sec_type="STK",currency="USD",exchange="SMART"):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.currency = currency
    contract.exchange = exchange
    return contract 

def limitOrder(direction, quantity, lmt_price): #You can pass in an account number (account_num) here and use that as such order.account = account_num
    order = Order()
    order.action = direction
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = lmt_price
    order.account = 'DU2372889'
    order.tif = 'DAY'
    order.outsideRth = False
    return order

charpar = ")"
time.sleep(2)
print("")

#-=-=-=----=-=-=====-=-=-------=-=-=====-=-=-----=-=-=-=====--=-=-----========-=-=-----=-=-=-=====--=-=-----===

order_id = app.nextValidOrderId     
app.placeOrder(order_id, Ticker("TSLA"), limitOrder("BUY", 1, 170))
print("Order 1 - placed (with order ID = ", order_id, charpar)
print("")
time.sleep(.2)     


order_id+=1    
app.placeOrder(order_id, Ticker("AAPL"), limitOrder("BUY", 1, 165))        
print("Order 2 - placed (with order ID = ", order_id, charpar)    
print("")
time.sleep(.2)     

order_id+=1   
app.placeOrder(order_id, Ticker("A"), limitOrder("BUY", 1, 145))        
print("Order 3 - placed (with order ID = ", order_id, charpar)    
print("")