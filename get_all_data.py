#This is 116th congress
#115th congress
#114 congress
#113 congress
#112 congress
#111 congress
#110 congress
#109
#108 except for 3960
#107 except for 4480
#106 except for 1280
#105 
#104 except 320
#103


#103 senate returned no results


#all done except 116


#110 house congress was overwritten 

congresses = range(110, 117)


import os
import json
import time

from tqdm import tqdm


all_offsets = range(0, 10000, 20)  

for offset in tqdm(all_offsets):
	# First read it
	outname = 'offset{:05d}_106.json'.format(offset)
	os.system('curl "https://api.propublica.org/congress/v1/106/house/bills/introduced.json?offset={}" -H "X-API-Key: faPEPmdWz9WBS7PRp79zFKKXEVJMTTSbOlhDwjBZ" > {}'.format(offset, outname))

	# Then verify
	try:
		with open(outname, 'r') as f:
			data = json.load(f, strict = False)
	except json.decoder.JSONDecodeError:
		new_outname = outname.replace('.json', '_bad_character.json')
		os.rename(outname, new_outname)
		continue

	
	if data['status'] != 'OK':
		new_outname = outname.replace('.json', '_bad.json')
		os.rename(outname, new_outname)

	time.sleep(1)  # rest for 2 seconds


#now the senate bills


# for congress in tqdm(congresses):

# 	all_offsets = range(0, 5000, 20)  #remember to change

# 	for offset in tqdm(all_offsets):
# 		# First read it
# 		outname = 'offset{:05d}_{}s.json'.format(offset, congress)
# 		os.system('curl "https://api.propublica.org/congress/v1/{}/senate/bills/introduced.json?offset={}" -H "X-API-Key: faPEPmdWz9WBS7PRp79zFKKXEVJMTTSbOlhDwjBZ" > {}'.format(congress, offset, outname))

# 		print(outname)

# 		# Then verify
# 		try:
# 			with open(outname, 'r') as f:
# 				data = json.load(f, strict = False)
# 		except json.decoder.JSONDecodeError:
# 			new_outname = outname.replace('.json', '_bad_character.json')
# 			os.rename(outname, new_outname)
# 			continue

		
# 		if data['status'] != 'OK':
# 			new_outname = outname.replace('.json', '_bad.json')
# 			os.rename(outname, new_outname)

# 		time.sleep(1)  # rest for 2 seconds

