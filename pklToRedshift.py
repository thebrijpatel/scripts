import pickle as pkl
from pandas.io.sql import SQLTable

# Begin code to speedup db insert. Make sure to write this before importing pandas
def _execute_insert(self, conn, keys, data_iter):
    data = [dict((k, v) for k, v in zip(keys, row)) for row in data_iter]
    conn.execute(self.table.insert().values(data))

SQLTable._execute_insert = _execute_insert
# End code to speedup db insert

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://<user>:<password>@<hostname>/<dbname>')


with open('<pkl file path>', 'rb') as f:
    object = pkl.load(f)

df = pd.DataFrame(object)
new_column_name = {}

df.to_sql('3d_cluster_acad', engine, if_exists='replace', index=False, schema="mesa")

