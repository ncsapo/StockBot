import discord
import os
from dotenv import load_dotenv
import StockFunctions

from requests.models import ContentDecodingError

def manage_input(input):
    space1 = input.find(" ")
    space2 = input.find(" ",space1+1)
    ticker = input[space1+1:space2]
    interval = input[space2+1:]
    print(f"Reading ticker as: {ticker}, Period as: {interval}")
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

    if message.content.startswith('$stock') or message.content.startswith('$s ') or message.content.startswith('$S '):
            input = message.content 
            ticker, period = manage_input(input)
            if check_valid_period(period):    
                StockFunctions.get_historical(ticker, period)
                f = open('stock.png','rb')
                picture = discord.File(f)
                await message.channel.send(file=picture)
            else:
                await message.channel.send("Please enter a valid period\n\nValid periods are 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max\n\nProper Format: $stock TickerSymbol Period\nExample: $stock tsla 5d")
           

            
load_dotenv('bot.env')
TOKEN=os.getenv('DISCORD_TOKEN')

client.run(TOKEN)