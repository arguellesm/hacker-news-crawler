from app.crawler.domain.repository import Repository


class InMemoryRepository(Repository):
    """
    Represents an in memory repository.

    Entries are stored in memory as a list of Entry objects.
    """

    def __init__(self):
        """Inits InMemoryRepository with a list."""
        self.entries = []

    def save_entries(self, entries):
        """Saves entry list."""
        print("pre save")
        self.entries = entries
        print("post save")

    def get_entries(self):
        """Returns entry list."""
        return self.entries
