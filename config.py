from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 23378580))
API_HASH = getenv("API_HASH", "5056d12e7fdbdb6324f24a0baf38d953")
OWNER_ID = int(getenv("OWNER_ID", "8231852158"))
STRING_SESSION = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "KeralaChatfam")
UPDATE_CHNL = getenv("UPDATE_CHNL", "KeralaChatfam")
OWNER_USERNAME = getenv("OWNER_USERNAME", "KeralaChatfam")

# Random Start Images
IMG = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]


# Random Stickers
STICKER = [
    "",
    "",
    "",
]


EMOJIOS = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
