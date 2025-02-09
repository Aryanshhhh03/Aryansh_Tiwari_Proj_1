import os
import glob
import pandas as pd

def merge_csv_files(output_file="posts.csv"):
    # Find all files matching 'posts_hot_*.csv'
    csv_files = glob.glob("posts_hot_*.csv")

    if not csv_files:
        print("No CSV files found to merge.")
        return

    merged_df = pd.DataFrame()  # Create an empty dataframe

    for file in csv_files:
        df = pd.read_csv(file)
        merged_df = pd.concat([merged_df, df], ignore_index=True)

        print(f"Merged: {file}")  # Track progress

    # Remove duplicates based on Post_ID
    if "Post_ID" in merged_df.columns:
        merged_df.drop_duplicates(subset=["Post_ID"], keep="first", inplace=True)

    # Save the merged CSV file
    merged_df.to_csv(output_file, index=False, encoding="utf-8")
    print(f"Successfully merged {len(csv_files)} files into {output_file}")

if __name__ == "__main__":
    merge_csv_files()
