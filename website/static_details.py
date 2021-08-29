from datetime import datetime

from website.models import *


class PersonalDetails:
    name = "Rohnak Agarwal"
    dob = "July 9, 2000"
    residence = "Cuttack, Odisha, India"
    mail_id = "rrka79wal@gmail.com"
    phone = "9658600961"
    github = "https://github.com/rrkas"
    linkedin = "https://www.linkedin.com/in/rohnak-agarwal-5558391a0/"
    qwiklabs = "https://google.qwiklabs.com/public_profiles/4b318807-5a88-4858-8fd1-3230f22b21d3"
    credly = "https://www.credly.com/users/rohnak-agarwal/badges"
    hobbies = ["Poems", "Coding"]
    sports = "Badminton"
    education = [
        Education(
            "B.Tech. (CSE)",
            "College of Engineering and Technology (CET)",
            "Ghatikia, Bhubaneswar",
            2022,
            str(round(9.44 * 9.5, 2)),
        ),
        Education("Class-12", "D.A.V. Public School", "CDA-6, Cuttack", 2018, "92.40"),
        Education("Class-10", "D.A.V. Public School", "CDA-6, Cuttack", 2016, "95.00"),
    ]
    cv_url = "https://drive.google.com/file/d/1P22vMgAFCZf6H01rAoJX15y2QfAplfAn/preview?usp=drivesdk"


