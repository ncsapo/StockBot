import yfinance
import matplotlib.pyplot as plt

# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
def getHistorical(tickerSym, start, end):
    tickerData = yfinance.download(tickerSym, start=start, end=end)
    tickerData['High'].plot()

    plt.xlabel("Date")
    plt.ylabel("High")
    plt.title("Microsoft Price Data")
    plt.grid()
    #plt.show()
    plt.savefig('graph.png')


    


getHistorical('MSFT', '2021-2-10', '2021-2-25')

print('SF Finished')