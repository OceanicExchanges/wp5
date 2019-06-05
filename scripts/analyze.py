#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import matplotlib.pyplot as plt

def to_timeser(df):
	#parse years
	raw_years = df['year'].str.split('_')
	years = []
	for year in raw_years:
		years.append(year[0])
	df['year'] = years
	df['year'] = pd.to_datetime(df['year'])
	df.set_index(['year'], drop=True, inplace=True)
	return df

def plot_timeline(df,column,filename,title=''):
	if not title:
		title = column
	ax = df[column].plot(legend=True)
	ax.set_title(title)
	plt.savefig(filename)
	plt.close()
	print('Saved plot to', filename)

def superimpose(df,column,filename,title=''):
	ax = df[column].plot(legend=True)
	if title:
		ax.set_title(title)
	plt.savefig(filename)
	print('Plot is open on', filename)

def to_decade(df):
	df = df.groupby((df.index.year//10)*10).mean().round(2)
	return df

def main(df):
	df = to_timeser(df)
	print('')
	print('Available concepts:', df.columns.to_list())
	print('')
	return df

if __name__== "__main__":
	try:
		filename = sys.argv[1]
		df = pd.read_csv(filename, sep='\t', skiprows=2)
	except:
		print('USAGE:')
		print('')
		print('python3 -i analyze.py <file.tsv>')
		sys.exit(0)
	df = main(df)
