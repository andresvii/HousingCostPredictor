import pandas as pd
import sys
import numpy as np
from sklearn.datasets.openml import fetch_openml


# # we check to see if the dataset entry is valid.
# # we catch the error in case of invali entry.
filename = sys.argv[1]
try:
    if(filename.endswith('.csv')):
        df = pd.read_csv(filename, header = None)  # reading the dataset with pandas function
    ## here is were we put X and Y 
except:
    print('Invalid entry for dataset argument')
    sys.exit()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1, stratify = y) 
# # X and y values for out train case and test case. 
