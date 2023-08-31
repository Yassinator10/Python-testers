# Import libraries
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import pandas as pd
import threading
import time
tickers = ["NQ",]
class TradeApp(EWrapper, EClient): 
    def __init__(self): 
        EClient.__init__(self, self) 
        self.data = {}
    def historicalData(self, reqId, bar):
        if tickers[reqId] not in self.data:
            self.data[tickers[reqId]] = [{"Date":bar.date,"Open":bar.open,"High":bar.high,"Low":bar.low,"Close":bar.close,"Volume":bar.volume}]
        else:
            self.data[tickers[reqId]].append({"Date":bar.date,"Open":bar.open,"High":bar.high,"Low":bar.low,"Close":bar.close,"Volume":bar.volume})
        print("reqID:{}, date:{}, open:{}, high:{}, low:{}, close:{}, volume:{}".format(reqId,bar.date,bar.open,bar.high,bar.low,bar.close,bar.volume))
    def historicalDataEnd(self, reqId, start, end):
        super().historicalDataEnd(reqId, start, end)
        print("HistoricalDataEnd. ReqId:", reqId, "from", start, "to", end)
        self.data[tickers[reqId]] = pd.DataFrame(self.data[tickers[reqId]])
        self.data[tickers[reqId]].set_index("Date",inplace=True)
        event.set()
def usFut(symbol,expiry,sec_type="FUT",currency="USD",exchange="CME"):
    contract = Contract()
    contract.symbol = "NQ"
    contract.secType = sec_type
    contract.currency = currency
    contract.exchange = exchange
    contract.lastTradeDateOrContractMonth = expiry
    contract.includeExpired = True 
    return contract 
def histData(req_num,contract,duration,candle_size):
    #app.reqMarketDataType(3) 
    app.reqHistoricalData(reqId=req_num, 
                          contract=contract,
                          endDateTime='20220928 23:59:59',
                          durationStr=duration,
                          barSizeSetting=candle_size,
                          whatToShow='TRADES',
                          useRTH=1,
                          formatDate=1,
                          keepUpToDate=0,
                          chartOptions=[])   # EClient function to request contract details
def websocket_con():
    app.run()
app = TradeApp()
app.connect(host='127.0.0.1', port=7496, clientId=23) #port 4002 for ib gateway paper trading/7497 for TWS paper trading
con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) # some latency added to ensure that the connection is established
event = threading.Event()
for ticker in tickers:
    event.clear()
    histData(tickers.index(ticker),usFut(ticker,"202209"),'20 D', '1 day')
    event.wait()
#extract and store historical data in dataframe
historicalData = app.data