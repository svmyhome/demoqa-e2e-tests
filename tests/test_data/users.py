from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Physics'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


class Hobby(Enum):
    Sports = '1'
    Reading = '2'
    Music = '3'


@dataclass
class User:
    first_name: str
    gender: Gender
    last_name: str = 'Ivanov'
    user_email: str = 'Ivanov@mail.ru'
    student_name: str = 'Ivan Ivanov'
    mobile: str = '1234567890'
    year: str = '2015'
    month: str = 'September'
    day: str = '30'
    subjects: Tuple[Subject] = (Subject.Maths, Subject.History)
    hobbies: Tuple[Hobby] = (Hobby.Sports, Hobby.Music)
    currentAddress = 'chbsdhjcb cdsjbcjsdbc jcsdjcndncj'
    state: str = 'Uttar Pradesh'
    city: str = 'Lucknow'


yuri = User(first_name='yuri', gender=Gender.Male)
