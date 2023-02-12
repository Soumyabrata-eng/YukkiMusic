import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Vars
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGO_DB_URI  = getenv("MONGO_DB_URI")
BOT_TOKEN = getenv("BOT_TOKEN")
LOG_GROUP_ID= getenv("LOG_GROUP_ID")
MUSIC_BOT_NAME= getenv("MUSIC_BOT_NAME")
SUPPORT_GROUP= getenv("SUPPORT_GROUP")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "bloggerminds")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TeamYukki/YukkiMusicBot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400")) 
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
GITHUB_REPO = getenv("GITHUB_REPO", None)

# More Strings (Set up more assistants)
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Var Arrays
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []

# Images
START_IMG_URL = getenv("START_IMG_URL", "https://tiny.cc/erisnew")
PING_IMG_URL = getenv("PING_IMG_URL","Yukkimusic/assets/eris.jpeg)
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL","Yukkimusic/assets/eris.jpeg)
GLOBAL_IMG_URL = getenv("GLOBAL_IMG_URL","Yukkimusic/assets/eris.jpeg)
STATS_IMG_URL = getenv("STATS_IMG_URL","Yukkimusic/assets/eris.jpeg)
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL","Yukkimusic/assets/eris.jpeg)
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL","Yukkimusic/assets/eris.jpeg)
STREAM_IMG_URL = getenv("STREAM_IMG_URL","Yukkimusic/assets/eris.jpeg) 
SOUNDCLOUD_IMG_URL =getenv("SOUNDCLOUD_IMG_URL","Yukkimusic/assets/eris.jpeg)
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL","Yukkimusic/assets/eris.jpeg)
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL","Yukkimusic/assets/eris.jpeg)
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL","Yukkimusic/assets/eris.jpeg)
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL","Yukkimusic/assets/eris.jpeg)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))
