class Poem:
    def __init__(self, name: str, url: str, date: str):
        self.name = name
        self.url = url
        self.date = date


class Education:
    def __init__(self, std: str, school: str, address: str, year: int, score: str):
        self.std = std
        self.school = school
        self.address = address
        self.year = year
        self.score = score


class CertificateType:
    COURSE = 'Course'
    INTERNSHIP = 'Internship'
    PROJECT = 'Project'
    OPEN_SOURCE = 'Open Source'
    WORKSHOP = 'Workshop'


class Certificate:
    def __init__(self, issuer: str, filepathstatic: str, date: str, type: CertificateType, name: str):
        self.issuer = issuer
        self.url = filepathstatic
        self.date = date
        self.type = type
        self.name = name


class Skill:
    def __init__(self, name: str, url: str, level: int):
        self.name = name
        self.url = url
        self.level = level


class Experience:
    def __init__(self, name: str, months: int, place: str, type: CertificateType, date:str):
        self.name = name
        self.months = months
        self.place = place
        self.type = type
        self.date = date


class Project:
    def __init__(self, name: str, desc: str, url: str, date: str):
        self.name = name
        self.desc = desc
        self.url = url
        self.date = date
