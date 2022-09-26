#to get the stock detail using yahoo finance api
from time import strftime, time
import pyinputplus as pyip
import pandas as pd
import yfinance as yf
import datetime
from datetime import date,timedelta

name =  pyip.inputStr("Enter the name of the stock: ")
start_date = pyip.inputDate("Enter the Starting date(YYYY/MM/DD): ",)
end_date = pyip.inputDate("Enter the End date(YYYY/MM/DD): ",)
if end_date>date.today():
    print("Enter the End Date again we can't get the data of tomorrow: ")
    end_date = pyip.inputDate("Enter the end_date: ")
if start_date>end_date:
    print("Starting day can't be the day after End date: ")
    start_date = pyip.inputDate("Enter the Enddate: " )


dataval = yf.Ticker(f"{name}")
data = yf.download(name,start_date,end_date)
print(f"Data for the given {start_date} - {end_date} of time for the {name}")
print(data)
print("\nDetails of Max Volume traded in the given interval")
# col = "Volume"
val = data.loc[data["Volume"].idxmax()]
print(val)
print(f"\nQuarterly financial report of {name}\n",dataval.quarterly_financials)
