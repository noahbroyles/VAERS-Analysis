#!/usr/bin/python3


import sys
import pandas as pd

for i,chunk in enumerate(pd.read_csv(sys.argv[1], chunksize=20000, engine='python')):
    chunk.to_csv(f'{sys.argv[2]}-{i}-VAERS{sys.argv[3]}.csv', index=False)
