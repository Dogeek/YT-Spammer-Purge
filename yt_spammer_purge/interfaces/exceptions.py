from .messages import IMessage


class YTSpammerError(Exception):
    def __init__(self, message: IMessage):
        self.message = message

    def __str__(self):
        return (
            f'Error Code {self.message.error_category}-{self.message.error_code}'
            f'{self.message.message}'
        )
