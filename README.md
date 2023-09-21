# GitHub Insights History
 
GitHub provides insights for repositories including page views and unique visitor counts. GitHub only provides 2 weeks of history for these metrics

The script [metric_collection.py](https://github.com/ev2900/GitHub_Insigths_History/blob/main/Metric_Collection/metric_collection.py) in this repository collect and store these metrics (page views and unique visitor counts) for all of a given GitHub user's repositories. Storing these metrics outside of GitHub allows a user to retain a longer history for page views and unique visitor counts metrics

## Summary of My Repository Data

To view the historic data of views for my repositories check out [views.csv](https://github.com/ev2900/GitHub_Insigths_History/blob/main/Metric_Collection/Metric_Data/views.csv) for unique visits check out [unique_visits.csv](https://github.com/ev2900/GitHub_Insigths_History/blob/main/Metric_Collection/Metric_Data/unique_visits.csv)

Or the table below summarizes views and unique visits per month for all of my repositories
 
| Month - Year      | # of Views  | # of Unique Visits   |
| -----------       | ----------- | -------------------- |
| January - 2023    | 1,615       | 452                  |
| February - 2023   | 2,051       | 644                  |
| March - 2023      | 2,219       | 780                  |
| April - 2023      | 2,774       | 727                  |
| May - 2023        | 2,651       | 638                  |
| June - 2023       | 2,541       | 769                  |
| July - 2023       | 2,530       | 706                  |
| September - 2023  | 3,448       | 856                  |
| **Total**         | **19,829**  | **5,572**            |

## How to Set this up for your GitHub

1. Set up a personal access token

The script that collects the page views and unique visitors requires push access in order to see the traffic statistics for each repository. The script uses a GitHub person access token to authenticate

To generate a person access token go to [Settings](https://github.com/settings/profile) -> [Developer settings](https://github.com/settings/apps) -> [Personal access tokens](https://github.com/settings/tokens) -> [Tokens classic](https://github.com/settings/tokens)

The token will need permissions to push to repositories in your account. To make it easy you can select the repo permissions

<img width="500" alt="cat_indicies_1" src="https://github.com/ev2900/GitHub_Insigths_History/blob/main/README/token_creation.png">

After you create the person access token create a file with the name *token.txt* copy/past the value of the person access token from GitHub into this file. Save the file in *Metric_Collection* folder. Or update the path to the file in line 8 of the [metric_collection.py](https://github.com/ev2900/GitHub_Insigths_History/blob/main/Metric_Collection/metric_collection.py) script

2. Run the python script

The python requires the following libraries: requests, json, pandas. If you do not already have them installed you will need to install them

Before running the script update the  ```git_hub_user_name = <GitHub user name ex. ev2900>``` with your GitHub username

To run the python script on the command line run ```python metric_collection.py``` 

After running the python script you should see the files in the *Metric_Data* [unique_visits.csv](https://github.com/ev2900/GitHub_Insigths_History/blob/main/Metric_Collection/Metric_Data/unique_visits.csv) and [views.csv](https://github.com/ev2900/GitHub_Insigths_History/blob/main/Metric_Collection/Metric_Data/views.csv) updated
