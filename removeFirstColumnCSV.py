import pandas as pd
import sys
import os
df = pd.read_csv(sys.argv[1])
# If you know the name of the column skip this
first_column = df.columns[0]
# Delete file first
os.system("rm " + sys.argv[1])
df = df.drop([first_column], axis=1)
df.to_csv(sys.argv[1], index=False)
