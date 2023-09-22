import requests
import json
import pandas
import re

# Configurable variables
git_hub_user_name = "ev2900"
bearer_token = open("token.txt", "r").read()

# Read in historic data
metric_data_views = pandas.read_csv ("Metric_Data/views.csv")
metric_data_unique_visits = pandas.read_csv ("Metric_Data/unique_visits.csv")

# Get list of all repositories for GitHub user
get_repos = requests.get("https://api.github.com/users/" + git_hub_user_name + "/repos?per_page=250")

# Add a new row if a row for the repository does not already exists
for repo in get_repos.json():

	repo_name = repo["name"]

	if not (metric_data_views["Repository_Name"] == repo_name).any():		
		
		new_row_df = pandas.DataFrame({"Repository_Name": [repo_name]})
		
		metric_data_views = pandas.concat([metric_data_views, new_row_df]) 
		print("New repository (views): " + repo_name)

	if not (metric_data_unique_visits["Repository_Name"] == repo_name).any():
		
		new_row_df = pandas.DataFrame({"Repository_Name": [repo_name]})
		
		metric_data_unique_visits = pandas.concat([metric_data_unique_visits, new_row_df])
		print("New repository (unique visits): " + repo_name)

for repo in get_repos.json():

	# Get traffic (ie. page views, unique visitor) for each repository
	get_traffic = requests.get("https://api.github.com/repos/" + git_hub_user_name + "/" + repo["name"] + "/traffic/views", headers = {"Accept": "application/vnd.github+json", "Authorization" : "Bearer " + bearer_token, "X-GitHub-Api-Version" : "2022-11-28"})

	# Create an empty column for the time stamp if it does not exist
	for date in get_traffic.json()["views"]:
			
		timestamp = date["timestamp"]

		if timestamp not in metric_data_views.columns:
			metric_data_views[timestamp] = ""

		if timestamp not in metric_data_unique_visits.columns:
			metric_data_unique_visits[timestamp] = ""

	# Iterate over traffic data by date
	for date in get_traffic.json()["views"]:
			
		repo_name = repo["name"]
		timestamp = date["timestamp"]
		views = date["count"]
		unique_visits = date["uniques"]

		# Add view data to data frame
		metric_data_views.loc[metric_data_views.Repository_Name == repo_name,timestamp] = views

		# Add unique vists to data frame
		metric_data_unique_visits.loc[metric_data_unique_visits.Repository_Name == repo_name,timestamp] = unique_visits

# Write updated data frame to CSV
metric_data_views.to_csv("Metric_Data/views.csv", index=False)
metric_data_unique_visits.to_csv("Metric_Data/unique_visits.csv", index=False)
