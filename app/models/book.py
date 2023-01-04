from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    def to_dict(self):
        # Create an empty dictionary
        # for each attribute in Book
        # create a key with the attribute's name
        # set it to the value of the attribute
        # return the dictionary

        book_dict = {}
        book_dict["id"] = self.id
        book_dict["title"] = self.title
        book_dict["description"] = self.description
        
        return book_dict