from datetime import datetime

from website.models import *


class PersonalDetails:
    name = 'Rohnak Agarwal'
    dob = 'July 9, 2000'
    residence = 'Cuttack, Odisha, India'
    mail_id = 'rrka79wal@gmail.com'
    phone = '9658600961'
    github = 'https://github.com/rrkas'
    linkedin = 'https://www.linkedin.com/in/rohnak-agarwal-5558391a0/'
    qwiklabs = 'https://google.qwiklabs.com/public_profiles/4b318807-5a88-4858-8fd1-3230f22b21d3'
    hobbies = ['Poems', 'Coding']
    sports = 'Badminton'
    education = [
        Education(
            'B.Tech. (CSE)',
            'College of Engineering and Technology (CET)',
            'Ghatikia, Bhubaneswar',
            2022,
            str(round(9.44 * 9.5, 2)),
        ),
        Education('Class 12', 'D.A.V. Public School', 'CDA-6, Cuttack', 2018, '92.40'),
        Education('Class 10', 'D.A.V. Public School', 'CDA-6, Cuttack', 2016, '95.00'),
    ]


class PoemData:
    collections = [
        Poem(
            'The Verse Of facts',
            'https://drive.google.com/file/d/13Jc98bZu_soi23WsFm7V6y7qRQiMVejb/preview?usp=drivesdk',
            '14/05/2019',
        )
    ]
    short_poems = [
        Poem(
            'The Sea Shore',
            'https://drive.google.com/file/d/1-9zF5XN16AAQnLB7osR24TELVlPImg4B/preview?usp=drivesdk',
            '11/01/2019',
        ),
        Poem(
            'The Small Playground',
            'https://drive.google.com/file/d/1-GpLka6xVZIcHew4Nn-D2YXDHnsuXbRM/preview?usp=drivesdk',
            '12/01/2019',
        ),
        Poem(
            'The Last Breath',
            'https://drive.google.com/file/d/1-Z55FNk-01Bx47ji4ZS9n9BgUpZdGkyG/preview?usp=drivesdk',
            '18/01/2019',
        ),
        Poem(
            'The Thirst of Glimpse',
            'https://drive.google.com/file/d/1-XjULOOhLe_TInMnU3DgP6RPipd6luhl/preview?usp=drivesdk',
            '19/01/2019',
        ),
        Poem(
            'The Mighty Knights',
            'https://drive.google.com/file/d/1-V-QQCssK02uG1wVg6zOz5uL6FFdAVhn/preview?usp=drivesdk',
            '17/02/2019',
        ),
        Poem(
            'Will you still stay beside me?',
            'https://drive.google.com/file/d/1-044SR20kwWZ9Z2DHu8lDL_6Gbvr2rYW/preview?usp=drivesdk',
            '27/03/2019',
        ),
        Poem(
            'Tug Of War',
            'https://drive.google.com/file/d/1--W51nOg5-Bmv-ND046y5low8ZMUmlfI/preview?usp=drivesdk',
            '02/07/2019',
        ),
        Poem(
            'द्रौपदी की रक्षा',
            'https://drive.google.com/file/d/1-1kg3eFyj0j7M6U7PUbOOuJKHh6H_Nm4/preview?usp=drivesdk',
            '15/08/2019',
        ),
        Poem(
            'So Glad It Happened',
            'https://drive.google.com/file/d/1-jWrmkpGGScRhNvftyFIpqyzax02d7ux/preview?usp=drivesdk',
            '25/08/2019',
        ),
        Poem(
            'The Great Erosion',
            'https://drive.google.com/file/d/1-8NIHojMLIC0tT3AgSuZtC18qDd-n0FB/preview?usp=drivesdk',
            '07/09/2019',
        ),
        Poem(
            'The Ultimate Hunter',
            'https://drive.google.com/file/d/1-06WdtXkqvQx04FH9Zvrtr060t4l6uZj/preview?usp=drivesdk',
            '23/10/2019',
        ),
        Poem(
            'Far and Near',
            'https://drive.google.com/file/d/1-cGbRweEJeV3iNb_Nc0jLvUJ9ilmNneL/preview?usp=drivesdk',
            '17/11/2019',
        ),
        Poem(
            'Listen to Understand',
            'https://drive.google.com/file/d/1-kFJtWSxA39CT3TfQa0ZrmAJJcbgjZuf/preview?usp=drivesdk',
            '18/11/2019',
        ),
        Poem(
            'The Reins To Emotions',
            'https://drive.google.com/file/d/1-sCWIPN_xLvvuwN_IpGcBFPKybXxO4PM/preview?usp=drivesdk',
            '20/11/2019',
        ),
        Poem(
            'Long Way to Go Alone',
            'https://drive.google.com/file/d/1-wKwFPdmc8pmnkpX78aJszyFqEIrjgac/preview?usp=drivesdk',
            '25/11/2019',
        ),
        Poem(
            'Stuck in the Past',
            'https://drive.google.com/file/d/10-8i2Z1pLksVF_tI8pa-dbUlMbCdQpyT/preview?usp=drivesdk',
            '27/11/2019',
        ),
        Poem(
            'Not of My Kind',
            'https://drive.google.com/file/d/100LoxSyEJN3zYby0ePg-vyMb7T240b_o/preview?usp=drivesdk',
            '28/11/2019',
        ),
        Poem(
            'Being Low',
            'https://drive.google.com/file/d/100nI0IOrAXkSHgn9oJvlPuNw85Zu1rom/preview?usp=drivesdk',
            '29/11/2019',
        ),
        Poem(
            'And we call ourselves HUMANS?',
            'https://drive.google.com/file/d/105pb_AmBRy_NxefAiZh5zMCT6GWU4NAT/preview?usp=drivesdk',
            '30/11/2019',
        ),
        Poem(
            'My kingdom of darkness',
            'https://drive.google.com/file/d/112c5baNJbtqqXzrkYDpAjzKaQO3J1h8y/preview?usp=drivesdk',
            '15/12/2019',
        ),
        Poem(
            'Grinded',
            'https://drive.google.com/file/d/13K0O3E6NkaDtKdFR-lUltgk-E4czt0HV/preview?usp=drivesdk',
            '17/12/2019',
        ),
        Poem(
            'कुछ रंग ऐसे भी',
            'https://drive.google.com/file/d/13PYkQuE7HbQLSHkgIzzMiEIhN18RXEI1/preview?usp=drivesdk',
            '09/03/2020',
        ),
        Poem(
            'Life is?',
            'https://drive.google.com/file/d/100zQs_aEkCB5rBluBtjFOqxwSsL8ESRD/preview?usp=drivesdk',
            '01/03/2021'
        ),
        Poem(
            'Reality of illusions',
            'https://drive.google.com/file/d/1CgBj5kUOSh1TNbtPSUIW4IaPrt07HFde/preview?usp=drivesdk',
            '19/03/2021',
        )
    ]

    @staticmethod
    def get_short_poems():
        PoemData.short_poems.sort(key=lambda x: datetime.strptime(x, format='%d/%m/%Y'), reverse=True)
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
        Skill('Python', 'skills/py.png', 4),
        Skill('Flutter', 'skills/flutter.png', 4),
        Skill('Golang', 'skills/go.png', 3),
        Skill('Flask', 'skills/flask.png', 3),
        Skill('Android', 'skills/android.png', 3),
        Skill('Kotlin', 'skills/kt.png', 3),
        Skill('C-Language', 'skills/c.png', 3),
        Skill('C++', 'skills/cpp.png', 3),
        Skill('Java', 'skills/java.png', 3),
    ]
    certificates = [
        Certificate(
            issuer='Coursera',
            type=CertificateType.COURSE,
            date='08-04-2020',
            url='https://drive.google.com/file/d/1ZzQgM50shU-kqnIz3jAlqYOUJxQ0kZ6i/preview?usp=drivesdk',
            name='Python for Everybody',
        ),
        Certificate(
            issuer='Central Tool Room & Training Centre (CTTC)',
            type=CertificateType.INTERNSHIP,
            date='29-06-2019',
            name='Core Java',
            url='https://drive.google.com/file/d/1JbJVyiHy3jfMto7BqRWynfHYZJLVLvYu/preview?usp=drivesdk',
        ),
        Certificate(
            issuer='KIDE',
            type=CertificateType.OPEN_SOURCE,
            date='06-10-2020',
            name='HactoberFest 2020',
            url='https://drive.google.com/file/d/19ccEi8Y-3F65vccfJxDFzaTt5EV_pdem/preview?usp=drivesdk',
        ),
        Certificate(
            issuer='PriME Technology PVT Ltd.',
            type=CertificateType.INTERNSHIP,
            date='16-09-2020',
            name='Flutter App Internship - Karmik Suraksha',
            url='https://drive.google.com/file/d/12CWAsswL8Z9-TCsSnJy1RM8H7ze7jc8a/preview?usp=drivesdk',
        ),
        Certificate(
            issuer='PriME Technology PVT Ltd.',
            type=CertificateType.INTERNSHIP,
            date='02-01-2021',
            name='Flutter App Internship - Utkristh Gunnavatta',
            url='https://drive.google.com/file/d/1qzKDrxgjYXx6Cmj3lZyCjWNwvabEWdV9/preview?usp=drivesdk',
        ),
        Certificate(
            issuer='LIT & Spectrum',
            type=CertificateType.WORKSHOP,
            date='20-10-2019',
            name='Python Workshop',
            url='https://drive.google.com/file/d/1uhPKTIrDi3F-1N_eAQdq5UbKqB3BOJoH/preview?usp=drivesdk',
        ),
        Certificate(
            issuer='Nimble Tech & Spectrum',
            type=CertificateType.INTERNSHIP,
            date='31-05-2020',
            name='Android App Development',
            url='https://drive.google.com/file/d/1WASwDy078AvQYAUozwJV1nXBTVJ1ORJj/preview?usp=drivesdk',
        ),
        Certificate(
            issuer='Cisco Networking Academy',
            type=CertificateType.INTERNSHIP,
            date='23-04-2021',
            name='Cybersecurity Essentials',
            url='https://drive.google.com/file/d/1UTAA-l4Rcgj1RzIrqW-WH5AeHzZnZc8y/preview?usp=drivesdk',
        ),
        Certificate(
            issuer='Cisco Networking Academy',
            type=CertificateType.INTERNSHIP,
            date='23-04-2021',
            name='Introduction to Cybersecurity',
            url='https://drive.google.com/file/d/1XQxYHHQUgbPtY5mV6Ixc9XQZb72GNAUx/preview?usp=drivesdk',
        ),
        Certificate(
            issuer='Cisco Networking Academy',
            type=CertificateType.INTERNSHIP,
            date='30-03-2021',
            name='Introduction to Packet Tracer',
            url='https://drive.google.com/file/d/1UpTJ5_0f_cfXWO6Gft06qmqZkJciYX8Z/preview?usp=drivesdk',
        ),
        Certificate(
            issuer='OpenEDG Python Institute (Cisco)',
            type=CertificateType.INTERNSHIP,
            date='13-03-2021',
            name='Programming Essentials in Python (PCAP)',
            url='https://drive.google.com/file/d/1OOZq73deaJrMVNiNO4eRTPCu7D-UjVMO/preview?usp=drivesdk',
        ),
    ]
    experience = [
        Experience(
            name='Flutter Mobile App Intern',
            type=CertificateType.INTERNSHIP,
            months=2,
            place='PriME Technology PVT Ltd.',
            date=''
        )
    ]

    @staticmethod
    def get_certificates():
        Technical.certificates.sort(key=lambda x: datetime.strptime(x.date, '%d-%m-%Y'), reverse=True)
        return Technical.certificates


