from __future__ import print_function

import os
import tarfile

print("Setting up data directory")
print("-------------------------")

if not os.path.exists('data/nycflights/'):
    print("- Extracting flight data... ", end='', flush=True)
    with tarfile.open('data/nycflights.tar.gz', mode='r:gz') as flights:
        flights.extractall('data/')
    print("done", flush=True)

print("** Finished! **")
