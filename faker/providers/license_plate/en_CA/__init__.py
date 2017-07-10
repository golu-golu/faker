# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as LicensePlateProvider


class Provider(LicensePlateProvider):
    # from https://www.revolvy.com/main/index.php?s=Canadian%20licence%20plate%20designs%20and%20serial%20formats
    formats = (
        # Alberta
        '???-####',
        # BC
        '??# ##?',
        '?? ####',
        # Manitoba
        '??? ###',
        # New Brunswick
        '??? ###',
        # Newfoundland and Labrador
        '??? ###',
        # NWT
        '######',
        # Nova Scotia
        '??? ###',
        # Nunavut
        '### ###',
        # Ontario
        '### ???',
        '???? ###',
        '??# ###',
        '### #??',
        '?? ####',
        'GV??-###',
        # PEI
        '## ##??',
        # Quebec
        '?## ???',
        # Saskatchewan
        '### ???',
        # Yukon
        '???##'
    )