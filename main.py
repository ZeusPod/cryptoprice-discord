import discord
from discord.colour import Color
from discord.ext import commands
from pycoingecko import CoinGeckoAPI
import json
import datetime
import time 

cg = CoinGeckoAPI()
#get price for coins from api
price_bitcoin = []
price_bitcoin = cg.get_price(ids=["Bitcoin", "ethereum", "Dogecoin"], vs_currencies="usd")

#Save the data in a Json file 
with open ('data.json' ,'w') as file:
    json.dump(price_bitcoin, file, indent = 3)

#Load data from Json file
coinsfile = open ('data.json', 'r') 
jsondata = coinsfile.read()
#parser
obj = json.loads(jsondata)

#btc price 
btc = obj['bitcoin']
btcprice = btc['usd'] 

#ethereum price 
eth = obj['ethereum']
ethprice = eth['usd'] 

#dogecoin price 
doge = obj['dogecoin']
dogeprice = doge['usd'] 




bot = commands.Bot(command_prefix='>')

#events
@bot.event
async def on_ready():
    print('Bot activo')

#command BTC price
@bot.command()
async def preciobtc(ctx):
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del BTC {btcprice}**", timestamp=datetime.datetime.utcnow(), Color=discord.Color.blue())
       embed.add_field(name="Price Font", value="Powered by Coingeicko")
       embed.add_field(name="Dev", value="Jose Morales")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/1/small/bitcoin.png?1547033579")
       await ctx.send(embed=embed)

#command ethereum price 
@bot.command()
async def precioeth(ctx):
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del ETH {ethprice}**", timestamp=datetime.datetime.utcnow(), Color=discord.Color.blue())
       embed.add_field(name="Price Font", value="Powered by Coingeicko")
       embed.add_field(name="Dev", value="Jose Morales")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/279/small/ethereum.png?1595348880")
       await ctx.send(embed=embed)

#command dogecoin price 
@bot.command()
async def preciodogecoin(ctx):
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Dogecoin {dogeprice}**", timestamp=datetime.datetime.utcnow(), Color=discord.Color.blue())
       embed.add_field(name="Price Font", value="Powered by Coingeicko")
       embed.add_field(name="Dev", value="Jose Morales")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/5/small/dogecoin.png?1547792256")
       await ctx.send(embed=embed)


bot.run('ODMxMTg2MjQ3OTI0ODQyNTI3.YHRkhA.jf-u-GFzImrYlD8o-yzF6IJD7sU')