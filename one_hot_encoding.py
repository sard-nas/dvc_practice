import pandas as pd

dataset_path = './datasets/titanic.csv'

df = pd.read_csv(dataset_path)
df = pd.get_dummies(df, columns=['Sex'])

df.to_csv(dataset_path, index=False)
