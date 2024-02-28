import requests
import json
import pandas as pd
import re
import datetime
import os

# Read in historic data
metric_data_views = pd.read_csv ("Metric_Data/views.csv")
metric_data_unique_visits = pd.read_csv ("Metric_Data/unique_visits.csv")

today = datetime.date.today()
year_month = today.strftime("%Y-%m-")

#
# Get total number of views for this month
#

# Filter the number columns to only this, columns for this month 
filter_col = [col for col in metric_data_views if col.startswith(year_month)]
metric_data_views = metric_data_views[filter_col]

# Add a new column with the total number of views for each repository 
metric_data_views.loc[:,'Row_Total'] = metric_data_views.sum(numeric_only=True, axis=1)

# Sum the column with the total number of views for each repository
total_views = metric_data_views['Row_Total'].sum()
print("Total number of views for " +  year_month.rstrip("-") + ": " + str(int(total_views)))

#
# Get total number of views for this month
#

# Filter the number columns to only this, columns for this month 
filter_col = [col for col in metric_data_unique_visits if col.startswith(year_month)]
metric_data_unique_visits = metric_data_unique_visits[filter_col]

# Add a new column with the total number of views for each repository 
metric_data_unique_visits.loc[:,'Row_Total'] = metric_data_unique_visits.sum(numeric_only=True, axis=1)

# Sum the column with the total number of views for each repository
total_unique_visits = metric_data_unique_visits['Row_Total'].sum()
print("Total number of unique visits for " + year_month.rstrip("-") + ": " + str(int(total_unique_visits)))

#
# Update the README
# 

# Open the README for OpenSearch_CloudWatch_Alarms
with open("..\\README.md") as README_file:
	README_lines = [line.rstrip() for line in README_file]
README_file.close()

new_README_lines = []
views_months = []
unique_visits_months = []

for line in README_lines:

	# Find current month and update it with new totals
	if re.match(r'\| ' + re.escape(year_month.rstrip("-")) + r' \| ', line):
		new_README_lines.append('| ' + year_month.rstrip("-") + ' | ' + str(int(total_views)) + ' | ' + str(int(total_unique_visits)) + ' |')
		#print('| ' + year_month.rstrip("-") + ' | ' + str(int(total_views)) + ' | ' + str(int(total_unique_visits)) + '	|')

		views_months.append(int(total_views))
		unique_visits_months.append(int(total_unique_visits))

	else:
		# Update totals for all months
		if re.match(r'\| 202\d-.*', line):
			views_months.append(int(line.split('|')[2].rstrip().lstrip()))
			unique_visits_months.append(int(line.split('|')[3].rstrip().lstrip()))

		if re.match(r'.*Total.*', line):
			print("Total number of unique views: " + str(sum(views_months)))
			print("Total number of unique visits: " + str(sum(unique_visits_months)))
			
			new_README_lines.append("| **Total** | **" + str(sum(views_months)) + "** | **" + str(sum(unique_visits_months)) + "** |")
			#print("| **Total** | **" + str(sum(views_months)) + "** | **" + str(sum(unique_visits_months)) + "** |")
		else:
			new_README_lines.append(line)

new_README_file = open("..\\README.md", "w")

for line in new_README_lines:
	new_README_file.write(line + "\n")

new_README_file.close()

# Push to GitHub
os.system("git -C C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\GitHub_Insigths_History add .")
os.system('git -C C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\GitHub_Insigths_History commit -m "Updating history"')
os.system("git -C C:\\Users\\ev290\\OneDrive\\Desktop\\GitHub\\GitHub_Insigths_History push")