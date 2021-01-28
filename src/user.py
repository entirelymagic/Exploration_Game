

class User:
    """User class, will have email as the primary key when looking for it in the database."""

    def __init__(self, email, first_name, last_name, heroes):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.heroes = heroes

    def __repr__(self):
        return f"<User  email: {self.email}>"






