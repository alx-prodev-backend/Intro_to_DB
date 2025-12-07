# book_class.py
class Book:
    def __init__(self, title, author, year ):
        """Constructor : initializes book attributes"""
        self.title= title
        self.author = author
        self.year= year
        return

    def __del__(self):
        """Destructor : print message when object is deleted  """
        print(f"Deleting {self.title}")

    def  __str__(self):
        """ String representation: user-friendly readable text """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official represent recreates the object  """
        return f"Book('{self.title}', '{self.author}', {self.year})"