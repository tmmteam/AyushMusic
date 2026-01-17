import os

from AyushMusic.core.bot import Aru
from AyushMusic.core.dir import dirr
from AyushMusic.core.git import git
from AyushMusic.core.userbot import Userbot
from AyushMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()

# git only for vps, not heroku
if not os.getenv("DYNO"):
    git()

dbb()
heroku()

app = Aru()
userbot = Userbot()

from .platforms import *

apple = AppleAPI()
carbon = CarbonAPI()
soundcloud = SoundAPI()
spotify = SpotifyAPI()
resso = RessoAPI()
telegram = TeleAPI()
youtube = YouTubeAPI()
