##Name: Bruno Suverza-Baek
##Date of Submission: 6-20-2021

##NOTE: To see plots, just uncomment all of the lines with just one '#'
## Any lines with '##' are to be interpreted as notes

## Run as python3 approximate_index.py [n] .DJI dow_jones_historical_prices.csv > approximation.csv

## Import necessary libraries
#import matplotlib.pyplot as plt
#from matplotlib import style
import pandas as pd
import argparse

## Parser arguments for the command line
parser = argparse.ArgumentParser()

parser.add_argument("securities",type=int)
parser.add_argument("index")
parser.add_argument("priceCSV")

args = parser.parse_args()

## Read csv inputted in the command line
df = pd.read_csv(args.priceCSV)

##Print Symbols and Weight columns in the output csv
print("Symbols","Weight",sep='\t')

if (args.index=='.DJI'):
	## Array of securities in order of output 
	symbol = ['AAPL','IBM','TRV','JPM','AXP','INTC','CAT','WBA','DIS','GS','JNJ','CVX','DOW','HD','KO','MCD',
		'NKE','V','PFE','VZ','WMT','MMM','PG','XOM','MRK','UTX','MSFT','CSCO','UNH','BA'
	]

	## Array of weights of securities in correspondence to their respective securities
	weight = [0.051810388,0.03587289,0.037519953,0.028578256,0.030755248,0.012771318,0.033408078,0.013886295,
		0.034473836,0.052223184,0.034820203,0.031257507,0.012822002,0.053476545,0.013123032,0.052802449,
		0.021843319,0.043763505,0.010358457,0.014849201,0.027714974,0.045693021,0.028772671,0.019370683,
		0.021151952,0.033982252,0.033822795,0.013801525,0.062191761,0.093082699
	]

	## Print symbols and respective weights to output csv
	for i in range(0,args.securities):
		print(symbol[i],"{:.7f}".format(weight[i]*100),sep='\t')

##  Create lists of prices for each security and main index
#	dji = list(df.loc[df['Symbol']=='.DJI'].iloc[:,2])
#	aapl = list(df.loc[df['Symbol']=='AAPL'].iloc[:,2])
#	axp = list(df.loc[df['Symbol']=='AXP'].iloc[:,2])
#	ba = list(df.loc[df['Symbol']=='BA'].iloc[:,2])
#	cat = list(df.loc[df['Symbol']=='CAT'].iloc[:,2])
#	csco = list(df.loc[df['Symbol']=='CSCO'].iloc[:,2])
#	cvx = list(df.loc[df['Symbol']=='CVX'].iloc[:,2])
#	dis = list(df.loc[df['Symbol']=='DIS'].iloc[:,2])
#	dow = list(df.loc[df['Symbol']=='DOW'].iloc[:,2])
#	gs = list(df.loc[df['Symbol']=='GS'].iloc[:,2])
#	hd = list(df.loc[df['Symbol']=='HD'].iloc[:,2])
#	ibm = list(df.loc[df['Symbol']=='IBM'].iloc[:,2])
#	intc = list(df.loc[df['Symbol']=='INTC'].iloc[:,2])
#	jnj = list(df.loc[df['Symbol']=='JNJ'].iloc[:,2])
#	jpm = list(df.loc[df['Symbol']=='JPM'].iloc[:,2])
#	ko = list(df.loc[df['Symbol']=='KO'].iloc[:,2])
#	mcd = list(df.loc[df['Symbol']=='MCD'].iloc[:,2])
#	mmm = list(df.loc[df['Symbol']=='MMM'].iloc[:,2])
#	mrk = list(df.loc[df['Symbol']=='MRK'].iloc[:,2])
#	msft = list(df.loc[df['Symbol']=='MSFT'].iloc[:,2])
#	nke = list(df.loc[df['Symbol']=='NKE'].iloc[:,2])
#	pfe = list(df.loc[df['Symbol']=='PFE'].iloc[:,2])
#	pg = list(df.loc[df['Symbol']=='PG'].iloc[:,2])
#	trv = list(df.loc[df['Symbol']=='TRV'].iloc[:,2])
#	unh = list(df.loc[df['Symbol']=='UNH'].iloc[:,2])
#	utx = list(df.loc[df['Symbol']=='UTX'].iloc[:,2])
#	v = list(df.loc[df['Symbol']=='V'].iloc[:,2])
#	vz = list(df.loc[df['Symbol']=='VZ'].iloc[:,2])
#	wba = list(df.loc[df['Symbol']=='WBA'].iloc[:,2])
#	wmt = list(df.loc[df['Symbol']=='WMT'].iloc[:,2])
#	xom = list(df.loc[df['Symbol']=='XOM'].iloc[:,2])

##  Create list of dates
#	date = df['Date'].tolist()
#	dates = list(set(date))
#	dates = sorted(dates)

