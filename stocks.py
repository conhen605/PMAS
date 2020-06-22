# stocks.py
class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행':'A000100'}
    def GetCount(self):
        return len(self.stocks)
    def NameToCode(self, name):
        return self.stocks[name]

class Cptest:
    def __init__(self):
        self.stocks = {'삼성전자':'A000200'}
    def test(self):
        return 0