class PoemData:
    collections = [
        Poem(
            "The Verse Of facts",
            "https://drive.google.com/file/d/13Jc98bZu_soi23WsFm7V6y7qRQiMVejb/preview?usp=drivesdk",
            "14/05/2019",
        )
    ]
    short_poems = [
        Poem(
            "The Sea Shore",
            "https://drive.google.com/file/d/1-9zF5XN16AAQnLB7osR24TELVlPImg4B/preview?usp=drivesdk",
            "11/01/2019",
        ),
        Poem(
            "The Small Playground",
            "https://drive.google.com/file/d/1-GpLka6xVZIcHew4Nn-D2YXDHnsuXbRM/preview?usp=drivesdk",
            "12/01/2019",
        ),
        Poem(
            "The Last Breath",
            "https://drive.google.com/file/d/1-Z55FNk-01Bx47ji4ZS9n9BgUpZdGkyG/preview?usp=drivesdk",
            "18/01/2019",
        ),
        Poem(
            "The Thirst of Glimpse",
            "https://drive.google.com/file/d/1-XjULOOhLe_TInMnU3DgP6RPipd6luhl/preview?usp=drivesdk",
            "19/01/2019",
        ),
        Poem(
            "The Mighty Knights",
            "https://drive.google.com/file/d/1-V-QQCssK02uG1wVg6zOz5uL6FFdAVhn/preview?usp=drivesdk",
            "17/02/2019",
        ),
        Poem(
            "Will you still stay beside me?",
            "https://drive.google.com/file/d/1-044SR20kwWZ9Z2DHu8lDL_6Gbvr2rYW/preview?usp=drivesdk",
            "27/03/2019",
        ),
        Poem(
            "Tug Of War",
            "https://drive.google.com/file/d/1--W51nOg5-Bmv-ND046y5low8ZMUmlfI/preview?usp=drivesdk",
            "02/07/2019",
        ),
        Poem(
            "द्रौपदी की रक्षा",
            "https://drive.google.com/file/d/1-1kg3eFyj0j7M6U7PUbOOuJKHh6H_Nm4/preview?usp=drivesdk",
            "15/08/2019",
        ),
        Poem(
            "So Glad It Happened",
            "https://drive.google.com/file/d/1-jWrmkpGGScRhNvftyFIpqyzax02d7ux/preview?usp=drivesdk",
            "25/08/2019",
        ),
        Poem(
            "The Great Erosion",
            "https://drive.google.com/file/d/1-8NIHojMLIC0tT3AgSuZtC18qDd-n0FB/preview?usp=drivesdk",
            "07/09/2019",
        ),
        Poem(
            "The Ultimate Hunter",
            "https://drive.google.com/file/d/1-06WdtXkqvQx04FH9Zvrtr060t4l6uZj/preview?usp=drivesdk",
            "23/10/2019",
        ),
        Poem(
            "Far and Near",
            "https://drive.google.com/file/d/1-cGbRweEJeV3iNb_Nc0jLvUJ9ilmNneL/preview?usp=drivesdk",
            "17/11/2019",
        ),
        Poem(
            "Listen to Understand",
            "https://drive.google.com/file/d/1-kFJtWSxA39CT3TfQa0ZrmAJJcbgjZuf/preview?usp=drivesdk",
            "18/11/2019",
        ),
        Poem(
            "The Reins To Emotions",
            "https://drive.google.com/file/d/1-sCWIPN_xLvvuwN_IpGcBFPKybXxO4PM/preview?usp=drivesdk",
            "20/11/2019",
        ),
        Poem(
            "Long Way to Go Alone",
            "https://drive.google.com/file/d/1-wKwFPdmc8pmnkpX78aJszyFqEIrjgac/preview?usp=drivesdk",
            "25/11/2019",
        ),
        Poem(
            "Stuck in the Past",
            "https://drive.google.com/file/d/10-8i2Z1pLksVF_tI8pa-dbUlMbCdQpyT/preview?usp=drivesdk",
            "27/11/2019",
        ),
        Poem(
            "Not of My Kind",
            "https://drive.google.com/file/d/100LoxSyEJN3zYby0ePg-vyMb7T240b_o/preview?usp=drivesdk",
            "28/11/2019",
        ),
        Poem(
            "Being Low",
            "https://drive.google.com/file/d/100nI0IOrAXkSHgn9oJvlPuNw85Zu1rom/preview?usp=drivesdk",
            "29/11/2019",
        ),
        Poem(
            "And we call ourselves HUMANS?",
            "https://drive.google.com/file/d/105pb_AmBRy_NxefAiZh5zMCT6GWU4NAT/preview?usp=drivesdk",
            "30/11/2019",
        ),
        Poem(
            "My kingdom of darkness",
            "https://drive.google.com/file/d/112c5baNJbtqqXzrkYDpAjzKaQO3J1h8y/preview?usp=drivesdk",
            "15/12/2019",
        ),
        Poem(
            "Grinded",
            "https://drive.google.com/file/d/13K0O3E6NkaDtKdFR-lUltgk-E4czt0HV/preview?usp=drivesdk",
            "17/12/2019",
        ),
        Poem(
            "कुछ रंग ऐसे भी",
            "https://drive.google.com/file/d/13PYkQuE7HbQLSHkgIzzMiEIhN18RXEI1/preview?usp=drivesdk",
            "09/03/2020",
        ),
        Poem(
            "Life is?",
            "https://drive.google.com/file/d/100zQs_aEkCB5rBluBtjFOqxwSsL8ESRD/preview?usp=drivesdk",
            "01/03/2021",
        ),
        Poem(
            "Reality of illusions",
            "https://drive.google.com/file/d/1CgBj5kUOSh1TNbtPSUIW4IaPrt07HFde/preview?usp=drivesdk",
            "19/03/2021",
        ),
    ]

    @staticmethod
    def get_short_poems():
        PoemData.short_poems.sort(
            key=lambda x: datetime.strptime(x, format="%d/%m/%Y"), reverse=True
        )
        return PoemData.short_poems

    @staticmethod
    def get_poem_by_id(id: int):
        poems = PoemData.short_poems + PoemData.collections
        poem = [p for p in poems if p.id == id]
        if len(poem) == 0:
            return None
        return poem[0]


