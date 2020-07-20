"""TODO: need to store ADS_DEV_KEY on CI"""

# Standard library
import os

# This project
from astropy_sustainability import get_papers

queries = {
    'astropy-citations': (
        'property:refereed citations(2018AJ....156..123A) '
        'OR citations(2013A&A...558A..33A)'),
    'python-fulltext': (
        'full:"python" property:"refereed" collection:"astronomy"'),
    'idl-fulltext': (
        'full:"idl" property:"refereed" collection:"astronomy"'),
    'matlab-fulltext': (
        'full:"matlab" property:"refereed" collection:"astronomy"'),
    'julia-fulltext': (
        'full:"julia" property:"refereed" collection:"astronomy"')
}

# One up from the scripts directory:
cache_path = os.path.join(os.path.split(os.path.abspath(__file__))[0],
                          '../cache')
os.makedirs(cache_path, exist_ok=True)

for slug, query in queries.items():
    filename = os.path.join(cache_path, f'{slug}.csv')
    if os.path.exists(filename):
        print(f"Results exist for '{slug}' - skipping...")
    q, papers_df = get_papers(query, rows_per_page=1000, max_pages=100)
    print(q.response.get_ratelimits())
    papers_df.to_csv(filename)
