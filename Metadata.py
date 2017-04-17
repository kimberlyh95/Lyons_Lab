import sys
import csv
import json
from datetime import datetime

info_f = sys.argv[1]

with open(info_f) as CSV:
	readCSV = csv.DictReader(CSV)
	for row in readCSV:
		genome_id = int(row["ProjectID"])
		name = row['Run']
		sample_name = row['SampleName']
		download_path = row["Run"]
		biosample = row['BioSample']
		srr_number = row['Run']
		SRA = row['Sample']
		link = row['Link']
		data = {}
		data['genome_id'] = genome_id
		data['notebook_id'] = 0
		data['meta_data'] = {}
		data['meta_data']['name'] = sample_name
		data['meta_data']['description'] = "None"
		data['meta_data']['restriced'] = True 
		data['meta_data']['source'] = "NCBI"
		data['meta_data']['version'] = 1
		data['meta_data']['tags'] = ['string', 'string']
		data['additional_metadata'] = [] 
		extra = {}
		extra['BioSample'] = biosample
		extra['SRA'] = SRA
		extra['Link'] = link
		extra['Obtained'] = str(datetime.now())
		data['additional_metadata'].append(extra)
		sra_stuff = {}
		sra_stuff['type'] = 'sra'
		sra_stuff['path'] = download_path
		data['source_data'] = []
		data['source_data'].append(sra_stuff)

		organized_data = json.dumps(data, indent=4)
		print organized_data





