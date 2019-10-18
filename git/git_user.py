
class GitUser:

    """
    Data class to encapsulate a git user. 
    """
    def __init__(self, name, email, signing_key=None):
        self._name = name
        self._email = email
        self._signing_key = signing_key


    # Defining getters (accessors) below

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def signing_key(self):
        return self._signing_key
    
    # And, setters (mutators)

    @name.setter
    def name(self, value):
        _name = value

    @email.setter
    def email(self, value):
        _email = value

    @signing_key.setter
    def signing_key(self, value):
        _signing_key = value


