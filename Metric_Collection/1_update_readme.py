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
total = metric_data_views['Row_Total'].sum()
print("Total number of views: " + str(int(total)))

#
# Get total number of views for this month
#

# Filter the number columns to only this, columns for this month 
filter_col = [col for col in metric_data_unique_visits if col.startswith(year_month)]
metric_data_unique_visits = metric_data_unique_visits[filter_col]

# Add a new column with the total number of views for each repository 
metric_data_unique_visits.loc[:,'Row_Total'] = metric_data_unique_visits.sum(numeric_only=True, axis=1)

# Sum the column with the total number of views for each repository
total = metric_data_unique_visits['Row_Total'].sum()
print("Total number of unique visits: " + str(int(total)))