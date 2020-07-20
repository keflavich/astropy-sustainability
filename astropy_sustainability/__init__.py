from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    pass  # package is not installed

from .ads_helpers import get_papers
from .git_helpers import make_commit_stats_file
