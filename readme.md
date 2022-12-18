# Twitter ETL DAG

This DAG extracts data from the Twitter API using the `twitter_etl` function from the `twitter_etl` module, transforms it into a suitable format for analysis, and loads it into an S3 bucket. The `twitter_etl` function is run once a day.

![](diagram.png)
## Prerequisites

Before running this DAG, you will need to have the following installed:

- Python 3
- The following Python packages:
  - `airflow`
  - `datetime`
  - `timedelta`
  - `tweepy`
  - `pandas`
  - `s3fs`
  - `configparser`
- Create s3 bucket called `twitter-airflow-etl` or you can save output on your local machine
## Configuration


You will need to replace `YOUR_ACCESS_KEY`, `YOUR_ACCESS_SECRET`, `YOUR_ACCESS_TOKEN`, and `YOUR_ACCESS_TOKEN_SECRET` configuration file called `config.ini` with your own Twitter API credentials.

## Running the DAG

To run the DAG, simply use the Airflow UI to trigger the DAG or use the `airflow` command line to run the DAG.

## Output

The `twitter_etl` function will create a CSV file called `tweets.csv` in the `twitter-airflow-etl` S3 bucket. The file will contain the following columns:

- `user`: the username of the user who tweeted
- `text`: the text of the tweet
- `favorite_count`: the number of times the tweet was favorited
- `retweet_count`: the number of times the tweet was retweeted
- `created_at`: the date and time the tweet was created


