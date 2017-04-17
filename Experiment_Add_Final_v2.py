import requests
import json
import sys

usr = sys.argv[1]
tkn = sys.argv[2]
gen_id = sys.argv[3]
sam_name = sys.argv[4]
ver = sys.argv[5]
source = sys.argv[6]
path_1 = sys.argv[7]
path_2= sys.argv[8]

payload = {"genome_id": gen_id,
           "metadata" : {"name": sam_name,
                         "version": ver,
                         "source" : source,
                         "restricted": True
                        },
           "source_data": [{"type": "irods", "path": path_1}, 
                           {"type": "irods", "path": path_2}],
           "read_params": {"read_type": "paired", "encoding": 33},
           "alignment_params": {"tool": "hisat2", "load_bam": True}
          }
params = {'username': usr, 
           'token' : tkn}

response= requests.put("https://geco.iplantcollaborative.org/coge-qa/coge/api/v1/experiments", 
                       data=json.dumps(payload),
                       headers={'Content-Type': 'application/json'},
                       params=params)
status_code = response.status_code
response_url= response.url
response_text = response.text
if status_code == 201:
    print("Success")
    print response_url
else: 
    print("Error")
    print status_code
    print response_url
    print response_text