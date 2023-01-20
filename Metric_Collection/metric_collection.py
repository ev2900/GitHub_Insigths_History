
import requests
import json
import pandas

# Configurable variables
git_hub_user_name = "ev2900"
bearer_token = open("token.txt", "r").read()

# Read in historic metric data
metric_data_views = pandas.read_csv ("Metric_Data/views.csv")

# Get list of all repositories for GitHub user
get_repos = requests.get("https://api.github.com/users/" + git_hub_user_name + "/repos?per_page=250")

for repo in get_repos.json():

	# Get traffic (ie. page views, unique visitor) for each repository
	get_traffic = requests.get("https://api.github.com/repos/" + git_hub_user_name + "/" + repo["name"] + "/traffic/views", headers = {"Accept": "application/vnd.github+json", "Authorization" : "Bearer " + bearer_token, "X-GitHub-Api-Version" : "2022-11-28"})

	# Create an empty column for the time stamp if it does not exist
	for date in get_traffic.json()["views"]:
			
		timestamp = date["timestamp"]

		if timestamp not in metric_data_views.columns:
			metric_data_views[timestamp] = ""

	# Add view data to data frame
	for date in get_traffic.json()["views"]:
			
		repo_name = repo["name"]
		timestamp = date["timestamp"]
		views = date["count"]

		metric_data_views.loc[metric_data_views.Repository_Name == repo_name,timestamp] = views

# Write updated data frame to CSV
metric_data_views.to_csv("Metric_Data/views.csv", index=False)