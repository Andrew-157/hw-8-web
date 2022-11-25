from faker import Faker
from datetime import datetime
from random import randint


def groups_data():

    data = [('first',), ('second',), ('third',)]

    return data


def students_data():

    fake = Faker()
    data = []

    for id in range(1, 11):
        data.append((id, fake.name(), 'first'))

    for id in range(11, 21):
        data.append((id, fake.name(), 'second'))

    for id in range(21, 31):
        data.append((id, fake.name(), 'third'))

    return data


def subjects_data():

    fake = Faker()
    data = []
    subject_1 = "MATH"
    subject_2 = "PHYSICS"
    subject_3 = "BIOLOGY"
    subject_4 = "HISTORY"
    subject_5 = "CHEMISTRY"

    teacher_1 = fake.name()
    teacher_2 = fake.name()
    teacher_3 = fake.name()

    data.append((subject_1, teacher_1), (subject_2, teacher_2),
                (subject_3, teacher_3), (subject_4, teacher_2),
                (subject_5, teacher_1))


def marks_subject_1():

    data = []
    subject = "MATH"

    for id in range(1, 11):
        data.extend([
            (id, subject, randint(1, 5), datetime(
                2022, randint(1, 2), randint(1, 28)).date()),
            (id, subject, randint(1, 5), datetime(
                2022, randint(3, 4), randint(1, 30)).date()),
            (id, subject, randint(1, 5), datetime(
                2022, randint(5, 6), randint(1, 30)).date()),
            (id, subject, randint(1, 5), datetime(
                2022, randint(7, 8), randint(1, 30)).date()),
            (id, subject, randint(1, 5), datetime(
                2022, randint(9, 10), randint(1, 30)).date()),
            (id, subject, randint(1, 5), datetime(2022, 11, randint(1, 25)).date())])

    for id in range(11, 21):
        data.extend([
            (id, subject, randint(1, 5), datetime(
                2022, randint(1, 4), randint(1, 28)).date()),
            (id, subject, randint(1, 5), datetime(
                2022, randint(5, 7), randint(1, 30)).date()),
            (id, subject, randint(1, 5), datetime(
                2022, randint(8, 9), randint(1, 30)).date()),
            (id, subject, randint(1, 5), datetime(2022, randint(10, 11), randint(1, 25)).date())])

    for id in range(21, 31):
        data.extend([
            (id, subject, randint(1, 5), datetime(
                2022, randint(1, 5), randint(1, 28)).date()),
            (id, subject, randint(1, 5), datetime(
                2022, randint(6, 8), randint(1, 30)).date()),
            (id, subject, randint(1, 5), datetime(2022, randint(9, 11), randint(1, 30)).date())])

    return data
