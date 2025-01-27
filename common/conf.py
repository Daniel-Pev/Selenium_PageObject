""""
Configuration class
"""

from creds import MyData


class Cfg:
    TOKEN = MyData.my_token  # Enter your token
    TRAINER_ID = MyData.my_trainer_id  # Enter your trainer id
    TRAINER_NAME = MyData.my_trainer_name
    TRAINER_CITY = MyData.my_city
    URL = 'https://pokemonbattle.ru'
    VALID = {
        'email': MyData.my_email,  # Enter valid mail
        'password': MyData.my_password  # Enter valid password
    }
