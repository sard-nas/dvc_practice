import pandas as pd

dataset_path = './datasets/titanic.csv'

df = pd.read_csv(dataset_path)
df['Age'] = df['Age'].fillna(int(df['Age'].mean()))

df.to_csv(dataset_path, index=False)