##  Apply weights to their respective securities
#	for i in range(0,130):
#		aapl[i] *= 0.051810388
#		axp[i] *= 0.030755248
#		ba[i] *= 0.093082699
#		cat[i] *= 0.033408078
#		csco[i] *= 0.013801525
#		cvx[i] *= 0.031257507
#		dis[i] *= 0.034473836
#		dow[i] *= 0.012822002
#		gs[i] *= 0.052223184
#		hd[i] *= 0.053476545
#		ibm[i] *= 0.03587289
#		intc[i] *= 0.012771318
#		jnj[i] *= 0.034820203
#		jpm[i] *= 0.028578256
#		ko[i] *= 0.013123032
#		mcd[i] *= 0.052802449
#		mmm[i] *= 0.045693021
#		mrk[i] *= 0.021151952
#		msft[i] *= 0.033822795
#		nke[i] *= 0.021843319
#		pfe[i] *= 0.010358457
#		pg[i] *= 0.028772671
#		trv[i] *= 0.037519953
#		unh[i] *= 0.062191761
#		utx[i] *= 0.033982252
#		v[i] *= 0.043763505
#		vz[i] *= 0.014849201
#		wba[i] *= 0.013886295
#		wmt[i] *= 0.027714974
#		xom[i] *= 0.019370683

#	val = []

##  For each inputted [n], append summation of weighted securities to val array
#	if (args.securities==1):
#		for i in range(0,130):
#			val.append(aapl[i])
#	elif (args.securities==2):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i])
#	elif (args.securities==3):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i])
#	elif (args.securities==4):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i])
#	elif (args.securities==5):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i])
#	elif (args.securities==6):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i])
#	elif (args.securities==7):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i])
#	elif (args.securities==8):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i])
#	elif (args.securities==9):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i])
#	elif (args.securities==10):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i])
#	elif (args.securities==11):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i])
#	elif (args.securities==12):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i])
#	elif (args.securities==13):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i])
#	elif (args.securities==14):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i])
#	elif (args.securities==15):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i])
#	elif (args.securities==16):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i])
#	elif (args.securities==17):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i])
#	elif (args.securities==18):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i]+v[i])
#	elif (args.securities==19):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i]+v[i]+pfe[i])
#	elif (args.securities==20):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i]+v[i]+pfe[i]+vz[i])
#	elif (args.securities==21):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i]+v[i]+pfe[i]+vz[i]+wmt[i])
#	elif (args.securities==22):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i]+v[i]+pfe[i]+vz[i]+wmt[i]+mmm[i])
#	elif (args.securities==23):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i]+v[i]+pfe[i]+vz[i]+wmt[i]+mmm[i]+pg[i])
#	elif (args.securities==24):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i]+v[i]+pfe[i]+vz[i]+wmt[i]+mmm[i]+pg[i]
#				+xom[i])
#	elif (args.securities==25):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i]+v[i]+pfe[i]+vz[i]+wmt[i]+mmm[i]+pg[i]
#				+xom[i]+mrk[i])
#	elif (args.securities==26):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i]+v[i]+pfe[i]+vz[i]+wmt[i]+mmm[i]+pg[i]
#				+xom[i]+mrk[i]+utx[i])
#	elif (args.securities==27):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i]+v[i]+pfe[i]+vz[i]+wmt[i]+mmm[i]+pg[i]
#				+xom[i]+mrk[i]+utx[i]+msft[i])
#	elif (args.securities==28):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i]+v[i]+pfe[i]+vz[i]+wmt[i]+mmm[i]+pg[i]
#				+xom[i]+mrk[i]+utx[i]+msft[i]+csco[i])
#	elif (args.securities==29):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i]+v[i]+pfe[i]+vz[i]+wmt[i]+mmm[i]+pg[i]
#				+xom[i]+mrk[i]+utx[i]+msft[i]+csco[i]+unh[i])
#	elif (args.securities==30):
#		for i in range(0,130):
#			val.append(aapl[i]+ibm[i]+trv[i]+jpm[i]+axp[i]+intc[i]+cat[i]+wba[i]+dis[i]+gs[i]+jnj[i]
#				+cvx[i]+dow[i]+hd[i]+ko[i]+mcd[i]+nke[i]+v[i]+pfe[i]+vz[i]+wmt[i]+mmm[i]+pg[i]
#				+xom[i]+mrk[i]+utx[i]+msft[i]+csco[i]+unh[i]+ba[i])

##  Plot and display both approximation and main index arrays
#	style.use('ggplot')
#	fig = plt.figure()
#	ax = fig.add_subplot(111)

#	ax.plot(dates,val,color='blue',label='Approximation')
#	ax.set_xticks(ax.get_xticks()[::2])
#	ax.tick_params(axis='y',labelcolor='blue')

#	ax2 = ax.twinx()

#	ax2.plot(dates,dji,color='red',label='.DJI')
#	ax2.set_xticks(ax2.get_xticks()[::25])
#	ax2.tick_params(axis='y',labelcolor='red')

#	lns,labs = ax.get_legend_handles_labels()
#	lns2,labs2 = ax2.get_legend_handles_labels()
#	ax2.legend(lns+lns2,labs+labs2,loc=0)

#	plt.title(".DJI vs. Approximation")
#	plt.show()