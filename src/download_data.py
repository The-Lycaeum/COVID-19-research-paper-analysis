import re
import requests
from requests.exceptions import RequestException

import os
import sys
import tarfile

import gzip
import shutil

urls = ['https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-04-10/biorxiv_medrxiv.tar.gz',
        'https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-04-10/custom_license.tar.gz',
        'https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-04-10/comm_use_subset.tar.gz',
        'https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-04-10/noncomm_use_subset.tar.gz']

## functions for unzipping the downloaded tar.gz files

def unpack(filename):
    total = untar(filename)
    if total:
        args = total, total > 1 and 's were' or ' was'
        sys.stdout.write('Report: %s file%s untared.' % args)
    else:
        filename = os.path.basename(sys.argv[0])
        sys.stdout.write('Usage: %s <file_or_dir> ...' % filename)

def untar(paths):
    total = 0
    for path in paths:
        if os.path.isdir(path):
            try:
                dir_list = os.listdir(path)
            except:
                pass
            else:
                total += untar(os.path.join(path, new) for new in dir_list)
        elif os.path.isfile(path):
            try:
                tarfile.open(path).extractall(os.path.dirname(path))
            except:
                pass
            else:
                total += 1
    return total


# try to load each dataset from source link
# if URL header has a title for the data, use that as filename
# if not, parse URL for filename

for url in urls:
    print('Attempting to connect to ', url)
    try:
        with requests.get(url) as r:
            
            print('Connection successful.  Downloading content...')
            fname = ''
            if "Content-Disposition" in r.headers.keys():
                fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
            else:
                fname = url.split("/")[-1]

            print('Content Accessed: ', fname)
            path = "../data/raw/" + fname
            print('Saving ', fname, " to location: ", path)
            with open(path, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=128):
                    fd.write(chunk)
            print("File download complete.", "\n")
            
            print("Extracting file...", "\n")
            #fname = fname.split(".")[0]
            print(fname)
            unpack(fname)
            print("Extraction for ", fname, " complete.", "\n")
    except RequestException as e:
        print('Error: ', e, 'with URL: ', url)

print('\n', "All files finished downloading & extracting. Please check /data/raw.")





