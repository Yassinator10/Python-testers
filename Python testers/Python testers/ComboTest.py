from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.contract import ComboLeg
import threading
import time

global Bid, Ask
Bid = []
Ask = []

class TradeApp(EWrapper, EClient): 
    def __init__(self): 
        EClient.__init__(self, self) 

    def tickPrice(self, reqId, tickType, price, attrib):
        super().tickPrice(reqId, tickType, price, attrib)
        #print("TickPrice. TickerId:", reqId, "tickType:", tickType, "Price:", price)
        if tickType == 1:
            print("Bid = ", price)
            Bid.append(price)
        if tickType == 2:
            print("Ask = ", price)
            Ask.append(price)
            print("")
            #print("TickPrice. TickerId:", reqId, "tickType:", tickType, "Price:", price)
            #print(ticker, "52 week high = ", price)

    def tickSize(self, reqId, tickType, size):
        super().tickSize(reqId, tickType, size)
       
        
def comboOptContract(symbol,action,sec_type="BAG",currency="USD",exchange="SMART"):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.currency = currency
    contract.exchange = exchange

    leg1 = ComboLeg()
    leg1.conId =645411168 #642872552
    leg1.ratio = 1
    leg1.action = "BUY"
    leg1.exchange = "CME"
    
    leg2 = ComboLeg()
    leg2.conId = 645410287 #642872926
    leg2.ratio = 1
    leg2.action = "BUY"
    leg2.exchange = "CME"
  
    contract.comboLegs = []
    contract.comboLegs.append(leg1)
    contract.comboLegs.append(leg2)
    return contract

def streamSnapshotData(req_num,contract):
    """stream tick leve data"""
    app.reqMarketDataType(1)
    app.reqMktData(reqId=req_num, 
                   contract=contract,
                   genericTickList="",
                   snapshot=False,
                   regulatorySnapshot=False,
                   mktDataOptions=[])
    
def websocket_con():
    app.run()

app = TradeApp()
app.connect(host='127.0.0.1', port=7496, clientId=2) #port 4002 for ib gateway paper trading/7497 for TWS paper trading
time.sleep(2)
con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()

tickers = ["NQ"]
for ticker in tickers:
    streamSnapshotData(tickers.index(ticker),comboOptContract(ticker,"BUY"))
    time.sleep(2)
    
time.sleep(5) 
    
"""
Bid1 =  Bid[0]
Ask1 =  Ask[0] 

print("Bid = ",Bid1)
print("Ask = ", Ask1)
"""

"""
app.disconnect()
"""