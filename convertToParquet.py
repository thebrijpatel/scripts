import pandas as pd
import sys
df = pd.read_parquet(sys.argv[1])
df.to_csv(sys.argv[1].split('.')[0]+'.csv')
