from faker import Faker

fake = Faker("Ru-ru")


class RegisterData:
    def __init__(
        self,
        login=None,
        password=None,
        email=None,
        email_2=None,
        name=None,
        surname=None,
        city=None,
    ):
        self.login = login
        self.password = password
        self.email = email
        self.email_2 = email_2
        self.name = name
        self.surname = surname
        self.city = city

    @staticmethod
    def random():
        login = fake.email()
        password = fake.password()

        email = fake.email()
        name = fake.first_name()
        surname = fake.last_name()
        city = fake.city()
        return RegisterData(
            login=login,
            password=password,
            email=email,
            email_2=email,
            name=name,
            surname=surname,
            city=city,
        )
