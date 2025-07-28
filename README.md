# GitHub Insights History

GitHub provides insights for repositories including page views and unique visitor counts. GitHub only provides 2 weeks of history for these metrics

The script [metric_collection.py](https://github.com/ev2900/GitHub_Insigths_History/blob/main/Metric_Collection/metric_collection.py) in this repository collect and store these metrics (page views and unique visitor counts) for all of a given GitHub user's repositories. Storing these metrics outside of GitHub allows a user to retain a longer history for page views and unique visitor counts metrics

## Summary of My Repository Data

To view the historic data of views for my repositories check out [views.csv](https://github.com/ev2900/GitHub_Insigths_History/blob/main/Metric_Collection/Metric_Data/views.csv) for unique visits check out [unique_visits.csv](https://github.com/ev2900/GitHub_Insigths_History/blob/main/Metric_Collection/Metric_Data/unique_visits.csv)

Or the table below summarizes views and unique visits per month for all of my repositories

| Month - Year | # of Views | # of Unique Visits |
| ------------ | ---------- | ------------------ |
| 2023-01 | 1615 | 452 |
| 2023-02 | 2051 | 644 |
| 2023-03 | 2219 | 780 |
| 2023-04 | 2774 | 727 |
| 2023-05 | 2651 | 638 |
| 2023-06 | 2541 | 769 |
| 2023-07 | 2530 | 706 |
| 2023-08 | 3448 | 856 |
| 2023-09 | 3860 | 916 |
| 2023-10 | 3818 | 953 |
| 2023-11 | 2786 | 888 |
| 2023-12 | 4982 | 1032 |
| 2024-01 | 4409 | 912 |
| 2024-02 | 3177 | 1025 |
| 2024-03 | 3985 | 1273 |
| 2024-04 | 3713 | 1248 |
| 2024-05 | 4140 | 1364 |
| 2024-06 | 3637 | 1528 |
| 2024-07 | 1813 | 681 |
| 2024-08 | 3397 | 1383 |
| 2024-09 | 3540 | 1326 |
| 2024-10 | 3472 | 1610 |
| 2024-11 | 1973 | 1113 |
| 2024-12 | 1522 | 795 |
| 2025-01 | 2241 | 1178 |
| 2025-02 | 1833 | 1091 |
| 2025-03 | 2083 | 1145 |
| 2025-04 | 1545 | 793 |
| 2025-05 | 1654 | 905 |
| 2025-06 | 1762 | 934 |
| 2025-07 | 1086 | 630 |
| **Total** | **86257** | **30295** |

## How to Set this up for your GitHub

1. Set up a personal access token

The script that collects the number of page views and unique visitors requires push access to see the traffic statistics for each repository. The script in this project uses a GitHub person access token to authenticate

To generate a person access token go to [Settings](https://github.com/settings/profile) -> [Developer settings](https://github.com/settings/apps) -> [Personal access tokens](https://github.com/settings/tokens) -> [Tokens classic](https://github.com/settings/tokens)

To make it easy you can select the repo permissions

<img width="500" alt="token_creation" src="https://github.com/ev2900/GitHub_Insigths_History/blob/main/README/token_creation.png">

After you create the person access token create a file with the name *token.txt* then copy and past the value of the person access token from GitHub into this file. Save the file in *Metric_Collection* folder

2. Install required libraries

The python script requires the following non-standard libraries: requests, pandas. If you do not already have them installed install them via

```pip install requests``` <br>
```pip install pandas```

3. Configure the output data files

The results of the python script will be directed to [unique_visits.csv](https://github.com/ev2900/GitHub_Insigths_History/blob/main/Metric_Collection/Metric_Data/unique_visits.csv) and [views.csv](https://github.com/ev2900/GitHub_Insigths_History/blob/main/Metric_Collection/Metric_Data/views.csv) in the *Metric_Collection* folder

When you clone, download ... this repository these CSV files have data in them w/r to my repositories. Delete all of the columns and rows except for first row of the first column

The excel file should look like the following before the first run

<img width="300" alt="blank_excel" src="https://github.com/ev2900/GitHub_Insigths_History/blob/main/README/blank_excel.png">

4. Update the python script

In the [metric_collection.py](https://github.com/ev2900/GitHub_Insigths_History/blob/main/Metric_Collection/metric_collection.py) update ```git_hub_user_name = <GitHub user name ex. ev2900>``` with your GitHub username and save the file

5. Run the python script

To run the python script on the command line run ```python metric_collection.py```

6. Schedule the python script

Now that everything is set up you will want to repeat step #5 at least every two weeks. GitHub insights only keeps two weeks of historic data. Running the script at least every two weeks ensures you are storing longer durations of these statistics in the csv files
