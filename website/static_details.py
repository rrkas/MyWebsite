from flask import url_for

from website.models import *


class PersonalDetails:
    name = 'Rohnak Agarwal'
    dob = 'July 9, 2000'
    residence = 'Cuttack, Odisha, India'
    mail_id = 'rrka79wal@gmail.com'
    github = 'https://github.com/rrkas'
    linkedin = 'https://www.linkedin.com/in/rohnak-agarwal-5558391a0/'
    qwiklabs = 'https://google.qwiklabs.com/public_profiles/4b318807-5a88-4858-8fd1-3230f22b21d3'
    hobbies = ['Poems', 'Coding']
    sports = 'Badminton'
    education = [
        Education('B.Tech. (CSE)', 'College of Engineering and Technology (CET)', 'Ghatikia, Bhubaneswar', 2022, str(round(9.44 * 9.5, 2))),
        Education('Class 12', 'D.A.V. Public School', 'CDA-6, Cuttack', 2018, '92.40'),
        Education('Class 10', 'D.A.V. Public School', 'CDA-6, Cuttack', 2016, '95.00'),
    ]


class PoemData:
    collections = [
        Poem(
            'The Verse Of facts',
            'https://drive.google.com/file/d/13Jc98bZu_soi23WsFm7V6y7qRQiMVejb/view?usp=sharing',
            '14/05/2019',
        )
    ]
    short_poems = [
        Poem(
            'The Sea Shore',
            'https://drive.google.com/file/d/1-9zF5XN16AAQnLB7osR24TELVlPImg4B/view?usp=sharing',
            '11/01/2019',
        ),
        Poem(
            'The Small Playground',
            'https://drive.google.com/file/d/1-GpLka6xVZIcHew4Nn-D2YXDHnsuXbRM/view?usp=sharing',
            '12/01/2019',
        ),
        Poem(
            'The Last Breath',
            'https://drive.google.com/file/d/1-Z55FNk-01Bx47ji4ZS9n9BgUpZdGkyG/view?usp=sharing',
            '18/01/2019',
        ),
        Poem(
            'The Thirst of Glimpse',
            'https://drive.google.com/file/d/1-XjULOOhLe_TInMnU3DgP6RPipd6luhl/view?usp=sharing',
            '19/01/2019',
        ),
        Poem(
            'The Mighty Knights',
            'https://drive.google.com/file/d/1-V-QQCssK02uG1wVg6zOz5uL6FFdAVhn/view?usp=sharing',
            '17/02/2019',
        ),
        Poem(
            'Will you still stay beside me?',
            'https://drive.google.com/file/d/1-044SR20kwWZ9Z2DHu8lDL_6Gbvr2rYW/view?usp=sharing',
            '27/03/2019',
        ),
        Poem(
            'Tug Of War',
            'https://drive.google.com/file/d/1--W51nOg5-Bmv-ND046y5low8ZMUmlfI/view?usp=sharing',
            '02/07/2019',
        ),
        Poem(
            'द्रौपदी की रक्षा',
            'https://drive.google.com/file/d/1-1kg3eFyj0j7M6U7PUbOOuJKHh6H_Nm4/view?usp=sharing',
            '15/08/2019',
        ),
        Poem(
            'So Glad It Happened',
            'https://drive.google.com/file/d/1-jWrmkpGGScRhNvftyFIpqyzax02d7ux/view?usp=sharing',
            '25/08/2019',
        ),
        Poem(
            'The Great Erosion',
            'https://drive.google.com/file/d/1-8NIHojMLIC0tT3AgSuZtC18qDd-n0FB/view?usp=sharing',
            '07/09/2019',
        ),
        Poem(
            'The Ultimate Hunter',
            'https://drive.google.com/file/d/1-06WdtXkqvQx04FH9Zvrtr060t4l6uZj/view?usp=sharing',
            '23/10/2019',
        ),
        Poem(
            'Far and Near',
            'https://drive.google.com/file/d/1-cGbRweEJeV3iNb_Nc0jLvUJ9ilmNneL/view?usp=sharing',
            '17/11/2019',
        ),
        Poem(
            'Listen to Understand',
            'https://drive.google.com/file/d/1-kFJtWSxA39CT3TfQa0ZrmAJJcbgjZuf/view?usp=sharing',
            '18/11/2019',
        ),
        Poem(
            'The Reins To Emotions',
            'https://drive.google.com/file/d/1-sCWIPN_xLvvuwN_IpGcBFPKybXxO4PM/view?usp=sharing',
            '20/11/2019',
        ),
        Poem(
            'Long Way to Go Alone',
            'https://drive.google.com/file/d/1-wKwFPdmc8pmnkpX78aJszyFqEIrjgac/view?usp=sharing',
            '25/11/2019',
        ),
        Poem(
            'Stuck in the Past',
            'https://drive.google.com/file/d/10-8i2Z1pLksVF_tI8pa-dbUlMbCdQpyT/view?usp=sharing',
            '27/11/2019',
        ),
        Poem(
            'Not of My Kind',
            'https://drive.google.com/file/d/100LoxSyEJN3zYby0ePg-vyMb7T240b_o/view?usp=sharing',
            '28/11/2019',
        ),
        Poem(
            'Being Low',
            'https://drive.google.com/file/d/100nI0IOrAXkSHgn9oJvlPuNw85Zu1rom/view?usp=sharing',
            '29/11/2019',
        ),
        Poem(
            'And we call ourselves HUMANS?',
            'https://drive.google.com/file/d/105pb_AmBRy_NxefAiZh5zMCT6GWU4NAT/view?usp=sharing',
            '30/11/2019',
        ),
        Poem(
            'My kingdom of darkness',
            'https://drive.google.com/file/d/112c5baNJbtqqXzrkYDpAjzKaQO3J1h8y/view?usp=sharing',
            '15/12/2019',
        ),
        Poem(
            'Grinded',
            'https://drive.google.com/file/d/13K0O3E6NkaDtKdFR-lUltgk-E4czt0HV/view?usp=sharing',
            '17/12/2019',
        ),
        Poem(
            'कुछ रंग ऐसे भी',
            'https://drive.google.com/file/d/13PYkQuE7HbQLSHkgIzzMiEIhN18RXEI1/view?usp=sharing',
            '09/03/2020',
        ),
        Poem(
            'Life is?',
            'https://drive.google.com/file/d/100zQs_aEkCB5rBluBtjFOqxwSsL8ESRD/view?usp=sharing',
            '01/03/2021'
        ),
        Poem(
            'Reality of illusions',
            'https://drive.google.com/file/d/1CgBj5kUOSh1TNbtPSUIW4IaPrt07HFde/view?usp=sharing',
            '19/03/2021',
        )
    ]


