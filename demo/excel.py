##############################################################################
#
# A simple example of converting a Pandas dataframe to an xlsx file using
# Pandas and XlsxWriter.
#
# Copyright 2013-2017, John McNamara, jmcnamara@cpan.org
#

# import pandas as pd
#
# df = pd.DataFrame({'Data11': [1011, "aasd", "22", 20, 15, 30, 45]})
#
# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('D:\pyproject\excel\pandas_simple.xlsx', engine='xlsxwriter')
#
# # Convert the dataframe to an XlsxWriter Excel object.
# # df.to_excel(writer, sheet_name='Sheet11')
# df.to_excel(writer)
# # Close the Pandas Excel writer and output the Excel file.
# writer.save()

import pandas as pd

df = pd.DataFrame({'Data11': [1011, "aasd", "22", 20, 15, 30, 45]})

writer = pd.ExcelWriter('D:\pyproject\excel\pandas_simple.xlsx', engine='xlsxwriter')

df.to_excel(writer)
writer.save()
