import requests
import sys

genome_id = sys.argv[1]

response = requests.get("https://genomevolution.org/coge/api/v1/genomes/%s" % str(genome_id))
if response.status_code == 200:
    json_obj = response.json()
    chromosomes = json_obj['chromosomes']
    full_length = 0
    for key in chromosomes:
        if key['length']:
            full_length += int(key['length'])
    print "The full length of the genome is: %d. " % (full_length) 
            
else:
    print "Page cannot be found or server is not responding"