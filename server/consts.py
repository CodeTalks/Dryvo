import os

DEBUG_MODE = os.environ.get("FLASK_DEBUG", 1)
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
WORKDAY_DATE_FORMAT = "%Y-%m-%d"
MAXIMUM_PER_PAGE = 100
MOBILE_LINK = "dryvo://auth/"
FACEBOOK_SCOPES = "email"
LOG_RETENTION = "7 days"
PROFILE_SIZE = 200
