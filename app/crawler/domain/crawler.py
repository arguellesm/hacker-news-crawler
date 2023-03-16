class Crawler:
    """
    Crawler interface.
    """

    def get_entries(self, num_entries=30):
        """Retrieves a number of entries."""

        raise NotImplementedError
