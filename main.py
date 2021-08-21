from os import name
import threading
import discord
from discord import embeds
from discord import client
from discord import role
from discord.colour import Color
from discord.ext import commands
from discord.utils import async_all
from pycoingecko import CoinGeckoAPI
import json
import datetime
import time 
from threading import Timer
from discord import utils
from discord.utils import get


#metodo para obtener los precios
def getprice():
    cg = CoinGeckoAPI()
    coinsprice = cg.get_price(ids='bitcoin, ethereum, dogecoin, tron, chainlink, tether, basic-attention-token, ripple, cardano, uniswap, binancecoin, monero, polkadot, litecoin, bitcoin-cash, pancakeswap-token,helmet-insure,1inch,belt,tokocrypto, stellar,ubix-network, vechain,theta-token, filecoin, usd-coin, wrapped-bitcoin, eos, bitcoin-cash-sv, iota, klay-token, solana, crypto-com-chain, cosmos, terra-luna, neo, smooth-love-potion, axie-infinity ', vs_currencies='usd', include_market_cap='true', include_24hr_vol='true')
    print(coinsprice)

    #Save the data in a Json file 
    with open ('data.json' ,'w') as file:
        json.dump(coinsprice, file, indent = 3)

    #Load data from Json file
    coinsfile = open ('data.json', 'r') 
    jsondata = coinsfile.read()
    #parser
    obj = json.loads(jsondata)
    threading.Timer(10,getprice).start()


def printtest():
    precios = getprice()
    print(precios)
    threading.Timer(10,printtest)

imprime = printtest()


#Discord bot 

bot = commands.Bot(command_prefix='>')




#events que nos indica cuando el bot esta activo via consola
@bot.event
async def on_ready():
    print('Bot activo')

#comando para agregar el rol automatico
@bot.event
async def on_member_join(ctx):
    autorole = discord.utils.get(ctx.guild.roles, name="cryptouser")
    await ctx.add_roles(autorole)



#comandos para solicitar precios
@bot.command()
async def comandos(ctx):
    embed = discord.Embed(title = f"{ctx.guild.name}", description="comandos para consultar las cotizaciones", timestamp=datetime.
    datetime.utcnow(), color=discord.Color.orange())
    embed.add_field(name="Consulta BTC", value=">preciobtc")
    embed.add_field(name="Consulta ETH", value=">precioeth")
    embed.add_field(name="Consulta DOG", value=">preciodoge")
    embed.add_field(name="Consulta TRX", value=">preciotrx")
    embed.add_field(name="Consulta Link", value=">preciochainlink")
    await ctx.send(embed=embed)

