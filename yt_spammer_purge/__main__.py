import sys

from rich import print

from yt_spammer_purge.helpers.youtube import YoutubeClient
from yt_spammer_purge.interfaces.messages import EMessages
from yt_spammer_purge.interfaces.exceptions import YTSpammerError


def main():
    if sys.version_info < (3, 6):
        raise YTSpammerError(EMessages.PYTHON_TOO_OLD)

    print(EMessages.WELCOME)
    client = YoutubeClient()
