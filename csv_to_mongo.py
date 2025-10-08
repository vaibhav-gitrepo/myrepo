import os
from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://host.docker.internal:27017/")
db = client["mydatabase"]
collection = db["sample"]

df = pd.read_csv("sample.csv")
collection.insert_many(df.to_dict(orient="records"))
print("Data imported successfully!")




