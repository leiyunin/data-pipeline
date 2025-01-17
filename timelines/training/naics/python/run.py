'''
This file will automatically run ML_data_generation.py in a loop. 
Output will be data files for all states from 2017-2022 for naics2 and naics4.
Paths of generated output follows: f"{output_dir}/US-{state}-training-naics{naics_value}-counties-{year}.csv"

Instructions:
1. First, install all required packages by running: 
    pip install -r requirement.txt

2. Then, run this file using: 
    python run.py
'''
import ML_data_generation
import datetime

year_range=range(2017,2022)
state_list=['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
for k in [2,4,6]:
    print(f"Start time: {datetime.datetime.now()}")
    for i in year_range:
        for j in state_list:
#             if i==2017 and j in ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
# 'HI', 'IA', 'ID', 'IL', 'IN'] or j=='ME':
#                 continue
            print(f"Starting task for naics{k}, year{i}, state{j}...")
            start_time = datetime.datetime.now()
            try:
                ML_data_generation.main(i,j,k)
                end_time = datetime.datetime.now()
                print(f"Succeed. naics{k}:{i}:{j} has been saved.")
                print(f"Execution time: {end_time}")
                print("=================================")
            except:
                print(f"Failed to generate output for naics{k}, year{i}, state{j}.")
                print("=================================")
                continue
    print(f"Output for naics{k} finished. End time: {datetime.datetime.now()}")