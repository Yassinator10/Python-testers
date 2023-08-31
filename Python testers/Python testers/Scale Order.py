from ibapi.client import *
from ibapi.wrapper import *
from ibapi.contract import Contract
from ibapi.order import Order
import threading
import time

port = 7496

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
app.connect("127.0.0.1", port, clientId=101)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

def Ticker(symbol,sec_type="STK",currency="USD",exchange="SMART"):
    contract = Contract()
    contract.symbol = "AAPL"
    contract.exchange = exchange
    contract.secType = sec_type
    contract.currency = currency
    contract.primaryExchange = "ISLAND"
    return contract 

def scaleOrder(direction,quantity,lmt_price):
    order = Order()
    order.action = direction
    order.orderType = "LMT"        
    order.totalQuantity = quantity
    order.lmtPrice = lmt_price
    #order.transmit = False
    #order.outsideRth = True
    order.tif = 'DAY'
    
    #MAIN
    order.scaleInitLevelSize  = 2000  
    order.scaleSubsLevelSize  = 500   #optional - After the initial fill of 2,000 shares switch to quantity = 500
    order.scalePriceIncrement = .05   #must be > 0
    order.scaleRandomPercent = False
    
    #AUTO PRICE ADJUSTMENT
    #order.scalePriceAdjustValue = .2 
    #order.scalePriceAdjustInterval = 1   
    
    #PROFIT TAKER
    order.scaleProfitOffset = 2  
    order.scaleAutoReset = False  
    #order.scaleInitPosition = 2000   #seems optional
    #order.scaleInitFillQty = 200     #seems optional
    
    #order.scaleTable = ""
    
    
    """
    MAIN
    order.scaleInitLevelSize        # type: int - Defines the size of the first, or initial, order component
    order.scaleSubsLevelSize        # type: int - Defines the order size of the subsequent scale order components
    order.scalePriceIncrement       # type: float - Defines the price increment between scale components 
    order.scaleRandomPercent        # type: boolean - Defines the random percent by which to adjust the position

    AUTO PRICE ADJUSTMENT 
    order.scalePriceAdjustValue     # type: float - Modifies the value of the Scale order
    order.scalePriceAdjustInterval  # type: int - Specifies the interval when the price is adjusted
    
    PROFIT ORDERS
    order.scaleProfitOffset         # type: float - Specifies the offset when to adjust profit
    order.scaleAutoReset            # type: boolean - Restarts the Scale series if the order is cancelled
    order.scaleInitPosition         # type: int - The initial position of the Scale order
    order.scaleInitFillQty          # type: int - Specifies the initial quantity to be filled
    order.scaleTable = ""
    
    Sample code (paths):
    C:\TWS API\samples\Python\Testbed\AvailableAlgoParams.py
    C:\TWS API\samples\Python\Testbed\Program.py
    C:\TWS API\source\pythonclient\ibapi\client.py
    
    Documentation:
    All Scale Order parameters - https://interactivebrokers.github.io/tws-api/classIBApi_1_1Order.html#a0ffd872cdcb1cd30f873a0883d48fdd5  or C:\TWS API\samples\Python\Testbed\AvailableAlgoParams.py
    Nicer scale trader examples TWS - https://ibkrguides.com/tws/usersguidebook/algos/basic_scale_orders.htm 
    
    2 paths in TWS to confirm the order(s) was set-up properly once submitted to TWS:
     TWS > Orders Window > choose the Settings wheel (top-right corner of the Orders Window) > Settings > look right under “Available Columns” > expand “Scale Orders” section > double-click to add each field > should now be reflected in the Orders Window 
     TWS > Orders Window > right-click on the scale order > choose: View Scale Progress > should show details of the Scale order (if that option is NOT shown TWS may not be acknowledging this is a “scale” order) 
     
    """

    return order

time.sleep(3)
order_id = 121212#app.nextValidOrderId          

app.placeOrder(order_id,Ticker(""),scaleOrder("BUY", 25000, 174))



