import os
import glob
import pandas as pd
from psaw import PushshiftAPI
from datetime import datetime as dt


os.mkdir("data")


# Specify start and end dates
start_epoch = int(dt(2021, 3, 22).timestamp()) 
end_epoch = int(dt(2022, 6, 1).timestamp()) 

# Create API Instance
api = PushshiftAPI()

while start_epoch < end_epoch + 86200: 
    # Starting time string formatting
    start_date = dt.fromtimestamp(start_epoch)
    date_str = start_date.strftime("%Y %b %d")

    # Make request
    api_request_generator = api.search_comments(subreddit='redscarepod',
                                                after = start_epoch,
                                                before = start_epoch + 860000//2) 
    print(f"Making API call for {dateStr}")
    
    try:
        print(f"Beggining to process data for {dateStr}")
        df_comments = pd.DataFrame([comment.d_ for comment in api_request_generator])
        df_comments['date'] = pd.to_datetime(missy_comments['created_utc'], utc = True, unit = 's')
        df_central = df_comments[['date','score','body']]
        print(f"Data processed for {date_str}")
        df_central.to_csv(fr"data\\{date_str}.csv", index = False, header = True)
    except KeyError:
        print(f"Got key error skipping {date_str}")
        pass
        
    start_epoch += 860000//2 # 4 days
    
print("Scraping complete, starting concatenation")
os.chdir(r"data\\")

all_filenames = [file for file in glob.glob('*.csv')]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ]) 
combined_csv.to_csv( "combined.csv", index = False, encoding = 'utf-8-sig') 
print("Dataset ready to use")
