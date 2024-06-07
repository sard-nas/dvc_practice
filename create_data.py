import pandas as pd
import requests

dataset_path = './datasets/titanic.csv'

url = 'https://raw.githubusercontent.com/ashishpatel26/Titanic-Machine-Learning-from-Disaster/master/input/train.csv'
response = requests.get(url)

with open(dataset_path, 'wb') as file:
    file.write(response.content)

df = pd.read_csv(dataset_path)
