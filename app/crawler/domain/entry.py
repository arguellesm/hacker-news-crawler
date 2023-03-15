class Entry:
    """
    Represents a new from Hacker News.
    """

    def __init__(self, title, order, comments, points):
        """Inits Entry with a title, an order number, a comment number and a points number."""
        
        if len(title) > 0:
            self.title = title
        else:
            raise ValueError('Title can not be empty')
        
        try:
            order = int(order)
        except:
            raise TypeError('Order must be a number')
        
        if int(order) > 0:
            self.order = order
        else:
            raise ValueError('Invalid order number')

        try:
            comments = int(comments)
            self.comments = comments
        except:
            raise TypeError('Comments must be an integer.')
        
        try:
            points = int(points)
            self.points = points
        except:
            raise TypeError('Points must be an integer.')
        


    def to_dict(self):
        """Returns a dictionary with the Entry information."""

        return {key: value for key, value in self.__dict__.items()}