from abc import ABC, abstractmethod
from datetime import datetime


class Entry(ABC):
    def __init__(self, n: str, p):
        """
        Entry constructor.
        """
        self.name = n
        self.parent = p
        self.created = datetime.now()
        self.last_updated = datetime.now()
        self.last_accessed = datetime.now()

    def delete(self) -> bool:
        """
        Deletes current file.
        """
        if self.parent == None:
            return False
        return self.parent.delete_entry(self)

    @abstractmethod
    def size(self) -> int: pass

    def get_full_path(self) -> str:
        """
        Returns full path name of entry.
        """
        if self.parent == None:
            return self.name
        return self.parent.get_full_path() + "/" + self.name


class File(Entry):
    def __init__(self, n: str, p, size: int):
        """
        File constructor.
        """
        super().__init__(n, p)
        self.size = size

    @property
    def size(self) -> int:
        """
        Returns size of file.
        """
        return self.size


class Directory(Entry):
    def __init__(self, n: str, p):
        """
        Directory constructor.
        """
        super().__init__(n, p)
        self.contents = []

    def size(self) -> int:
        """
        Returns size of all content inside directory.
        """
        size = 0
        for c in self.contents:
            size += c.size()
        return size

    def number_of_files(self) -> int:
        """
        Counts the number of files in current directory.
        """
        count = 0
        for c in self.contents:
            if isinstance(c, Directory):
                count += 1  # Directory counts as a file
                count += c.number_of_files()
            elif isinstance(c, File):
                count += 1
        return count

    def delete_entry(self): pass
    def add_entry(self): pass
