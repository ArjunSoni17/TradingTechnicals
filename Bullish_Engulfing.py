import alpaca_trade_api as tradeapi
import requests
import time
import numpy as np
from datetime import datetime, timedelta
from pytz import timezone
import datetime
from datetime import date
import re
import os
import csv
import sys
import holidays

api = tradeapi.REST(
    key_id='xxxxxxxxxx',
    secret_key='xxxxxxxxxxxxxx',
    base_url='XXXXXXXXX'
)

def nexttime(x):
    us_holidays = holidays.US() #.keys()
    x = x + datetime.timedelta(days=1)
    if x.weekday() <=4 and x  not in us_holidays :
        return x
    elif x.weekday() >4 or x in us_holidays:
        x = x + datetime.timedelta(days=1)

        if x.weekday() <=4 and x  not in us_holidays :
            return x
        elif x.weekday() >4 or x in us_holidays:
            x = x + datetime.timedelta(days=1)
            if x.weekday() <=4 and x  not in us_holidays:
                return x
            elif x.weekday()>4 or x in us_holidays:
                x = x + datetime.timedelta(days=1)
                return x



def time(x):
    us_holidays = holidays.US() #.keys()
    if x.weekday() <=4 and x  not in us_holidays :
        return x
    elif x.weekday() >4 or x in us_holidays:
        x = x - datetime.timedelta(days=1)

        if x.weekday() <=4 and x  not in us_holidays :
            return x
        elif x.weekday() >4 or x in us_holidays:
            x = x - datetime.timedelta(days=1)
            if x.weekday() <=4 and x  not in us_holidays:
                return x
            elif x.weekday()>4 or x in us_holidays:
                x = x - datetime.timedelta(days=1)
                return x
my_list_verygood=[]   
list_lowergood=[]           
list_uppergood=[]   
list_mediumengulfing=[] 
list_justengulfing=[]   
total=0
currentdate = input("Please enter todays date in the format yyyy-mm-dd: ")
year,month,day = currentdate.split('-')
day1 = date(int(year),int(month),int(day))
t1= day1
t1=time(t1)
print(t1)
t2= t1 - datetime.timedelta(days=1)
t2=time(t2)
print(t2)
t3= t2 - datetime.timedelta(days=1)
t3=time(t3)
print(t3)
t4= t3 - datetime.timedelta(days=1)
t4=time(t4)
print(t4)
t5= t4 - datetime.timedelta(days=1)
t5=time(t5)
print(t5)



