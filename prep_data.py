from __future__ import print_function

import os
import pandas as pd
import tarfile
from glob import glob

print("Setting up data directory")
print("-------------------------")

flightdir = os.path.join('data', 'nycflights')
jsondir = os.path.join('data', 'flightjson')

if not os.path.exists(flightdir):
    print("- Extracting flight data... ", end='', flush=True)
    tar_path = os.path.join('data', 'nycflights.tar.gz')
    with tarfile.open(tar_path, mode='r:gz') as flights:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(flights, "data/")
    print("done", flush=True)

if not os.path.exists(jsondir):
    print("- Creating json data... ", end='', flush=True)
    os.mkdir(jsondir)
    for path in glob(os.path.join('data', 'nycflights', '*.csv')):
        prefix = os.path.splitext(os.path.basename(path))[0]
        # Just take the first 10000 rows for the demo
        df = pd.read_csv(path).iloc[:10000]
        df.to_json(os.path.join('data', 'flightjson', prefix + '.json'),
                   orient='records', lines=True)
    print("done", flush=True)

print("** Finished! **")
