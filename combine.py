import glob
import pandas as pd 
import json
from tqdm import tqdm

files = glob.glob("./*.json")

data = []

bad = []

for file in tqdm(files):
	if "bad" in file:
		continue

	print(file)

	with open(file, "r") as f:
		try:
			current = json.load(f, strict = False)
		except json.decoder.JSONDecodeError:
			bad.append(file)
			continue

	for r in current['results']:
		current = pd.DataFrame.from_dict(r['bills'])

		data.append(current)
	
bills = pd.concat(data)

bills.to_csv("../Data/bills_propublica.csv", index = False)

print(bad)