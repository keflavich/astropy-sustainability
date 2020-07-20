# Standard library
import datetime

# Third-party
import ads
import astropy.table as at
import numpy as np


def get_papers(query, rows_per_page=100, max_pages=100):
    """
    Parameters
    ----------
    query : str
    rows_per_page : int (optional)
    max_pages : int (optional)

    Returns
    -------
    search_query : `ads.SearchQuery`
    papers_df : `pandas.DataFrame`
    """
    q = ads.SearchQuery(q=query,
                        sort="date",
                        max_pages=max_pages,
                        rows=rows_per_page,
                        fl=["identifier", "title", "author", "year",
                            "pubdate", "pub", "citation_count"])

    all_dicts = []
    for paper in q:
        # Get arxiv ID
        aid = [":".join(t.split(":")[1:]) for t in paper.identifier
               if t.startswith("arXiv:")]

        all_dicts.append(dict(
            authors='; '.join(paper.author) if paper.author else '',
            year=int(paper.year) if paper.year is not None else -1,
            pubdate=paper.pubdate if paper.pubdate is not None else '',
            title=paper.title[0] if paper.title is not None else '',
            pub=paper.pub if paper.pub is not None else '',
            arxiv=aid[0] if len(aid) else '',
            citations=(paper.citation_count
                       if paper.citation_count is not None else 0)
        ))

    papers = at.Table(sorted(all_dicts, key=lambda x: x['pubdate'],
                             reverse=True))

    # Convert list of papers to pandas DataFrame
    df = papers.to_pandas()
    df['pubdate'] = np.array([datetime.datetime(int(x.split('-')[0]),
                                                max(1, int(x.split('-')[1])), 1)
                              for x in df['pubdate']])
    df.index = df['pubdate']
    df = df.sort_index()

    return q, df
