from abc import ABC
from enum import Enum, auto


class UserStatusType(Enum):
    Offline = auto()
    Away = auto()
    Idle = auto()
    Available = auto()
    Busy = auto()


class RequestStatus(Enum):
    Unread = auto()
    Read = auto()
    Accepted = auto()
    Rejected = auto()


class User:
    def __init__(self, id: int, account_name: str, full_name: str):
        """
        User constructor.
        """
        self.id = id
        self.status = None
        # Maps from the other participant's user if to the chat.
        self.private_chats = {}
        # List of group chats.
        self.group_chats = []
        # Maps from the other person's user id to the add request.
        self.received_add_requests = {}
        # Maps from the other person's user id to the add request.
        self.sent_add_requests = {}
        # Maps from the user id to user object.
        self.contacts = {}
        self.account_name = account_name
        self.full_name = full_name

    def send_message(self, to, content: str): pass
    def send_message_to_group_chat(self, id: int, content: str): pass
    def add_contact(self, user): pass
    def received_add_request(self, req): pass
    def sent_add_request(self, req): pass
    def remove_add_request(self, req): pass
    def request_add_user(self, account_name: str): pass


class Conversation(ABC):
    def __init__(self, id):
        """
        Conversation constructor.
        """
        self.id = id
        self.participants = []
        self.messages = []


class GroupChat(Conversation):
    def __init__(self, id):
        """
        GroupChat constructor.
        """
        super().__init__(id)

    def remove_participant(self, u: User): pass
    def add_participant(self, u: User): pass


class PrivateChat(Conversation):
    def __init__(self, id, u1: User, u2: User):
        """
        PrivateChat constructor.
        """
        super().__init__(id)
        self.participants.append(u1)
        self.participants.append(u2)

    def get_another_participant(self, u: User): pass


class Message:
    def __init__(self, content: str, date: str):
        """
        Message constructor.
        """
        self.content = content
        self.date = date


class AddRequest:
    def __init__(self, fro: User, to: User, date: str):
        """
        AddRequest constructor.
        """
        self.from_user = fro
        self.to_user = to
        self.data = date
        self.status = None


class UserStatus:
    def __init__(self, type: UserStatusType, message: str):
        """
        UserStatus constructor.
        """
        self.type = type
        self.message = message
