import os
from os import path
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = "AQC79eJ39IiE24rjPk0ASkdVI_LhtkCcQ43gjwvLxbm8aYE43INvs5Xvz4xce2JOs94kT1Mw8MH21vw7ThzOfsFbRVSLTPz0FS0aZgtOU8G3Gyjo8Mc8lJjq3hRf-gSfjWkzVjnPdTOABP3JbXptpk4EezyBTc5k_QZqZpSDWGGMuphjOgKVD1C2T1-7YT5TkW3VDN3YhVVygwyhbdHYTTRee6RzJPgwnEQ8ijNJBGWxpgNgd_j2rNuhwv2JO1GjBIqL8WXOEW1aCB5rJIF3k7sJk0GeeO6IQGFu_Y5aYuvOWeQXw5VEzSF47nFJsoHIomuq03Zx9RkIgpbUalmwiNLPTXKoywA"
BOT_TOKEN = "1756652877:AAHGjb4XeqypEzZgR9OlSWfYdzmTZ3tj1ns"
BOT_NAME = "@VCPlayBot"
UPDATES_CHANNEL = "LaylaList"
BG_IMAGE = "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png"
admins = {}
API_ID = int("4042631")
API_HASH = "e70b375fca15737a24eb5b8ba5ffe045"
BOT_USERNAME = "ALMusicBot"
ASSISTANT_NAME = "ALMusicAssistant"
SUPPORT_GROUP = "Awesomesupport"
PROJECT_NAME = "VCPlayBot2.0"
SOURCE_CODE = "github.com/QueenArzoo/VCPlayBot"
DURATION_LIMIT = int("15")
ARQ_API_KEY = None
PMPERMIT = "ENABLE"
LOG_GRP = None
COMMAND_PREFIXES = list("/")

SUDO_USERS = list("797768146")
