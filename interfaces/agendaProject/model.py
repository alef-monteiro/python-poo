class Contact:
    def __init__(self):
        self.id = None
        self.name = None
        self.email = None
        self.cell_phone = None
        self.zip_code = None
        self.street = None
        self.neighborhood = None
        self.city = None
        self.state = None

        @property
        def id(self):
            return self._id

        @id.setter
        def id(self, value):
            self._id = value

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            self._name = value

        @property
        def email(self):
            return self._email

        @email.setter
        def email(self, value):
            self._email = value

        @property
        def cell_phone(self):
            return self._cell_phone

        @cell_phone.setter
        def cell_phone(self, value):
            self._cell_phone = value

        @property
        def zip_code(self):
            return self._zip_code

        @zip_code.setter
        def zip_code(self, value):
            self._zip_code = value

        @property
        def street(self):
            return self._street

        @street.setter
        def street(self, value):
            self._street = value

        @property
        def neighborhood(self):
            return self._neighborhood

        @neighborhood.setter
        def neighborhood(self, value):
            self._neighborhood = value

        @property
        def city(self):
            return self._city

        @city.setter
        def city(self, value):
            self._city = value

        @property
        def state(self):
            return self._state

        @state.setter
        def state(self, value):
            self._state = value

