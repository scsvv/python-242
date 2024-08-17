class User:

    def __init__(self, 
                 login : str, 
                 name : str, 
                 surname : str, 
                 password : str, 
                 email : str | None = None, 
                 age : int | None = None,
                 ) -> None:
        
        self.login = login
        self.name = name
        self.surname = surname
        self.password = password
        self.email = email
        self.age = age
    
    def __get_all_keys(self):
        return tuple(self.__dict__.keys())   

    def set(self, **kwargs):
        keys = self.__get_all_keys()

        for kwarg, value in kwargs.items(): 
            if kwarg in keys:
                self.__setattr__(kwarg, value)
            else:
                self.__setattr__(f'{kwarg}_new', value)
    
    def get(self, key):
        keys = self.__get_all_keys()
        if key in keys:
            return self.__getattribute__(key)
        else: 
            return None


    def __str__(self) -> str:
        str_line = ""

        for key in self.__dict__:
            str_line += f'{key}: {self.__getattribute__(key)}\n'
        
        return str_line

user1 = User(
    login='scsvv', 
    name="Sam",
    surname="Skorobohatov", 
    password="hjkgfd", 
    email="d@d.com"
)

print(user1)

user1.set(name = "Sviat")

print(user1)

user1.set(auth_date = "13.03.2024")

print(user1)

print(user1.get('name'))
