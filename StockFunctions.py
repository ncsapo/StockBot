import finance as yf

def getHistorical(tickerSym):
    yf.Ticker(tickerSym)

getHistorical('PFE')
print('SF Finished')