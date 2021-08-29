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


class Certificate:
    COURSE = "Course"
    INTERNSHIP = "Internship"
    PROJECT = "Project"
    OPEN_SOURCE = "Open Source"
    WORKSHOP = "Workshop"

    def __init__(
        self,
        issuer: str,
        url: str,
        date: str,
        type: str,
        name: str,
        viewableURL: str = None,
    ):
        self.issuer = issuer
        self.url = url
        self.date = date
        self.type = type
        self.name = name
        if viewableURL:
            self.viewableURL = viewableURL
        elif "drive.google.com" in self.url:
            self.viewableURL = self.url


class Skill:
    def __init__(self, name: str, url: str, level: int):
        self.name = name
        self.url = url
        self.level = level


class Experience:
    def __init__(
        self,
        name: str = None,
        weeks: int = None,
        place: str = None,
        type: str = None,
        start_date: str = None,
        end_date: str = None,
        techs: List[str] = None,
    ):
        self.name = name
        self.weeks = weeks
        self.place = place
        self.type = type
        self.end_date = end_date
        self.start_date = start_date
        self.techs = techs or []


class Project:
    OPEN_SOURCE = "Open Source"
    INTERNSHIP = "Internship"
    PRACTICE = "Practice"

    def __init__(
        self,
        name: str = "",
        desc: str = "",
        url: str = "",
        date: str = None,
        tech_used=None,
        type=None,
        domain="",
        image_url=None,
        source_url=None,
        features=None,
    ):
        self.name = name
        self.desc = desc
        self.url = url
        self.date = date
        self.techUsed = tech_used or []
        self.type = type
        self.domain = domain
        self.image_url = image_url
        self.sourceURL = source_url
        self.features = features or []


class StudyMaterial:
    # type
    BOOK = "Book"
    NOTE = "Notes"
    QUESTION_PAPER = "Question Paper"
    SYLLABUS = "Syllabus"

    # language
    ENGLISH = "English"
    HINDI = "Hindi"
    URDU = "Urdu"

    def __init__(
        self,
        name: str = None,
        link: str = None,
        standard: str = None,
        type: str = None,
        subject: str = None,
        branch: str = None,
        language=None,
        source=None,
    ):
        self.name = name
        self.link = link
        self.standard = standard
        self.type = type
        self.subject = subject
        self.branch = branch
        self.language = language
        self.source = source


class MaterialSummary:
    def __init__(
        self,
        standard=None,
        books=None,
        notes=None,
        questions=None,
        subjects=None,
        languages=None,
    ):
        self.standard = standard
        self.books = books
        self.notes = notes
        self.questions = questions
        self.subjects = subjects
        self.languages = languages
