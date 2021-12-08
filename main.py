import numpy as np
import pandas as pd
import sklearn
url = "https://raw.githubusercontent.com/CS-521-A3/final-project-jaime-wang-and-Hilda-Guo/main/House%20Prediction%20Data.csv"
df = pd.read_csv(url)
df.to_csv('house_price', index=False)

