SECRET_KEY = "dump-secret-key"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.admin",
    "global_query_strings",
)


DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

GLOBAL_QUERY_STRINGS_IGNORE_URLS = ["example.com", "https://www.foo.org"]
GLOBAL_QUERY_STRINGS_IGNORE_RELATIVE_PATHS = True
GLOBAL_QUERY_STRINGS_PARAMS = {"foo": "bar", "lorem": "ipsum"}