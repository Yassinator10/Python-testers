from ibapi.client import *
from ibapi.wrapper import *
from ibapi.contract import *
import time

port = 7496

class TestApp(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        self.reqPositions()

    def position(self, account: str, contract: Contract, position: Decimal, avgCost: float):
        print(account, contract, position, avgCost)

    
app = TestApp()
app.connect('127.0.0.1', port, 0)
app.run()