# Standard library
import os

# This project
from astropy_sustainability import get_papers

cache_path = os.path.join(os.path.split(os.path.abspath(__file__))[0],
                          '../cache')
os.makedirs(cache_path, exist_ok=True)


def main():

    astropy_citations_query = ("property:refereed "
                               "citations(2018AJ....156..123A) "
                               "OR citations(2013A&A...558A..33A)")


if __name__ == "__main__":
    main()