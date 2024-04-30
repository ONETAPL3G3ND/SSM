import secrets

class Client:
    def __init__(self, Username):
        self._Token = secrets.token_hex(16)
        self._Username = Username
        self._Messages = []
        self._NewMessages = []

    @property
    def Username(self):
        return self._Username

    @property
    def NewMessages(self):
        msg = self._NewMessages
        self._Messages += self._NewMessages
        self._NewMessages = []
        return msg

    @property
    def Token(self):
        return self._Token


