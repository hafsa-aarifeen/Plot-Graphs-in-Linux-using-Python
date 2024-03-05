from openpyxl.chart import LineChart, Reference
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

input_file = input("Enter the path to your CSV file: ")
output_file = input("Enter the desired output filename (including .xlsx): ")
chart_title = input("Enter your desired chart title: ")

data = pd.read_csv(input_file)

wb = Workbook()

sheet = wb.active

for row in dataframe_to_rows(data, index=True, header=True):
        sheet.append(row)

chart = LineChart() 

categories = Reference(sheet, min_col=1, min_row=2, max_row=data.shape[0] + 1)

last_data_col = data.shape[1]  

output_col = last_data_col + 3
output_cell = f"{chr(ord('A') + output_col - 1)}{1}"  

values = Reference(sheet, min_col=2, max_col=last_data_col, min_row=1, max_row=data.shape[0] + 1)

chart.add_data(values, titles_from_data=True)
chart.set_categories(categories)

chart.title = chart_title
chart.style = 10  

sheet.add_chart(chart, output_cell)

wb.save(output_file)

print(f"Output saved to: {output_file}")
