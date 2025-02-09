# Meme Virality Analysis

## Overview
This project analyzes the factors influencing meme virality using Reddit data. The workflow involves scraping top posts from subreddits, merging the collected data, and running an analysis to extract insights.

## Workflow
### 1. Scraping Reddit Data
Run `scrape_top.py` to extract posts from the **top sections of subreddits**. Each execution will prompt you to enter the subreddit you want to extract posts from.

**Note:** For our research, we have already collected data from specific subreddits, stored in CSV files formatted as:
```
posts_hot_{subredditname}.csv
```
These files are available in the project folder.

### 2. Merging Data
Run `merge.py` to combine all collected data into a single file. This merged dataset will serve as the foundation for further analysis.

### 3. Analyzing Data
Use `analysis.ipynb` to perform an in-depth analysis of the dataset. This notebook contains scripts to extract insights related to meme virality.

## Requirements
All necessary dependencies are listed in `requirements.txt`. Install them using:
```
pip install -r requirements.txt
```

## Conclusion
This project provides an automated pipeline to scrape, merge, and analyze Reddit posts, offering insights into what makes memes go viral. By leveraging data-driven approaches, we uncover hidden patterns influencing meme popularity.

Happy Analyzing!

