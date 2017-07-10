# coding=utf-8

localized = True

from .. import BaseProvider
from string import ascii_uppercase
import re

class Provider(BaseProvider):
    formats = ()
    @classmethod
    def license_plate(cls):
        temp = re.sub(r'\?',
            lambda x: cls.random_element(ascii_uppercase),
            cls.random_element(cls.formats))
        return cls.numerify(temp)
