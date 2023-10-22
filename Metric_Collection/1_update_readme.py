import requests
import json
import pandas as pd
import re
import datetime

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
#print("Total number of views: " + str(int(total_views)))

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
#print("Total number of unique visits: " + str(int(total_unique_visits)))

#
# Update the README
# 

# Open the README for OpenSearch_CloudWatch_Alarms
with open("..\\README.md") as README_file:
	README_lines = [line.rstrip() for line in README_file]
README_file.close()

new_README_lines = []

for line in README_lines:

	regex = r'\| ' + re.escape(year_month.rstrip("-")) + r'		\| '

	if re.match(regex, line):
		new_README_lines.append('| ' + year_month.rstrip("-") + '		| ' + str(int(total_views)) + '		  | ' + str(int(total_unique_visits)) + '					 |')
		print('| ' + year_month.rstrip("-") + '		| ' + str(int(total_views)) + '		  | ' + str(int(total_unique_visits)) + '					 |')
	else:
		new_README_lines.append(line)

new_README_file = open("..\\README.md", "w")

for line in new_README_lines:
	new_README_file.write(line + "\n")

new_README_file.close()