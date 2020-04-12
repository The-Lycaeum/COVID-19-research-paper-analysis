import re
import requests
from requests.exceptions import RequestException


urls = ['https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-04-10/comm_use_subset.tar.gz',
        'https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-04-10/noncomm_use_subset.tar.gz',
        'https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-04-10/custom_license.tar.gz',
        'https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-04-10/biorxiv_medrxiv.tar.gz']


# try to load each dataset from source link
# if URL header has a title for the data, use that as filename
# if not, parse URL for filename

for url in urls:
    try:
        with requests.get(url) as r:
            print('Attempting to connect to ', url)
            print('Connection successful.  Downloading content...')
            fname = ''
            if "Content-Disposition" in r.headers.keys():
                fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
            else:
                fname = url.split("/")[-1]

            print('Content Accessed: ', fname)
            path = "data/raw/" + fname
            print('Saving ', fname, " to location: ", path)
            with open(path, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=128):
                    fd.write(chunk)
            print("File download complete.", "\n")
    except RequestException as e:
        print('Error: ', e, 'with URL: ', url)

print('\n', "All files finished downloading. Please check /data/raw.")
