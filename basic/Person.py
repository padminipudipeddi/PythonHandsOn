class Person:

    def __init__(self, first_name, last_name, age):
        """
      constructor that initializes person attributes
      :param first_name:
      :param last_name:
      """
        # (_) UNDER SCORE IS USED FOR PRIVATE VARIABLES.
        self._first_name = first_name
        self.last_name = last_name
        self._age = age

    @property
    def get_first_name(self):
        return self._first_name

    @property
    def set_first_name(self, first_name):
        self._first_name = first_name


if __name__ == '__main__':
    p1 = Person('sai', 'saripalli', 35)
    print(p1.get_first_name)
    print(p1._age)

    p2 = Person('padmini', 'pudipeddi', 30)
    print(p2.get_first_name)
