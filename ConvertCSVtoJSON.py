import pandas as pd
csv_file = pd.DataFrame(pd.read_csv(r'C:\Users\heimbucha\Documents\Year_FIPS_DMax.csv', sep = ",", header = 0, index_col = False))
csv_file.to_json(r'C:\Users\heimbucha\Documents\Year_FIPS_DMax.json')