class Technical:
    skills = [
        Skill('Python', 'skills/py.png', 4),
        Skill('Flutter', 'skills/flutter.png', 4),
        Skill('Golang', 'skills/go.png', 3),
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
            filepathstatic='certificates/Coursera python for everybody.pdf',
            name='Python for Everybody',
        ),
        Certificate(
            issuer='Central Tool Room & Training Centre (CTTC)',
            type=CertificateType.INTERNSHIP,
            date='29-06-2019',
            name='Core Java',
            filepathstatic='certificates/CTTC Core JAVA internship Certificate.jpg',
        ),
        Certificate(
            issuer='KIDE',
            type=CertificateType.OPEN_SOURCE,
            date='06-10-2020',
            name='HactoberFest 2020',
            filepathstatic='certificates/Hactoberfest2020 kide.png',
        ),
        Certificate(
            issuer='PriME Technology PVT Ltd.',
            type=CertificateType.INTERNSHIP,
            date='16-09-2020',
            name='Flutter App Internship - Karmik Suraksha',
            filepathstatic='certificates/PriME Technologies pvt ltd - Karmik Suraksha.pdf',
        ),
        Certificate(
            issuer='PriME Technology PVT Ltd.',
            type=CertificateType.INTERNSHIP,
            date='02-01-2021',
            name='Flutter App Internship - Utkristh Gunnavatta',
            filepathstatic='certificates/PriME TEchnologies pvt ltd - Utkristh Gunnavatta.pdf',
        ),
        Certificate(
            issuer='LIT & Spectrum',
            type=CertificateType.WORKSHOP,
            date='20-10-2019',
            name='Python Workshop',
            filepathstatic='certificates/Python workshop by LIT bbsr.jpg',
        ),
        Certificate(
            issuer='Nimble Tech & Spectrum',
            type=CertificateType.INTERNSHIP,
            date='31-05-2020',
            name='Android App Development',
            filepathstatic='certificates/Rohnak Agarwal internship Certificate spectrum.pdf',
        ),
        Certificate(
            issuer='Cisco Networking Academy',
            type=CertificateType.INTERNSHIP,
            date='23-04-2021',
            name='Cybersecurity Essentials',
            filepathstatic='certificates/RohnakAgarwal-Cybersecurity Esesentials.pdf',
        ),
        Certificate(
            issuer='Cisco Networking Academy',
            type=CertificateType.INTERNSHIP,
            date='23-04-2021',
            name='Introduction to Cybersecurity',
            filepathstatic='certificates/RohnakAgarwal-Introduction to cybersecurity.pdf',
        ),
        Certificate(
            issuer='Cisco Networking Academy',
            type=CertificateType.INTERNSHIP,
            date='30-03-2021',
            name='Introduction to Packet Tracer',
            filepathstatic='certificates/RohnakAgarwal-Introduction to packet tracer-certificate.pdf',
        ),
        Certificate(
            issuer='OpenEDG Python Institute (Cisco)',
            type=CertificateType.INTERNSHIP,
            date='13-03-2021',
            name='Programming Essentials in Python (PCAP)',
            filepathstatic='certificates/RohnakAgarwal-PCAP-certificate.pdf',
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

class Projects:
    pass
