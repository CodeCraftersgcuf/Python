import datetime
import time
from plyer import notification 
import yfinance as yf
msft=yf.Ticker("MSFT")
data= msft.info
notification.notify(
            title="Stock Market Notifier".format(datetime.date.today()),
            message="currentPrice={cp} \n regularMarketOpen={mo}\n regularMarketDayHigh={dh}\n regularMarketDayLow={dl}".format(
            cp=data["currentPrice"],
            mo=data["regularMarketOpen"],
            dh= data["regularMarketDayHigh"],
            dl=data["regularMarketDayLow"]
            ),
            timeout= 10
            )
time.sleep(10)
