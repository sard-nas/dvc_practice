import pandas as pd

dataset_path = './datasets/titanic.csv'

df = pd.read_csv(dataset_path)
df = df[['Pclass', 'Sex', 'Age']]

df.to_csv(dataset_path, index=False)
