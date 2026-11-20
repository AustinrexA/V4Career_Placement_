"""The 15 replacement job sources configured for V4Career.

Catalog entries make sources visible in the existing UI. A source is not
collectable until its Actor/API input has been tested and locally approved.
"""
JOB_PORTALS = [
    {"name": "Google Jobs", "base_url": "https://www.google.com/search?udm=8", "key": "GOOGLE_JOBS", "popular": True, "method": "Apify"},
    {"name": "iimjobs", "base_url": "https://www.iimjobs.com/", "key": "IIMJOBS", "popular": True, "method": "Apify"},
    {"name": "Jobrapido", "base_url": "https://www.jobrapido.com/", "key": "JOBRAPIDO", "popular": True, "method": "Apify"},
    {"name": "Apna", "base_url": "https://apna.co/", "key": "APNA", "popular": True, "method": "Apify"},
    {"name": "Remote OK", "base_url": "https://remoteok.com/", "key": "REMOTE_OK", "popular": False, "method": "Apify"},
    {"name": "We Work Remotely", "base_url": "https://weworkremotely.com/", "key": "WE_WORK_REMOTELY", "popular": False, "method": "Apify"},
    {"name": "Remotive", "base_url": "https://remotive.com/", "key": "REMOTIVE", "popular": False, "method": "Apify"},
    {"name": "Himalayas", "base_url": "https://himalayas.app/jobs", "key": "HIMALAYAS", "popular": False, "method": "Apify"},
    {"name": "Jobicy", "base_url": "https://jobicy.com/jobs", "key": "JOBICY", "popular": False, "method": "Apify"},
    {"name": "Working Nomads", "base_url": "https://www.workingnomads.com/jobs", "key": "WORKING_NOMADS", "popular": False, "method": "Apify"},
    {"name": "Arbeitnow", "base_url": "https://www.arbeitnow.com/", "key": "ARBEITNOW", "popular": False, "method": "Apify"},
    {"name": "Get on Board", "base_url": "https://www.getonbrd.com/", "key": "GET_ON_BOARD", "popular": False, "method": "Apify"},
    {"name": "Y Combinator – Work at a Startup", "base_url": "https://www.ycombinator.com/jobs", "key": "YC_WORK_AT_A_STARTUP", "popular": False, "method": "Apify"},
    {"name": "Dice", "base_url": "https://www.dice.com/", "key": "DICE", "popular": False, "method": "Apify"},
    {"name": "Built In", "base_url": "https://builtin.com/jobs", "key": "BUILT_IN", "popular": False, "method": "Apify"},
]

UI_PORTAL_KEYS = {item["key"] for item in JOB_PORTALS}
PORTAL_BY_KEY = {item["key"].lower(): item for item in JOB_PORTALS}
PORTAL_BY_NAME = {item["name"].strip().lower(): item for item in JOB_PORTALS}

# This is the Actor ID from the successful Google Jobs test run. All other
# sources remain unconfigured until their individual Actor is tested.
DEFAULT_APIFY_ACTORS = {
    "GOOGLE_JOBS": "vncntlabs~google-jobs-scraper",
}

APIFY_PORTAL_BILLING = {}