#command BTC price
@bot.command()
async def preciobtc(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #btc price from jason
       btc = obj['bitcoin']
       precioBtc = btc['usd']
       btcmktcap = btc['usd_market_cap']
       vol_hrs = btc['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del BTC {precioBtc} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.gold())
       embed.add_field(name="**Market cap**", value =btcmktcap)
       embed.add_field(name="**Vol last 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/1/small/bitcoin.png?1547033579")
       await ctx.send(embed=embed)

#ethreum price
@bot.command()
async def precioeth(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #ethreum price from jason
       eth = obj['ethereum']
       ethprice = eth['usd']
       ethmktcap = eth['usd_market_cap']
       vol_hrs = eth['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del Ethereum {ethprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
       embed.add_field(name="**Market cap**", value =ethmktcap)
       embed.add_field(name="**Vol last 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/279/small/ethereum.png?1595348880")
       await ctx.send(embed=embed)

#dogecoin price 

@bot.command()
async def preciodoge(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #tron price from jason
       doge = obj['dogecoin']
       dogeprice = doge['usd']
       dogemktcap = doge['usd_market_cap']
       vol_hrs = doge['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del Dogecoin {dogeprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_gold())
       embed.add_field(name="**Market cap**", value =dogemktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/5/small/dogecoin.png?1547792256")
       await ctx.send(embed=embed)

#tron price 

@bot.command()
async def preciotrx(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #btc price from jason
       trx = obj['tron']
       trxprice = trx['usd']
       trxmktcap = trx['usd_market_cap']
       vol_hrs = trx['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del TRX {trxprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
       embed.add_field(name="**Market cap**", value =trxmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/1094/small/tron-logo.png?1547035066")
       await ctx.send(embed=embed)

#precio Chainlink 

@bot.command()
async def preciochainlink(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #Chainlink price from jason
       link = obj['chainlink']
       linkprice = link['usd']
       linkmktcap = link['usd_market_cap']
       vol_hrs= link['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del Chainlink {linkprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
       embed.add_field(name="**Market cap**", value =linkmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/877/small/chainlink-new-logo.png?1547034700")
       await ctx.send(embed=embed)

#tether
@bot.command()
async def preciotether(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #theter price from jason
       tether = obj['tether']
       tetherprice = tether['usd']
       tethermktcap = tether['usd_market_cap']
       vol_hrs= tether['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Tether {tetherprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
       embed.add_field(name="**Market cap**", value =tethermktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/325/small/Tether-logo.png?1598003707")
       await ctx.send(embed=embed)


#Precio del Bat

@bot.command()
async def preciobat(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #bat price from jason
       bat= obj['basic-attention-token']
       batprice = bat['usd']
       batmktcap = bat['usd_market_cap']
       vol_hrs= bat['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del BAT  {batprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_red())
       embed.add_field(name="**Market cap**", value = batmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/677/small/basic-attention-token.png?1547034427")
       await ctx.send(embed=embed)


#Precio de ripple

@bot.command()
async def precioxrp(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #xrp price from jason
       xrp = obj['ripple']
       xrpprice = xrp['usd']
       xrpmktcap = xrp['usd_market_cap']
       vol_hrs= xrp['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del XRP {xrpprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
       embed.add_field(name="**Market cap**", value = xrpmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/44/small/xrp-symbol-white-128.png?1605778731")
       await ctx.send(embed=embed)

#precio cardano

@bot.command()
async def preciocardano(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #xrp price from jason
       car = obj['cardano']
       cardanoprice = car['usd']
       cardanomktcap = car['usd_market_cap']
       vol_hrs= car['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Cardano {cardanoprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
       embed.add_field(name="**Market cap**", value = cardanomktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/975/small/cardano.png?1547034860")
       await ctx.send(embed=embed)


#precio uniswap

@bot.command()
async def preciouniswap(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #uniswap price from json
       uni = obj['uniswap']
       uniswapprice = uni['usd']
       uniswapmktcap = uni['usd_market_cap']
       vol_hrs= uni['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Uniswap {uniswapprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.purple())
       embed.add_field(name="**Market cap**", value = uniswapmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/12504/small/uniswap-uni.png?1600306604")
       await ctx.send(embed=embed)

#precio binancecoin
@bot.command()
async def preciobnb(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #binancecoin price from json
       bnb = obj['binancecoin']
       bnbprice = bnb['usd']
       bnbmktcap = bnb['usd_market_cap']
       vol_hrs= bnb['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de BNB {bnbprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_gold())
       embed.add_field(name="**Market cap**", value = bnbmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/825/small/binance-coin-logo.png?1547034615")
       await ctx.send(embed=embed)


#precio monero
@bot.command()
async def preciomonero(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #monero price from json
       mon = obj['monero']
       moneroprice = mon['usd']
       moneromktcap = mon['usd_market_cap']
       vol_hrs= mon['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Monero {moneroprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.orange())
       embed.add_field(name="**Market cap**", value = moneromktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/69/small/monero_logo.png?1547033729")
       await ctx.send(embed=embed)


#precio polkadot
@bot.command()
async def preciopolkadot(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #polkadot price from json
       polka = obj['polkadot']
       polkaprice = polka['usd']
       polkamktcap = polka['usd_market_cap']
       vol_hrs= polka['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Polkadot {polkaprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_gray())
       embed.add_field(name="**Market cap**", value = polkamktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/12171/small/aJGBjJFU_400x400.jpg?1597804776")
       await ctx.send(embed=embed)


#precio litecoin
@bot.command()
async def preciolitecoin(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #litecoin price from json
       lite = obj['litecoin']
       liteprice = lite['usd']
       litemktcap = lite['usd_market_cap']
       vol_hrs= lite['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Litecoin {liteprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.light_grey())
       embed.add_field(name="**Market cap**", value = litemktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/2/small/litecoin.png?1547033580")
       await ctx.send(embed=embed)


#precio bitcoin-cash
@bot.command()
async def preciobch(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #bitcoin-cash price from json
       bch = obj['bitcoin-cash']
       bchprice = bch['usd']
       bchmktcap = bch['usd_market_cap']
       vol_hrs= bch['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Bitcoin Cash {bchprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
       embed.add_field(name="**Market cap**", value = bchmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/780/small/bitcoin-cash-circle.png?1594689492")
       await ctx.send(embed=embed)

#pancakeswap-token
@bot.command()
async def preciocake(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #bitcoin-cash price from json
       cake = obj['pancakeswap-token']
       cakeprice = cake['usd']
       cakemktcap = cake['usd_market_cap']
       vol_hrs= cake['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de pancakeswap-token   {cakeprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.magenta())
       embed.add_field(name="**Market cap**", value = cakemktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/12632/small/IMG_0440.PNG?1602654093")
       await ctx.send(embed=embed)


#helmet-insure
@bot.command()
async def preciohelmet(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #helmet-insure price from json
       helmet = obj['helmet-insure']
       helmetprice = helmet['usd']
       helmetmktcap = helmet['usd_market_cap']
       vol_hrs= helmet['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de helmet-insure  {helmetprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_gold())
       embed.add_field(name="**Market cap**", value = helmetmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/13680/small/ZMdK-1J4_400x400.png?1610834469")
       await ctx.send(embed=embed)


#1inch
@bot.command()
async def precio1inch(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #1inch price from json
       inch = obj['1inch']
       inchprice = inch['usd']
       inchmktcap = inch['usd_market_cap']
       vol_hrs= inch['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de 1inch {inchprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
       embed.add_field(name="**Market cap**", value = inchmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/13469/small/1inch-token.png?1608803028")
       await ctx.send(embed=embed)


#belt
@bot.command()
async def preciobelt(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #belt price from json
       belt = obj['belt']
       beltprice = belt['usd']
       beltmktcap = belt['usd_market_cap']
       vol_hrs= belt['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de belt {beltprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
       embed.add_field(name="**Market cap**", value = beltmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/14319/small/belt_logo.jpg?1615387083")
       await ctx.send(embed=embed)

#tokocrypto
@bot.command()
async def preciotko(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #belt price from json
       tko = obj['tokocrypto']
       tkoprice = tko['usd']
       tkomktcap = tko['usd_market_cap']
       vol_hrs= tko['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de tokocrypto {tkoprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_green())
       embed.add_field(name="**Market cap**", value = tkomktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/14577/small/tko-logo.png?1617093467")
       await ctx.send(embed=embed)

#UBX ubix-network
@bot.command()
async def precioubx(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #belt price from json
       ubx = obj['ubix-network']
       ubxprice = ubx['usd']
       ubxmktcap = ubx['usd_market_cap']
       vol_hrs= ubx['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Ubx {ubxprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_theme())
       embed.add_field(name="**Market cap**", value = ubxmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/13000/small/UBIX.png?1604281998?1617093467")
       await ctx.send(embed=embed)


#stellar price
@bot.command()
async def preciostellar(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #stellar price from json
       stl = obj['stellar']
       stlprice = stl['usd']
       stlmktcap = stl['usd_market_cap']
       vol_hrs= stl['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Stellar {stlprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.darker_grey())
       embed.add_field(name="**Market cap**", value = stlmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/100/small/Stellar_symbol_black_RGB.png?1552356157")
       await ctx.send(embed=embed)

#price vechain
@bot.command()
async def preciovechain(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #vechain price from json
       vech = obj['vechain']
       vechprice = vech['usd']
       vechmktcap = vech['usd_market_cap']
       vol_hrs= vech['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Vechain {vechprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
       embed.add_field(name="**Market cap**", value = vechmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/1167/small/VeChain-Logo-768x725.png?1547035194")
       await ctx.send(embed=embed)


#theta-token price
@bot.command()
async def preciotheta(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #theta-token price from json
       theta = obj['theta-token']
       thetaprice = theta['usd']
       thetamktcap = theta['usd_market_cap']
       vol_hrs= theta['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Theta {thetaprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
       embed.add_field(name="**Market cap**", value = thetamktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/2538/small/theta-token-logo.png?1548387191")
       await ctx.send(embed=embed)


#filecoin
@bot.command()
async def preciofilecoin(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #filecoin price from json
       file = obj['filecoin']
       fileprice = file['usd']
       filemktcap = file['usd_market_cap']
       vol_hrs= file['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Filecoin {fileprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
       embed.add_field(name="**Market cap**", value = filemktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/12817/small/filecoin.png?1602753933")
       await ctx.send(embed=embed)

#wrapped-bitcoin
@bot.command()
async def preciowbitcoin(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #wrapped-bitcoin price from json
       wbitcoin = obj['wrapped-bitcoin']
       wbitcoinprice = wbitcoin['usd']
       wbitcoinmktcap = wbitcoin['usd_market_cap']
       vol_hrs= wbitcoin['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de wrapped-bitcoin {wbitcoinprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.orange())
       embed.add_field(name="**Market cap**", value = wbitcoinmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/7598/small/wrapped_bitcoin_wbtc.png?1548822744")
       await ctx.send(embed=embed)


#eos
@bot.command()
async def precioeos(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #eos from json
       eoscoin = obj['eos']
       wbiteosprice = eoscoin['usd']
       wbiteosmktcap = eoscoin['usd_market_cap']
       vol_hrs= eoscoin['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Eos {wbiteosprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_gray())
       embed.add_field(name="**Market cap**", value = wbiteosmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/738/small/eos-eos-logo.png?1547034481")
       await ctx.send(embed=embed)


#bitcoin-cash-sv
@bot.command()
async def preciobsv(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #bsv from json
       bsvcoin = obj['bitcoin-cash-sv']
       bsvprice = bsvcoin['usd']
       bsvmktcap = bsvcoin['usd_market_cap']
       vol_hrs= bsvcoin['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Bsv {bsvprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.orange())
       embed.add_field(name="**Market cap**", value = bsvmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/6799/small/BSV.png?1558947902")
       await ctx.send(embed=embed)

#preciousdc
@bot.command()
async def preciousdc(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #USDC from json
       usdccoin = obj['usd-coin']
       usdcprice = usdccoin['usd']
       usdcmktcap = usdccoin['usd_market_cap']
       vol_hrs= usdccoin['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de USDC {usdcprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
       embed.add_field(name="**Market cap**", value = usdcmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/6319/small/USD_Coin_icon.png?1547042389")
       await ctx.send(embed=embed)


#precioiota
@bot.command()
async def precioiota(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #iota from json
       iotacoin = obj['iota']
       iotaprice = iotacoin['usd']
       iotamktcap = iotacoin['usd_market_cap']
       vol_hrs= iotacoin['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de IOTA {iotaprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_gray())
       embed.add_field(name="**Market cap**", value = iotamktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/692/small/IOTA_Swirl.png?1604238557")
       await ctx.send(embed=embed)


#precioklay-token
@bot.command()
async def precioklay(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #Klaytn  from json
       klaycoin = obj['klay-token']
       klayprice = klaycoin['usd']
       klaymktcap = klaycoin['usd_market_cap']
       vol_hrs= klaycoin['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Klaytn {klayprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_gray())
       embed.add_field(name="**Market cap**", value = klaymktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/9672/small/CjbT82vP_400x400.jpg?1570548320")
       await ctx.send(embed=embed)

#preciosolana
@bot.command()
async def preciosolana(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #solana  from json
       solcoin = obj['solana']
       solprice = solcoin['usd']
       solmktcap = solcoin['usd_market_cap']
       vol_hrs= solcoin['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Solana {solprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_purple())
       embed.add_field(name="**Market cap**", value = solmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/4128/small/coinmarketcap-solana-200.png?1616489452")
       await ctx.send(embed=embed)

#precio crypto-com-chain
@bot.command()
async def preciocro(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #crypto-com-chain  from json
       cryptocoin = obj['crypto-com-chain']
       cryptoprice = cryptocoin['usd']
       cryptomktcap = cryptocoin['usd_market_cap']
       vol_hrs= cryptocoin['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de crypto.com{cryptoprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
       embed.add_field(name="**Market cap**", value = cryptomktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/markets/images/589/large/crypto_com.jpg?1602499898")
       await ctx.send(embed=embed)

#precio cosmos
@bot.command()
async def precioatom(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #cosmos  from json
       cosmoscoin = obj['cosmos']
       cosmosprice = cosmoscoin['usd']
       cosmosmktcap = cosmoscoin['usd_market_cap']
       vol_hrs= cosmoscoin['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Cosmos{cosmosprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
       embed.add_field(name="**Market cap**", value = cosmosmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/1481/small/cosmos_hub.png?1555657960")
       await ctx.send(embed=embed)

#precio terra-luna
@bot.command()
async def precioterra(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #terra-luna  from json
       terracoin = obj['terra-luna']
       terraprice = terracoin['usd']
       terramktcap = terracoin['usd_market_cap']
       vol_hrs= terracoin['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Terra(Luna){terraprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
       embed.add_field(name="**Market cap**", value = terramktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/8284/small/luna1557227471663.png?1567147072")
       await ctx.send(embed=embed)


#precio neo
@bot.command()
async def precioneo(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #neo  from json
       neocoin = obj['neo']
       neoprice = neocoin['usd']
       neomktcap = neocoin['usd_market_cap']
       vol_hrs= neocoin['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Neo {neoprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
       embed.add_field(name="**Market cap**", value = neomktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/480/small/NEO_512_512.png?1594357361")
       await ctx.send(embed=embed)

#precio slp
@bot.command()
async def precioslp(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #slp  from json
       slpcoin = obj['smooth-love-potion']
       slpprice = slpcoin['usd']
       slpmktcap = slpcoin['usd_market_cap']
       vol_hrs= slpcoin['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de SLP {slpprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.purple())
       embed.add_field(name="**Market cap**", value = slpmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/10366/small/SLP.png?1578640057")
       await ctx.send(embed=embed)

#precio axs
@bot.command()
async def precioaxs(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #axs  from json
       axscoin = obj['axie-infinity']
       axsprice = axscoin['usd']
       axsmktcap = axscoin['usd_market_cap']
       vol_hrs= axscoin['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de AXS {axsprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
       embed.add_field(name="**Market cap**", value = axsmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morris**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/13029/small/axie_infinity_logo.png?1604471082")
       await ctx.send(embed=embed)


bot.run('ODMxMTg2MjQ3OTI0ODQyNTI3.YHRkhA.jf-u-GFzImrYlD8o-yzF6IJD7sU')