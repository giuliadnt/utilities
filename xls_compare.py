#!/usr/bin/env python

__author__ = "Giulia Dnt"

"""
compare two dataframes and prints to excel the rows of df2 which differs from df1. 

df2 ==> xls report of the most recent test
df1 ==> xls report of the previous test

Python 2.7.13 :: Anaconda 4.3.1 (x86_64)
pandas 0.19.2
xlsxwriter 0.9.6

"""

import pandas as pd
from xlsxwriter.utility import xl_rowcol_to_cell

#use name of the reports you want to compare
df1 = pd.read_excel('report.xls')
df2 = pd.read_excel('report1.xls')

df = pd.merge(df1, df2, how='outer', indicator=True)
rows_in_df1_not_in_df2 = df[df['_merge']=='left_only'][df1.columns]
rows_in_df2_not_in_df1 = df[df['_merge']=='right_only'][df2.columns]

#cmd to overwrite default pandas header style
pd.formats.format.header_style = None

#initilize writer object
writer = pd.ExcelWriter('compare_tests_RBC.xls', engine='xlsxwriter')

rows_in_df2_not_in_df1.to_excel(writer, sheet_name="sheet_1", index=False)

workbook = writer.book

#styles
header_format = workbook.add_format({'font_name': 'Arial', 
									 'font_size': 10,
									 'bold': True,
									 'bg_color': 'yellow',
									 'left': 1,
									 'right': 1
									  })

odd_format = workbook.add_format({'bg_color':'silver',
								  'font_name': 'Arial',
								  'font_size': 10, 
								  'text_wrap': True,
								  'left': 1,
								  'right': 1
								   })

even_format = workbook.add_format({'bg_color': 'cyan',
								   'font_name': 'Arial',
								   'font_size': 10, 
								   'text_wrap': True,
								   'left': 1,
								   'right': 1
								   })
#worksheet.set_default_row(20)

worksheet = writer.sheets['sheet_1']

for row in range(0, len(rows_in_df2_not_in_df1)+1):
	if row%2 !=0:
		worksheet.set_row(row, None, odd_format)
	elif row%2 ==0 and row!=0:
		worksheet.set_row(row, None, even_format)
	elif row ==0:
		worksheet.set_row(row, None, header_format)

worksheet.set_column('A:C', 10)
worksheet.set_column('D:D', 20)
worksheet.set_column('E:E', 80)
worksheet.set_column('F:F', 45)

writer.save()