class Projects:
    projects = [
        Project(
            name='Utkristh Gunnavatta',
            date='02-01-2021',
            type=ProjectType.INTERNSHIP,
            url='https://play.google.com/store/apps/details?id=com.prime.qa_app',
            techUsed=['Flutter', 'Firebase', 'Dart'],
            desc='This project was aimed to design a safety monitoring and feedback.',
            domain='Mobile App',
            image_url='https://play-lh.googleusercontent.com/grAVOkieIxLWIeho-EQ7V7_qfO7lxnYKoYr5MWYbkk-aJG5uYVoV77GnpajVgd9X8c8=s180-rw'
        ),
        Project(
            name='Karmik Suraksha',
            date='16-09-2020',
            type=ProjectType.INTERNSHIP,
            url='https://play.google.com/store/apps/details?id=com.prime.feedback_app',
            techUsed=['Flutter', 'Firebase', 'Dart'],
            desc='This project was aimed to design a process-flow, review and feedback.',
            domain='Mobile App',
            image_url='https://play-lh.googleusercontent.com/aXI4e6dfNht3fCbwwBWSjfVBPmbwRpuVoQrRAvyZZMnslvOpnpgcpnWIfBEEXzF4a1o=s180-rw'
        ),
        Project(
            name='CET-B Mobile App',
            date='11-01-2021',
            type=ProjectType.INTERNSHIP,
            url='https://play.google.com/store/apps/details?id=com.coeaibbsr.cetb',
            techUsed=['Flutter', 'Firebase', 'Dart'],
            desc='This project was aimed to bring CET college and its resources at fingertips of the students. '
                 'It is currently being used by the students. '
                 'This app provides all information about courses, scholarships, map of college and room arrangements.',
            domain='Mobile App',
            image_url='https://play-lh.googleusercontent.com/WDOfe5xQjRtZpuCEEl03I9en7vk8vmlQQeZdnBe6zDwT7tXTYuZKXurdood3ecLh4Q=s180-rw'
        ),
        Project(
            name='FlaskBlog',
            url='https://rrka3flaskblog.herokuapp.com/',
            type=ProjectType.PRACTICE,
            date='19-05-2021',
            techUsed=['Python', 'Flask', 'SQLite'],
            domain='Web App',
            desc='This project aims at serving as a blog to a community. '
                 'Here users can register and login and send blogs. Users can edit and delete their blogs.'
        )
    ]

    @staticmethod
    def get_projects():
        Projects.projects.sort(key=lambda x: datetime.strptime(x.date, '%d-%m-%Y'), reverse=True)
        return Projects.projects
