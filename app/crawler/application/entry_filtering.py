from app.crawler.domain.filter import Filter


class EntryFiltering:
    """
    Represents the entry filtering process.
    """

    def __init__(self, filter_functions, repository):
        """Init EntryFiltering with a set of filters and a repository."""

        self.repository = repository
        self.filters = dict()

        for f in filter_functions:
            if isinstance(f, tuple):
                self.filters[f[0].__name__] = Filter(f[0], sort_by=f[1])
            else:
                self.filters[f.__name__] = Filter(f)

    def filter(self, filter_type=None):
        """Apply a given filter.

        Parameter
        ---------
        filter_type: string
            Name of the filter willing to apply.

        Returns
        -------
        list
            A list of dictionaries representing entries.
        """

        entries = self.repository.get_entries()
        if filter_type is None:
            return [entry.to_dict() for entry in entries]
        return [entry.to_dict() for entry in self.filters[filter_type].apply(entries)]
