To run. -Unfortunately I didn't save a venv so you might have to sort out dependency conflicts, I intended it to be a one time run-. 

1. Make sure you have Java installed as a dependency. The install the dependencies in requirements.txt

2. In the scraper.py script mess about with the start_date, end_date and the unix time stamp increments to change time range and sampling frequency. 

3. From the red.ipynb file, remove the `df = df.sample(n = 1000000)` cell in `In [9]:`. If you are using a different sample size. 
