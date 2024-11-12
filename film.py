class Film: 

    def __init__(self, id: int, title: str, release_year: int, review: str="No review available"):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.review = review