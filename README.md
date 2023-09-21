# GitHub Insights History
 
GitHub provides insights for repositories including page views and unique visitor counts. GitHub only provides 2 weeks of history for these metrics. 

The script [metric_collection.py](https://github.com/ev2900/GitHub_Insigths_History/blob/main/Metric_Collection/metric_collection.py) in this repository collect and store these metrics (page views and unique visitor counts) for all of a given GitHub user's repositories. Storing these metrics outside of GitHub allows a user to retain a longer history for page views and unique visitor counts metrics.

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

The script that collects the page views and unique visitors requires push access in order to see the traffic statistics for each repository. The script uses a GitHub person access token to authenticate. 

To generate a person access token go to [Settings](https://github.com/settings/profile) -> [Developer settings](https://github.com/settings/apps) -> [Personal access tokens](https://github.com/settings/tokens) -> [Tokens classic](https://github.com/settings/tokens)

The token will need premissions to push to repositories in your account. To make it easy you can select the repo premissions



3. Run the python script
   
