import yfinance as yf
import matplotlib.pyplot as plt



def get_historical(tickerSym, period):
    #Get data
    if period in ['1d', '5d', '1mo']:
        stock =  yf.download(tickers=tickerSym, period=period, interval="15m")
    else:
        stock =  yf.download(tickers=tickerSym, period=period, interval="5d")
    #Convert to graphable formal
    #stock = stock.reset_index()
    #for i in ['Open', 'High', 'Close', 'Low']: 
    #    stock[i]  =  stock[i].astype('float64')
    #Graph and Save
    plt.clf()
    plt.title((tickerSym+" "+period).upper())
    plt.xlabel("Time/Date")
    plt.ylabel("Closing Price (USD)")
    plt.grid()
    stock['Adj Close'].plot()
    plt.savefig("stock.png")
    print(f"Graphed data for {tickerSym}")

#get_historical('tsla', '5d')

