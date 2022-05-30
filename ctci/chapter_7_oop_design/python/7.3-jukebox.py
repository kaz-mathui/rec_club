from enum import Enum
from abc import ABC


class CD:
    pass


class Song:
    def __init__(self, id: int, title: str, length: int, CD: CD = None):
        """
        Song constructor.
        """
        self.id = id
        self.title = title
        self.length = length
        self.CD = CD


class User:
    def __init__(self, name: str):
        """
        User constructor.
        """
        self.name = name


class Playlist:
    def __init__(self):
        """
        Playlist constructor.
        """
        self.current_song = None
        self.queue = []

    def get_next_s_to_play(self):
        """
        Retrieves next song from queue.
        """
        return self.queue.pop(0)

    def queue_up_song(self, s: Song):
        """
        Adds a song to queue.
        """
        self.queue.append(s)


class CDPlayer:
    def __init__(self, playlist: Playlist = None, cd: CD = None):
        """
        CDPlayer constructor.
        """
        self.playlist = playlist
        self.cd = cd

    def play_song(self, s: Song):
        """
        Play current song.
        """
        pass


class Jukebox:
    def __init__(self):
        """
        Jukebox constructor.
        """
        self.cd_player = None
        self.user = None
        self.cd_collection = set()
        self.song_selector = None

    def get_current_song(self):
        """
        Gets current song from song selector.
        """
        return self.song_selector.get_current_song()

    def set_user(self, u: User):
        """
        Sets user.
        """
        self.user = u
