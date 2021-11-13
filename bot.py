import discord
import os
from dotenv import load_dotenv
import StockFunctions

from requests.models import ContentDecodingError


def manage_input(input, to_return):
    if to_return == 1:
        input = input+" "
    space1 = input.find(" ")
    space2 = input.find(" ",space1+1)
    ticker = input[space1+1:space2]
    interval = input[space2+1:]
    print(f"Reading ticker as: {ticker}, Period as: {interval}")
    if to_return == 1:
        return ticker
    elif to_return == 2:
        return ticker, interval

def check_valid_period(input):
    if input in ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']:
        return True
    else:
        return False

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    input = message.content

    if message.content.startswith('$help'):
        embedMes = discord.Embed(title="StockBot Help Message", description="Here is what you can do with StockBot:", color=0x020e96)
        embedMes.add_field(name="Get Stock Historical Data: $stock ticker period", value="This with return a graph of the historical data of a valid ticker\nAlternatives: $s, $S\nExample: $stock TSLA 1mo", inline=False)
        embedMes.add_field(name="Get Recent Recommendations: $recommendations ticker", value="This with return the 5 most recent companies and their recommendations\nAlternatives: $r, $R\nExample: $recommendations MSFT", inline=False)
        await message.channel.send(embed=embedMes)

    if message.content.startswith('$stock') or message.content.startswith('$s ') or message.content.startswith('$S '): 
        ticker, period = manage_input(input, 2)
        if check_valid_period(period):    
            StockFunctions.get_historical(ticker, period)
            f = open('stock.png','rb')
            picture = discord.File(f)
            await message.channel.send(file=picture)
        else:
            await message.channel.send("Please enter a valid period\n\nValid periods are 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max\n\nProper Format: $stock TickerSymbol Period\nExample: $stock tsla 5d")
        
    if message.content.startswith('$recommendations') or message.content.startswith('$r ') or message.content.startswith('$R '):
        ticker = manage_input(input, 1)
        print(f"ticker is {ticker}")
        recs = StockFunctions.get_recommendations(ticker)
        embedMes = discord.Embed(title="Stock Recommendations", description="Top 5 Most Recent Recommendations", color=0x020e96)
        for company in recs:
            embedMes.add_field(name=company[0], value=company[1], inline=False)
        await message.channel.send(embed=embedMes)

            
load_dotenv('bot.env')
TOKEN=os.getenv('DISCORD_TOKEN')

client.run(TOKEN)