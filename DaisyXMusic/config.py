import os
from os import path
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = "BQARnHIjF84XYfXQDy30OgYUhgV8U9BNcjgcjj_fMzS06yDK6wRqsvjzdU-udEeHG99Kkq_LIbynXFzlQ50B_nRJhLoeIELbRCERfGVtoFHLHdZbi-FY6TdjaSfR-tHAOgbi6Jk39LmXQwXSDb1MlpWArivA-D7HVJiDQ_deCANPZ5cJy_9cWaBvs4pWPYgC1OrUZTaMpovqL45Kn70ELXrfWtQBm_e4uqpunYvezXsp23ApsF5jNg7oLIbuJysIaLxUgSAOoIbPuQcR8fan8JxwBU9Q3lz1fVzhBe-BAwkKoDhCeQcPiKK0ledqM7LQDgYqyNbwSVQJC6ASCyPyfOfdbWOzLwA"
BOT_TOKEN = "1730197977:AAHASrIdiaO-R07Onu4dH9EsJqzt-KMppi8"
BOT_NAME = "@VCPlayBot"
UPDATES_CHANNEL = "LaylaList"
BG_IMAGE = "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png"
admins = {}
API_ID = int("6595783")
API_HASH = "d6b2045d94544c7c406daf585671a44e"
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
