from datetime import datetime
from typing import List


class Poem:
    def __init__(self, name: str, url: str, date: str, id: str):
        self.name = name
        self.url = url
        self.date = date
        self.id = id

    @classmethod
    def from_df_row(cls, row, id):
        return cls(
            date=row["date"],
            name=row["name"],
            url=f'https://drive.google.com/file/d/{row["gdrive_file_id"]}/preview?usp=drivesdk',
            id=id,
        )


class Education:
    def __init__(self, **kwargs):
        self.std = kwargs.get("std")
        self.institute = kwargs.get("institute")
        self.address = kwargs.get("address")
        self.start_year = kwargs.get("start_year")
        self.end_year = kwargs.get("end_year")
        self.score = kwargs.get("score")

    @classmethod
    def from_df_row(cls, row):
        return cls(
            std=row["std"],
            start_year=row["start_year"],
            end_year=row["end_year"],
            institute=row["institute"],
            address=row["address"],
            score=row["score"],
        )


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

    @classmethod
    def from_df_row(cls, row):
        return cls(
            date=row["date"],
            type=row["type"],
            issuer=row["issuer"],
            name=row["name"],
            url=f'https://drive.google.com/file/d/{row["gdrive_file_id"]}/preview?usp=drivesdk',
        )


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

    @classmethod
    def from_df_row(cls, row):
        days = (
                datetime(*(list(map(int, row["end_date"].split("-"))))[::-1])
                - datetime(*(list(map(int, row["start_date"].split("-"))))[::-1])
        ).days
        weeks = int(round((days // 7) / 4) * 4)
        return cls(
            start_date=row["start_date"],
            end_date=row["end_date"],
            type=row["type"],
            name=row["name"],
            place=row["place"],
            techs=row["tech_list"].split(","),
            weeks=weeks,
        )


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

    @classmethod
    def from_df_row(cls, row):
        return cls(
            date=row["date"],
            type=row["type"],
            domain=row["domain"],
            name=row["name"],
            url=row["url"],
            source_url=row["source_url"],
            tech_used=row["tech_list"].split(","),
            desc=row["desc"],
            features=row["features"].split(";"),
            image_url=row["image_url"] if str(row["image_url"]) != "nan" else None,
        )


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
            id: str = None,
            name: str = None,
            link: str = None,
            standard: str = None,
            type: str = None,
            subject: str = None,
            branch: str = None,
            language=None,
            source=None,
    ):
        self.id = id
        self.name = name
        self.link = link
        self.standard = standard
        self.type = type
        self.subject = subject
        self.branch = branch
        self.language = language
        self.source = source

    @classmethod
    def from_df_row(cls, row, idx, is_class=True):
        return cls(
            id=f"b{idx}",
            name=row["material_name"],
            link=f'https://drive.google.com/file/d/{row["gdrive_file_id"]}/preview?usp=drivesdk',
            standard=f'Class-{str(row["class"]).zfill(2)}'
            if is_class
            else row["class"],
            type=row["type"],
            subject=row["subject"],
            branch=row["branch"] if row.get("branch") else None,
            language=row["language"],
            source=row["source"],
        )


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
