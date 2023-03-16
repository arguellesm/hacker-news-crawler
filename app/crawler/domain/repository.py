class Repository:
    """
    Repository interface.
    """

    def save_entries(self):
        """Saves entries."""

        raise NotImplementedError

    def get_entries(self):
        """Retrieves entries."""

        raise NotImplementedError
