from typing import List


class Poem:
    count = 0

    def __init__(self, name: str, url: str, date: str):
        Poem.count += 1
        self.name = name
        self.url = url
        self.date = date
        self.id = Poem.count


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
    def __init__(self, issuer: str, url: str, date: str, type: CertificateType, name: str, viewableURL: str = None):
        self.issuer = issuer
        self.url = url
        self.date = date
        self.type = type
        self.name = name
        if viewableURL:
            self.viewableURL = viewableURL
        elif 'drive.google.com' in self.url:
            self.viewableURL = self.url


class Skill:
    def __init__(self, name: str, url: str, level: int):
        self.name = name
        self.url = url
        self.level = level


class Experience:
    def __init__(self, name: str = None, weeks: int = None,
                 place: str = None, type: CertificateType = None,
                 date: str = None, techs: List[str] = []
                 ):
        self.name = name
        self.weeks = weeks
        self.place = place
        self.type = type
        self.date = date
        self.techs = techs


class ProjectType:
    OPEN_SOURCE = 'Open Source'
    INTERNSHIP = 'Internship'
    PRACTICE = 'Practice'


class Project:
    def __init__(self,
                 name: str = '', desc: str = '',
                 url: str = None, date: str = None, techUsed: List[str] = None,
                 type: ProjectType = None, domain=None, image_url=None,
                 ):
        self.name = name
        self.desc = desc
        self.url = url
        self.date = date
        self.techUsed = techUsed
        self.type = type
        self.domain = domain
        self.image_url = image_url
