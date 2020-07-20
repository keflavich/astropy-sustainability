"""
This module has functions to generate various information plots that can be
extracted from a git repository like how the number of commits and committers
grow over time.

Requires that you have a file that can be generatedwith:
git log --numstat --use-mailmap --format=format:"COMMIT,%H,%at,%aN"
"""

# Standard library
import os

# Third-party
import pandas as pd


def make_commit_stats_file(filename, overwrite=False, git_repo_path=None):
    """
    Running this will generate a file in the current directory that stores the
    statistics to make generating lots of plots easier.  Delete the file or
    set `overwrite` to True to always re-generate the statistics.
    """
    if os.path.isfile(filename) and not overwrite:
        df = pd.read_csv(filename)

    else:
        import subprocess
        import tempfile

        cmd = ('git log --use-mailmap --date=iso-local '
               '--format=format:\"%H\",\"%aI\",\"%aN\",\"%cN\"'.split())
        output = subprocess.check_output(cmd, cwd=git_repo_path)

        with tempfile.NamedTemporaryFile(mode='w+') as f:
            f.write(output.decode('utf-8'))
            f.seek(0)
            df = pd.read_csv(f.name, names=['commit', 'date', 'author',
                                            'committer'])

        df.to_csv(filename)

    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index(df['date'])

    return df
