"""Source adapters. Each takes a source config dict and returns a list of Jobs."""
from . import icims, links, oracle_hcm, successfactors, workday

FETCHERS = {
    "workday": workday.fetch,
    "oracle_hcm": oracle_hcm.fetch,
    "successfactors": successfactors.fetch,
    "icims": icims.fetch,
    "links": links.fetch_links,
    "page_watch": links.fetch_page_watch,
}
