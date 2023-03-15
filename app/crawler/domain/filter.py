class Filter:
    """
    Represents a filter and sorting criteria.
    """

    def __init__(self, *filter_functions, sort_by=None, reverse_sorting=True):
        """Inits Filter with a list of filter functions and sorting criterion."""

        self.filter_functions = filter_functions
        self.sort_by = sort_by
        self.reverse_sorting = reverse_sorting


    def apply(self, entries):
        """Applies filter functions to a set of entries"""
        
        filtered_entries = []
        
        for entry in entries:
            if all(filter_func(entry) for filter_func in self.filter_functions):
                filtered_entries.append(entry)

        if self.sort_by:
            filtered_entries.sort(key=lambda entry: entry.to_dict()[sort_by], reverse=reverse_sorting)
        
        return filtered_entries