y=["A","AAL","AAP","AAPL","ABBV","ABC","ABMD","ABT","ACMR","ACN","ADBE","ADI","ADM","ADP","ADSK","AEE","AEP","AES","AFL","AIG","AIV","AIZ","AJG","AKAM","ALB","ALGN","ALK","ALL","ALLE","ALXN","AMAT","AMCR","AMD","AME","AMGN","AMP","AMT","AMZN","ANET","ANSS","ANTM","AON","AOS","APA","APD","APH","APT","APTV","ARE","ATO","ATVI","AU","AVB","AVGO","AVY","AWK","AXP","AZO","BA","BAC","BAM","BAX","BBY","BDX","BEN","BF.B","BIDU","BIG","BIIB","BILI","BIO","BK","BKNG","BKR","BLDP","BLK","BLL","BMY","BR","BRK.B","BSX","BWA","BXP","BYND","C","CAG","CAH","CAKE","CAR","CARR","CAT","CB","CBOE","CBRE","CCI","CCL","CDE","CDLX","CDNS","CDW","CE","CERN","CF","CFG","CGC","CHD","CHEF","CHGG","CHRW","CHTR","CI","CINF","CL","CLX","CMA","CMCSA","CME","CMG","CMI","CMS","CNC","CNP","CODX","COF","COG","COO","COP","COST","COTY","CPB","CPRT","CRM","CRON","CRWD","CSCO","CSX","CTAS","CTL","CTSH","CTVA","CTXS","CVS","CVX","CXO","D","DAL","DD","DDOG","DE","DENN","DFS","DG","DGX","DHI","DHR","DIS","DISCA","DISCK","DISH","DKNG","DLR","DLTR","DOV","DOW","DPZ","DRD","DRE","DRI","DTE","DUK","DUST","DVA","DVN","DXC","DXCM","EA","EAT","EBAY","ECL","ED","EFX","EIX","EL","EMN","EMR","EOG","EQIX","EQR","ERI","ES","ESS","ETFC","ETN","ETR","ETSY","EVRG","EW","EXC","EXPD","EXPE","EXR","F","FANG","FAS","FAST","FB","FBHS","FCX","FDX","FE","FFIV","FIS","FISV","FITB","FLIR","FLS","FLT","FMC","FOX","FOXA","FRC","FRT","FSLY","FTI","FTNT","FTV","GD","GE","GILD","GIS","GL","GLUU","GLW","GM","GOL","GOLD","GOOG","GOOGL","GPC","GPN","GPS","GRMN","GS","GWW","HA","HAL","HAS","HBAN","HBI","HCA","HD","HES","HFC","HIG","HII","HLT","HOLX","HON","HPE","HPQ","HRB","HRL","HSIC","HST","HSY","HUM","HWM","IBM","ICE","IDXX","IEX","IFF","ILMN","IMAX","INCY","INFO","INO","INTC","INTU","IP","IPG","IPGP","IQV","IR","IRM","ISRG","IT","ITW","IVZ","J","JBHT","JCI","JKHY","JMIA","JNJ","JNPR","JPM","K","KEY","KEYS","KHC","KIM","KLAC","KMB","KMI","KMX","KO","KR","KSS","KSU","L","LAKE","LB","LDOS","LEG","LEN","LH","LHX","LIN","LK","LKQ","LLY","LMT","LNC","LNT","LOW","LRCX","LUV","LVS","LW","LX","LYB","LYV","M","MA","MAA","MAR","MAS","MAXR","MCD","MCHP","MCK","MCO","MDLZ","MDT","MET","MGM","MHK","MKC","MKTX","MLM","MMC","MMM","MNK","MNST","MO","MOS","MPC","MRK","MRNA","MRO","MS","MSCI","MSFT","MSI","MTB","MTCH","MTD","MU","MXIM","MYL","NBL","NCLH","NDAQ","NEE","NEM","NET","NFLX","NI","NIO","NKE","NLOK","NLSN","NOC","NOV","NOW","NRG","NSC","NTAP","NTRS","NUE","NUGT","NVAX","NVDA","NVR","NWL","NWS","NWSA","O","ODFL","OKE","OMC","OMI","ORCL","ORLY","OTIS","OXY","PAAS","PAYC","PAYX","PBCT","PCAR","PDD","PEAK","PEG","PENN","PEP","PFE","PFG","PG","PGR","PH","PHM","PINS","PKG","PKI","PLD","PM","PNC","PNR","PNW","PPG","PPL","PRGO","PRU","PSA","PSX","PTON","PVH","PWR","PXD","PYPL","QCOM","QRVO","RCL","RE","REG","REGN","RF","RH","RHI","RJF","RL","RMD","ROK","ROKU","ROL","ROP","ROST","RSG","RTX","SAVE","SBAC","SBGL","SBUX","SCHW","SDC","SE","SEE","SHAK","SHW","SIVB","SJM","SLB","SLG","SNA","SNAP","SNPS","SO","SOXS","SPCE","SPG","SPGI","SQ","SRE","SRNE","SSRM","STE","STLD","STT","STX","STZ","SWK","SWKS","SYF","SYK","SYY","T","TAP","TDG","TDOC","TDY","TEL","TER","TEVA","TFC","TFX","TGT","TIF","TJX","TLRY","TMO","TMUS","TPR","TQQQ","TROW","TRV","TSCO","TSLA","TSM","TSN","TT","TTWO","TUP","TWLO","TWTR","TXN","TXT","TYL","TZA","UA","UAA","UAL","UBER","UDR","UHS","ULTA","UNH","UNM","UNP","UPS","URI","USB","V","VAR","VFC","VIAC","VLO","VMC","VNO","VRSK","VRSN","VRTX","VTR","VXX","VZ","W","WAB","WAT","WBA","WDC","WEC","WELL","WFC","WHR","WKHS","WLTW","WM","WMB","WMT","WORK","WPM","WRB","WRK","WST","WU","WY","WYND","WYNN","XEL","XLNX","XLU","XOM","XRAY","XRX","XYL","YUM","ZBH","ZBRA","ZION","ZM","ZS","ZTS"]
for smbl in y:
    tick=0
    qnty=3500
    buy_deno=.5# in %
    sell_deno=.2 # in %

    barset = api.get_barset(smbl, '1D', limit=10)
    aapl_bars = barset[smbl]
    
    for i in aapl_bars :
        
        result = i.c,i.h,i.l,i.o,i.v,i.t.date(),smbl
        if t1 == i.t.date() :
            
            h1,l1,c1,o1 = i.h,i.l,i.c,i.o
            if i.c > i.o :
                Candle1="Green"
            elif i.c < i.o :
                Candle1="Red"
            elif i.c == i.o :
                Candle1="white"
        if t2 == i.t.date() :
            h2,l2,c2,o2 = i.h,i.l,i.c,i.o
            if i.c > i.o :
                Candle2="Green"
            elif i.c < i.o :
                Candle2="Red"
            elif i.c == i.o :
                pass
        if t3 == i.t.date() :
            h3,l3,c3,o3 = i.h,i.l,i.c,i.o
            if i.c > i.o :
                Candle3="Green"
            elif i.c < i.o :
                Candle3="Red"
            elif i.c == i.o :
                pass
        if t4 == i.t.date() :
            h4,l4,c4,o4 = i.h,i.l,i.c,i.o
            if i.c > i.o :
                Candle4="Green"
            elif i.c < i.o :
                Candle4="Red"
            elif i.c == i.o :
                pass
        if t5 == i.t.date() :
            h5,l5,c5,o5 = i.h,i.l,i.c,i.o
            if i.c > i.o :
                Candle5="Green"
            elif i.c < i.o :
                Candle5="Red"
            elif i.c == i.o :
                pass
        
    if  o1<c2 and o2<c1 and Candle1== "Green" and Candle2=="Red":
        print("------------------------------------Bullish engulfing on ",t1,smbl,h1,t2,smbl,h2)
        print("o1-c2=",(o1-c2))

        percantage1=-(((o1-c2)/o1)*100)
        print("percentage=",percantage1)

        print("o2-c1=",(o2-c1))
        percentage2=-(((o2-c1)/o2)*100)
        print("percentage=",percentage2)
        
        if percantage1>=1.1 and percentage2>=1.1:
            print("this engulfing is among verygood engulfings",smbl)
            my_list_verygood.append(smbl)   

        elif percantage1>=1.1 and percentage2<1.1:
            print("Lower part good engulfing  ",smbl)
            list_lowergood.append(smbl) 
        elif percentage2>=1.1 and percantage1<1.1:
            print("upper part good engulfing  ",smbl)
            list_uppergood.append(smbl)   
        elif (percantage1>=0.1 and percantage1 <1.1) or (percentage2>=0.1 and percentage2<1.1):
            print("Medium engulfing",smbl)
            list_mediumengulfing.append(smbl) 
        elif percantage1<0.1 and percentage2<0.1:
            print("just engulfing",smbl)
            list_justengulfing.append(smbl)  
    else:
        pass
    

print(my_list_verygood)
print(list_lowergood)
print(list_uppergood)  
print(list_mediumengulfing) 
print(list_justengulfing)


    