class Technical:
    skills = [
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
    certificates = [
        Certificate(
            issuer="Cisco Networking Academy",
            type=Certificate.COURSE,
            name="DevNet Associate",
            date="28-05-2021",
            url="https://drive.google.com/file/d/1p4hTkd_A6uj2-eETRkI-FEw-bwJT_xTI/preview?usp=drivesdk",
        ),
        Certificate(
            issuer="SAP SE",
            type=Certificate.COURSE,
            url="https://drive.google.com/file/d/14I2e3-p35aufVhZPiYCF8uxar4Iy-Kqq/preview?usp=drivesdk",
            date="23-05-2021",
            name="SAP Certified Development Associate - ABAP with SAP NetWeaver 7.50",
            # viewableURL='https://images.credly.com/
        ),
        Certificate(
            issuer="Coursera",
            type=Certificate.COURSE,
            date="08-04-2020",
            url="https://drive.google.com/file/d/1ZzQgM50shU-kqnIz3jAlqYOUJxQ0kZ6i/preview?usp=drivesdk",
            name="Python for Everybody",
        ),
        Certificate(
            issuer="Central Tool Room & Training Centre (CTTC)",
            type=Certificate.INTERNSHIP,
            date="29-06-2019",
            name="Core Java",
            url="https://drive.google.com/file/d/1JbJVyiHy3jfMto7BqRWynfHYZJLVLvYu/preview?usp=drivesdk",
        ),
        Certificate(
            issuer="KIDE",
            type=Certificate.OPEN_SOURCE,
            date="06-10-2020",
            name="HactoberFest 2020",
            url="https://drive.google.com/file/d/19ccEi8Y-3F65vccfJxDFzaTt5EV_pdem/preview?usp=drivesdk",
        ),
        Certificate(
            issuer="PriME Technology PVT Ltd.",
            type=Certificate.INTERNSHIP,
            date="16-09-2020",
            name="Flutter App Internship - Karmik Suraksha",
            url="https://drive.google.com/file/d/12CWAsswL8Z9-TCsSnJy1RM8H7ze7jc8a/preview?usp=drivesdk",
        ),
        Certificate(
            issuer="PriME Technology PVT Ltd.",
            type=Certificate.INTERNSHIP,
            date="02-01-2021",
            name="Flutter App Internship - Utkristh Gunnavatta",
            url="https://drive.google.com/file/d/1qzKDrxgjYXx6Cmj3lZyCjWNwvabEWdV9/preview?usp=drivesdk",
        ),
        Certificate(
            issuer="LIT & Spectrum",
            type=Certificate.WORKSHOP,
            date="20-10-2019",
            name="Python Workshop",
            url="https://drive.google.com/file/d/1uhPKTIrDi3F-1N_eAQdq5UbKqB3BOJoH/preview?usp=drivesdk",
        ),
        Certificate(
            issuer="Nimble Tech & Spectrum",
            type=Certificate.INTERNSHIP,
            date="31-05-2020",
            name="Android App Development",
            url="https://drive.google.com/file/d/1WASwDy078AvQYAUozwJV1nXBTVJ1ORJj/preview?usp=drivesdk",
        ),
        Certificate(
            issuer="Cisco Networking Academy",
            type=Certificate.COURSE,
            date="23-04-2021",
            name="Cybersecurity Essentials",
            url="https://drive.google.com/file/d/1UTAA-l4Rcgj1RzIrqW-WH5AeHzZnZc8y/preview?usp=drivesdk",
        ),
        Certificate(
            issuer="Cisco Networking Academy",
            type=Certificate.COURSE,
            date="23-04-2021",
            name="Introduction to Cybersecurity",
            url="https://drive.google.com/file/d/1XQxYHHQUgbPtY5mV6Ixc9XQZb72GNAUx/preview?usp=drivesdk",
        ),
        Certificate(
            issuer="Cisco Networking Academy",
            type=Certificate.COURSE,
            date="30-03-2021",
            name="Introduction to Packet Tracer",
            url="https://drive.google.com/file/d/1UpTJ5_0f_cfXWO6Gft06qmqZkJciYX8Z/preview?usp=drivesdk",
        ),
        Certificate(
            issuer="OpenEDG Python Institute (Cisco)",
            type=Certificate.COURSE,
            date="13-03-2021",
            name="Programming Essentials in Python (PCAP)",
            url="https://drive.google.com/file/d/1OOZq73deaJrMVNiNO4eRTPCu7D-UjVMO/preview?usp=drivesdk",
        ),
        Certificate(
            url="https://drive.google.com/file/d/1cenLYhNJWVyJ5gXWUELNTAVTL31jMp1N/preview?usp=drivesdk",
            issuer="Cisco Networking Academy",
            date="03-05-2021",
            name="CCNAv7: Introduction to Networks",
            type=Certificate.COURSE,
        ),
    ]
    experiences = [
        Experience(
            name="Flutter Mobile App Intern",
            type=Certificate.INTERNSHIP,
            weeks=8,
            place="PriME Technology PVT Ltd.",
            start_date="15-07-2020",
            end_date="16-09-2020",
            techs=["Flutter", "Firebase", "Dart"],
        ),
        Experience(
            name="Flutter Mobile App Intern",
            type=Certificate.INTERNSHIP,
            weeks=4,
            place="PriME Technology PVT Ltd.",
            start_date="01-12-2020",
            end_date="02-01-2021",
            techs=["Flutter", "Firebase", "Dart"],
        ),
        Experience(
            name="HactoberFest 2020",
            type=Certificate.OPEN_SOURCE,
            weeks=4,
            place="DigitalOcean",
            start_date="01-10-2020",
            end_date="31-10-2020",
            techs=["Flutter"],
        ),
        Experience(
            name="Core Java Student Intern",
            type=Certificate.INTERNSHIP,
            weeks=4,
            place="Central Tool Room and Training Centre (CTTC)",
            start_date="01-06-2019",
            end_date="29-06-2019",
            techs=["Java"],
        ),
        Experience(
            name="Intern",
            type=Certificate.INTERNSHIP,
            weeks=4 * 4,
            place="Banglore (Work from Home)",
            start_date="15-03-2021",
            techs=["Python", "Angular", "Docker", "ElasticSearch"],
        ),
    ]

    @staticmethod
    def get_certificates():
        Technical.certificates.sort(
            key=lambda x: datetime.strptime(x.date, "%d-%m-%Y"), reverse=True
        )
        return Technical.certificates

    @staticmethod
    def get_experiences():
        Technical.experiences.sort(
            key=lambda x: datetime.strptime(x.start_date, "%d-%m-%Y"), reverse=True
        )
        return Technical.experiences


class Projects:
    projects = [
        Project(
            name="{api-hub}",
            date="14-08-2021",
            type=Project.PRACTICE,
            url="https://rrka7apihub.herokuapp.com/",
            source_url="https://github.com/rrkas/api-hub",
            tech_used=["Flask", "Bootstrap", "HTML", "CSS"],
            desc="An API for common algorithms.",
            features=[
                "Detailed documentation",
                "Simple request and response structures",
                "Insightful responses",
            ],
            domain="Web App",
        ),
        Project(
            name="Utkristh Gunnavatta",
            date="02-01-2021",
            type=Project.INTERNSHIP,
            url="https://play.google.com/store/apps/details?id=com.prime.qa_app",
            tech_used=["Flutter", "Firebase", "Dart"],
            desc="This project was aimed to design a safety monitoring and feedback.",
            domain="Mobile App",
            features=[
                "Google Login",
                "Process Flow",
                "Monitoring and feedback",
                "Report Generation (excel)",
                "Distributed access to different level of users",
            ],
            image_url="https://play-lh.googleusercontent.com/grAVOkieIxLWIeho-EQ7V7_qfO7lxnYKoYr5MWYbkk-aJG5uYVoV77GnpajVgd9X8c8=s180-rw",
        ),
        Project(
            name="Karmik Suraksha",
            date="16-09-2020",
            type=Project.INTERNSHIP,
            url="https://play.google.com/store/apps/details?id=com.prime.feedback_app",
            tech_used=["Flutter", "Firebase", "Dart"],
            desc="This project was aimed to design a process-flow, review and feedback.",
            domain="Mobile App",
            features=[
                "Google Login",
                "Process Flow",
                "Monitoring and feedback",
                "Report Generation (excel)",
                "Distributed access to different level of users",
            ],
            image_url="https://play-lh.googleusercontent.com/aXI4e6dfNht3fCbwwBWSjfVBPmbwRpuVoQrRAvyZZMnslvOpnpgcpnWIfBEEXzF4a1o=s180-rw",
        ),
        Project(
            name="CET-B Mobile App",
            date="11-01-2021",
            type=Project.INTERNSHIP,
            url="https://play.google.com/store/apps/details?id=com.coeaibbsr.cetb",
            tech_used=["Flutter", "Firebase", "Dart"],
            desc="This project was aimed to bring CET college and its resources at fingertips of the students. "
            "It is currently being used by the students. "
            "This app provides all information about courses, scholarships, map of college and room arrangements.",
            domain="Mobile App",
            features=[
                "Google Login",
                "Distributed access to different level of users",
                "Campus Map with live location of user and landmarks",
                "Complain register",
                "Clubs and groups of college",
                "ChatBot and CommandBot",
                "Visitor's login",
                "Courses, Placements, Scholarships, Digital libraries",
                "Visitor Pass generation and approval",
            ],
            image_url="https://play-lh.googleusercontent.com/WDOfe5xQjRtZpuCEEl03I9en7vk8vmlQQeZdnBe6zDwT7tXTYuZKXurdood3ecLh4Q=s180-rw",
        ),
        Project(
            name="FlaskBlog",
            url="https://rrka3flaskblog.herokuapp.com/",
            type=Project.PRACTICE,
            date="19-05-2021",
            tech_used=["Python", "Flask", "SQLite", "HTML", "CSS"],
            domain="Web App",
            features=["User register/login", "Post CRUD", "User Profile", "Pagination"],
            desc="This project aims at serving as a blog to a community. "
            "Here users can register and login and send blogs. Users can edit and delete their blogs.",
            source_url="https://github.com/rrkas/PythonFlaskBlog",
        ),
        Project(
            name="Images to PDF",
            url="https://rrka4imagestopdf.herokuapp.com/",
            type=Project.PRACTICE,
            date="22-05-2021",
            tech_used=["Python", "Flask", "HTML", "CSS"],
            domain="Web App",
            features=["Image to PDF", "Space efficient"],
            desc="This project aims at converting images to PDF. "
            "This app can be found useful while making document "
            "of assignments, reports, etc which are in image formats.",
            source_url="https://github.com/rrkas/ImgToPdfFlask",
        ),
        Project(
            name="PDF Master",
            date="12-06-2021",
            type=Project.PRACTICE,
            url="https://rrka6pdfmaster.herokuapp.com/",
            source_url="https://github.com/rrkas/PdfMaster",
            tech_used=["Django", "Python", "HTML", "CSS", "JS"],
            domain="Web App",
            desc="A web app for manipulating and operating on PDFs. Features: PDF Merge, Images to PDF",
            features=[
                "Merge multiple PDFs",
                "Convert Images to PDF",
                "Space efficient",
            ],
        ),
    ]

    @staticmethod
    def get_projects():
        Projects.projects.sort(
            key=lambda x: datetime.strptime(x.date, "%d-%m-%Y"), reverse=True
        )
        for project in Projects.projects:
            project.features.sort()
        return Projects.projects


class StudyMaterials:
    class1_10 = [
        [
            StudyMaterial(
                name="Raindrops",
                type=StudyMaterial.BOOK,
                subject="English",
                link="https://drive.google.com/file/d/1oeutp5CMzEOxJcUw3aN4Pr3j75jiAIWL/view?usp=sharing",
                standard="Class-01",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Marigold",
                type=StudyMaterial.BOOK,
                subject="English",
                link="https://drive.google.com/file/d/1XthnoDAG4pA4-kzpWOyeHKBnvcasUqML/view?usp=sharing",
                standard="Class-01",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Rimjhim",
                type=StudyMaterial.BOOK,
                subject="Hindi",
                link="https://drive.google.com/file/d/1b2ESWdZEAbVHF1-F5__ZqYKlwJFssie-/view?usp=sharing",
                standard="Class-01",
                language=StudyMaterial.HINDI,
                source="NCERT",
            ),
            StudyMaterial(
                name="Ganit ka Jaadu",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/1r14CU9awF2xVf94ZtOxmTWhSOqhYu_8X/view?usp=sharing",
                standard="Class-01",
                language=StudyMaterial.HINDI,
                source="NCERT",
            ),
            StudyMaterial(
                name="Math Magic",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/1EFQGCcNJeCHCOhM44iQcJEjZXEryJcca/view?usp=sharing",
                standard="Class-01",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Riyazi ka Jadoo",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/1SDCXJDEa83fspYI2Cjp8jbMhLn1OnqCL/view?usp=sharing",
                standard="Class-01",
                language=StudyMaterial.URDU,
                source="NCERT",
            ),
            StudyMaterial(
                name="Ibtedai Urdu",
                type=StudyMaterial.BOOK,
                subject="Urdu",
                link="https://drive.google.com/file/d/1l332fany-uORCQuGpUCoYEc3abs4_h81/view?usp=sharing",
                standard="Class-01",
                language=StudyMaterial.URDU,
                source="NCERT",
            ),
        ],
        [
            StudyMaterial(
                name="Raindrops",
                type=StudyMaterial.BOOK,
                subject="English",
                link="https://drive.google.com/file/d/1Q7NOLPCWozzJDXp9gtIPG1LOMrXzM2L3/view?usp=sharing",
                standard="Class-02",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Marigold",
                type=StudyMaterial.BOOK,
                subject="English",
                link="https://drive.google.com/file/d/1A5pwcac-rfoveBtWxTCS9_KsxHS1vQSL/view?usp=sharing",
                standard="Class-02",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Rimjhim",
                type=StudyMaterial.BOOK,
                subject="Hindi",
                link="https://drive.google.com/file/d/1zhkahiaaEDBqef48GmamWE7c3vT6ce38/view?usp=sharing",
                standard="Class-02",
                language=StudyMaterial.HINDI,
                source="NCERT",
            ),
            StudyMaterial(
                name="Ganit ka Jadoo",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/1P6DmywtJBGN1-p6GCifYK25-AXKW8wz4/view?usp=sharing",
                standard="Class-02",
                language=StudyMaterial.HINDI,
                source="NCERT",
            ),
            StudyMaterial(
                name="Math Magic",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/18IRM1GgX18lrwBrTdq_gLQO-ZHgjndJ9/view?usp=sharing",
                standard="Class-02",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Riyazi ka Jadoo",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/13X3Bpz-7-MNAG4D7siFeEj5SXA8m4no0/view?usp=sharing",
                standard="Class-02",
                language=StudyMaterial.URDU,
                source="NCERT",
            ),
            StudyMaterial(
                name="Ibtedai Urdu",
                type=StudyMaterial.BOOK,
                subject="Urdu",
                link="https://drive.google.com/file/d/1PZ5JSJOfdyl8LTK3p7ESGoanbZ8eqgSj/view?usp=sharing",
                standard="Class-02",
                language=StudyMaterial.URDU,
                source="NCERT",
            ),
        ],
        [
            StudyMaterial(
                name="Marigold",
                type=StudyMaterial.BOOK,
                subject="English",
                link="https://drive.google.com/file/d/1j7U5E4P6jl5-nVB0ixEvzqDfOETeFlHO/view?usp=sharing",
                standard="Class-03",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Rimjhim",
                type=StudyMaterial.BOOK,
                subject="Hindi",
                link="https://drive.google.com/file/d/17bjS-cEnctAOr960Ift0_bpB2xemA7Qt/view?usp=sharing",
                standard="Class-03",
                language=StudyMaterial.HINDI,
                source="NCERT",
            ),
            StudyMaterial(
                name="Ganit ka Jadoo",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/1GHcRrtjwISXQSr42MR1lJ7Ppfwja0UA-/view?usp=sharing",
                standard="Class-03",
                language=StudyMaterial.HINDI,
                source="NCERT",
            ),
            StudyMaterial(
                name="Math Magic",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/1_K08o6BJbBtks63Q9cAP3Ez69tsFrSh2/view?usp=sharing",
                standard="Class-03",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Aas Paas",
                type=StudyMaterial.BOOK,
                subject="Environmental Studies",
                link="https://drive.google.com/file/d/1tuPctRGSdMqP54gYEG1rj05ln0unG25m/view?usp=sharing",
                standard="Class-03",
                language=StudyMaterial.HINDI,
                source="NCERT",
            ),
            StudyMaterial(
                name="Looking Around",
                type=StudyMaterial.BOOK,
                subject="Environmental Studies",
                link="https://drive.google.com/file/d/1xqMJE6sQLQNzec61xSWzatNVdemWmton/view?usp=sharing",
                standard="Class-03",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Riyazi ka Jadoo",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/1unyvtmYLkw7xO3srJfc9qN23z1qNXRqj/view?usp=sharing",
                standard="Class-03",
                language=StudyMaterial.URDU,
                source="NCERT",
            ),
            StudyMaterial(
                name="Aas Paas (Urdu)",
                type=StudyMaterial.BOOK,
                subject="Environmental Studies",
                link="https://drive.google.com/file/d/1DxDKJUIqmE9URp7_r87bIH5AcVuS1dm0/view?usp=sharing",
                standard="Class-03",
                language=StudyMaterial.URDU,
                source="NCERT",
            ),
            StudyMaterial(
                name="Ibtedai Urdu",
                type=StudyMaterial.BOOK,
                subject="Urdu",
                link="https://drive.google.com/file/d/1W_GAhPPrL14Nubm8-kShyJAXHiUboCW0/view?usp=sharing",
                standard="Class-03",
                language=StudyMaterial.URDU,
                source="NCERT",
            ),
        ],
        [
            StudyMaterial(
                name="Marigold",
                type=StudyMaterial.BOOK,
                subject="English",
                link="https://drive.google.com/file/d/1bSKHO_5kEjULyaN-SMaWJeOr89VxNSMm/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Rimjhim",
                type=StudyMaterial.BOOK,
                subject="Hindi",
                link="https://drive.google.com/file/d/1Xi7iVpn7pt_WFyaBOYH0C_DqhZuq1ghZ/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.HINDI,
                source="NCERT",
            ),
            StudyMaterial(
                name="Ganit ka Jadoo",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/12i0odfIW20OSFLc_LuOfmma135Y2MY57/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.HINDI,
                source="NCERT",
            ),
            StudyMaterial(
                name="Math Magic",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/1Pq64napVsSiO8U1AIk4IfvLUq6kutIpJ/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Aas Paas",
                type=StudyMaterial.BOOK,
                subject="Environmental Studies",
                link="https://drive.google.com/file/d/1sQQpaRVMBzVwz3uB17JwsK56XuuUy7wQ/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.HINDI,
                source="NCERT",
            ),
            StudyMaterial(
                name="Looking Around",
                type=StudyMaterial.BOOK,
                subject="Environmental Studies",
                link="https://drive.google.com/file/d/1Xi7iVpn7pt_WFyaBOYH0C_DqhZuq1ghZ/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Riyazi ka Jadoo",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/1x4e86EJm63kg9HzPWpu76GnDq9xFSn-D/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.URDU,
                source="NCERT",
            ),
            StudyMaterial(
                name="Aas Paas (Urdu)",
                type=StudyMaterial.BOOK,
                subject="Environmental Studies",
                link="https://drive.google.com/file/d/1INxUGZe0Uym3Puph3RmMTbfZPi4afrQA/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.URDU,
                source="NCERT",
            ),
            StudyMaterial(
                name="Ibtedai Urdu",
                type=StudyMaterial.BOOK,
                subject="Urdu",
                link="https://drive.google.com/file/d/1-la7FJEpIVtFsNAdqkM5IPRDWWVj4jyH/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.URDU,
                source="NCERT",
            ),
        ],
        [
            StudyMaterial(
                name="Marigold",
                type=StudyMaterial.BOOK,
                subject="English",
                link="https://drive.google.com/file/d/1MZtAP3VE1J4qQzQ8guppSYFFQfs8Ccyn/view?usp=sharing",
                standard="Class-05",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Rimjhim",
                type=StudyMaterial.BOOK,
                subject="Hindi",
                link="",
                standard="Class-05",
                language=StudyMaterial.HINDI,
                source="NCERT",
            ),
            StudyMaterial(
                name="Ganit ka Jadoo",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/12i0odfIW20OSFLc_LuOfmma135Y2MY57/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.HINDI,
                source="NCERT",
            ),
            StudyMaterial(
                name="Math Magic",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/1Pq64napVsSiO8U1AIk4IfvLUq6kutIpJ/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Aas Paas",
                type=StudyMaterial.BOOK,
                subject="Environmental Studies",
                link="https://drive.google.com/file/d/1sQQpaRVMBzVwz3uB17JwsK56XuuUy7wQ/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.HINDI,
                source="NCERT",
            ),
            StudyMaterial(
                name="Looking Around",
                type=StudyMaterial.BOOK,
                subject="Environmental Studies",
                link="https://drive.google.com/file/d/1Xi7iVpn7pt_WFyaBOYH0C_DqhZuq1ghZ/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.ENGLISH,
                source="NCERT",
            ),
            StudyMaterial(
                name="Riyazi ka Jadoo",
                type=StudyMaterial.BOOK,
                subject="Maths",
                link="https://drive.google.com/file/d/1x4e86EJm63kg9HzPWpu76GnDq9xFSn-D/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.URDU,
                source="NCERT",
            ),
            StudyMaterial(
                name="Aas Paas (Urdu)",
                type=StudyMaterial.BOOK,
                subject="Environmental Studies",
                link="https://drive.google.com/file/d/1INxUGZe0Uym3Puph3RmMTbfZPi4afrQA/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.URDU,
                source="NCERT",
            ),
            StudyMaterial(
                name="Ibtedai Urdu",
                type=StudyMaterial.BOOK,
                subject="Urdu",
                link="https://drive.google.com/file/d/1-la7FJEpIVtFsNAdqkM5IPRDWWVj4jyH/view?usp=sharing",
                standard="Class-04",
                language=StudyMaterial.URDU,
                source="NCERT",
            ),
        ],
    ]

    @staticmethod
    def get_summary():
        temp = []
        for materials in StudyMaterials.get_1_10_materials():
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

    @staticmethod
    def get_1_10_materials():
        temp = StudyMaterials.class1_10
        for classx in temp:
            classx.sort(key=lambda x: (x.standard + x.subject + x.name))
        return temp

    @staticmethod
    def get_std_data(std: str):
        if std.startswith("Class"):
            cls = int(std.split("-")[1]) - 1
            return StudyMaterials.get_1_10_materials()[cls]
