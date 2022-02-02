from dataclasses import dataclass
from enum import Enum
import sys

from yt_spammer_purge import __version__


class EErrorCategory(str, Enum):
    U = 'U'
    C = 'C'
    F = 'F'
    R = 'R'
    X = 'X'
    G = 'G'
    NOTSET = 'NOTSET'


@dataclass
class IMessage:
    message: str
    error_code: int = 0
    error_category: EErrorCategory = EErrorCategory.NOTSET

    def __str__(self):
        return self.message

    def __repr__(self):
        return str(self)


class EMessages(IMessage, Enum):
    PYTHON_TOO_OLD = IMessage(
        (
            f"This program requires running python 3.6 or higher! "
            f"You are running {'.'.join(sys.version_info)}"
        ), 2, EErrorCategory.U
    )

    WELCOME = IMessage(
        f'Loading YT Spammer Purge v{__version__}'
    )