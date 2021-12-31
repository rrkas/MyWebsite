from datetime import datetime
import pandas as pd
from website.models import *


class PoemData:
    def __init__(self):
        self.collections = []
        self.short_poems = []
        self.load_collections()
        self.load_short_poems()

    def load_collections(self):
        df = pd.read_csv(
            "https://raw.githubusercontent.com/rrkas/MyWebsiteData/main/data/poem_collections.csv"
        )
        df = df.sort_values(
            by="date",
            key=lambda col: [datetime.strptime(d, "%d/%m/%Y") for d in col],
            ascending=False,
        )
        for idx in range(len(df)):
            row = df.iloc[idx]
            poem = Poem.from_df_row(row, f"c{idx}")
            self.collections.append(poem)

    def load_short_poems(self):
        df = pd.read_csv(
            "https://raw.githubusercontent.com/rrkas/MyWebsiteData/main/data/poem_short.csv"
        )
        df = df.sort_values(
            by="date",
            key=lambda col: [datetime.strptime(d, "%d/%m/%Y") for d in col],
            ascending=False,
        )
        for idx in range(len(df)):
            row = df.iloc[idx]
            poem = Poem.from_df_row(row, f"s{idx}")
            self.short_poems.append(poem)

    def get_poem_by_id(self, id: str):
        poems = self.short_poems + self.collections
        poem = [p for p in poems if p.id == id]
        if len(poem) == 0:
            return None
        return poem[0]


class Technical:
    def __init__(self):
        self.skills = []
        self.certificates = []
        self.experiences = []
        self.load_skills()
        self.load_certificates()
        self.load_experiences()

    def load_skills(self):
        self.skills.extend(
            [
                Skill("Python", "skills/py.png", 4),
                Skill("Flutter", "skills/flutter.png", 4),
                Skill("Flask", "skills/flask.png", 3),
                Skill("Docker", "skills/docker.png", 3),
                Skill("C-Language", "skills/c.png", 3),
                Skill("C++", "skills/cpp.png", 3),
                Skill("Java", "skills/java.png", 3),
                Skill("Golang", "skills/go.png", 3),
                Skill("Android", "skills/android.png", 3),
                Skill("Kotlin", "skills/kt.png", 3),
            ]
        )

    def load_certificates(self):
        df = pd.read_csv(
            "https://raw.githubusercontent.com/rrkas/MyWebsiteData/main/data/technical_certificates.csv"
        )
        df = df.sort_values(
            by="date",
            key=lambda col: [datetime.strptime(d, "%d-%m-%Y") for d in col],
            ascending=False,
        )
        for row_idx in range(len(df)):
            row = df.iloc[row_idx]
            certificate = Certificate.from_df_row(row)
            self.certificates.append(certificate)

    def load_experiences(self):
        df = pd.read_csv(
            "https://raw.githubusercontent.com/rrkas/MyWebsiteData/main/data/technical_experience.csv"
        )
        df = df.sort_values(
            by="end_date",
            key=lambda col: [datetime.strptime(d, "%d-%m-%Y") for d in col],
            ascending=False,
        )
        for row_idx in range(len(df)):
            row = df.iloc[row_idx]
            expr = Experience.from_df_row(row)
            self.experiences.append(expr)


class Projects:
    def __init__(self):
        self.projects = []
        self.load_projects()

    def load_projects(self):
        df = pd.read_csv(
            "https://raw.githubusercontent.com/rrkas/MyWebsiteData/main/data/projects.csv"
        )
        df = df.sort_values(
            by="date",
            key=lambda col: [datetime.strptime(d, "%d-%m-%Y") for d in col],
            ascending=False,
        )
        for row_idx in range(len(df)):
            row = df.iloc[row_idx]
            project = Project.from_df_row(row)
            self.projects.append(project)


class StudyMaterials:
    def __init__(self):
        self.class01_12 = {}
        self.btech = {}

        self.load_class01_12()

    def load_class01_12(self):
        df = pd.read_csv(
            "https://raw.githubusercontent.com/rrkas/MyWebsiteData/main/data/study_materials_1_12.csv"
        )
        df = df.sort_values(
            by=["class", "subject", "language", "material_name"],
            ascending=True,
        ).reset_index()
        for class_num in df["class"].unique():
            materials = df[df["class"] == class_num]
            self.class01_12[class_num] = []
            for idx in range(len(materials)):
                row = materials.iloc[idx]
                material = StudyMaterial.from_df_row(row, idx)
                self.class01_12[class_num].append(material)

    def get_summary(self):
        temp = []
        for class_num in self.class01_12:
            materials = self.class01_12[class_num]
            temp.append(
                MaterialSummary(
                    standard=materials[0].standard,
                    books=len(
                        [
                            material
                            for material in materials
                            if material.type == StudyMaterial.BOOK
                        ]
                    ),
                    notes=len(
                        [
                            material
                            for material in materials
                            if material.type == StudyMaterial.NOTE
                        ]
                    ),
                    questions=len(
                        [
                            material
                            for material in materials
                            if material.type == StudyMaterial.QUESTION_PAPER
                        ]
                    ),
                    subjects=list(
                        sorted(set([material.subject for material in materials]))
                    ),
                    languages=list(
                        sorted(
                            set([material.language for material in materials]),
                        )
                    ),
                )
            )
        return temp

    def get_std_data(self, std: str):
        if std.startswith("Class"):
            cls = int(std.split("-")[1])
            return self.class01_12.get(cls)
