from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from datetime import datetime
import threading
import time
import pandas as pd

tickers = ["AAPL","A","TSLA"]

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def contractDetails(self, reqId, contractDetails):
        #print("Symbol =", contractDetails.contract.symbol)
        print("Local symbol =", contractDetails.contract.localSymbol)
        print("CONID =", contractDetails.contract.conId)
        print("Expiration =", contractDetails.contract.lastTradeDateOrContractMonth)
        print("TradingClass = ", contractDetails.contract.tradingClass)
        print("")
                   
  
def websocket_con():
    app.run()
 
app = TradingApp()      
app.connect("127.0.0.1", 7496, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

contract_event = threading.Event()
print("")

def Ticker(symbol,sec_type="STK",currency="USD",exchange="SMART"):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.currency = currency
    contract.exchange = exchange
    #contract.includeExpired = True
    #contract.lastTradeDateOrContractMonth = "202311"
    return contract 

for ticker in tickers:
    contract_event.clear() 
    app.reqContractDetails(tickers.index(ticker), Ticker(ticker)) 
    #contract_event.wait() 
    #app.disconnect()