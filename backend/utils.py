import os
import pandas as pd

def get_test_data():
    data_pth = "backend/datasets/tests/data.csv"
    data = []
    if os.path.exists(data_pth):
        df = pd.read_csv("backend/datasets/tests/data.csv")
        data = list(df.T.to_dict().values())
    return data
