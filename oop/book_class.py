class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes the book with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation (for debugging)."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

