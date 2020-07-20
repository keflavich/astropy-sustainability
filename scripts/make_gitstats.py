"""TODO: need to clone astropy as well..."""

# Standard library
import os
import sys

# This project
from astropy_sustainability import make_commit_stats_file

if len(sys.argv) < 2:
    raise ValueError("Specify the path to the Astropy git repo")

# One up from the scripts directory:
cache_path = os.path.join(os.path.split(os.path.abspath(__file__))[0],
                          '../cache')
os.makedirs(cache_path, exist_ok=True)

make_commit_stats_file(os.path.join(cache_path, 'gitlog.csv'),
                       git_repo_path=sys.argv[1], overwrite=True)
