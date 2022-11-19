import sqlite3
import faker
from random import randint
from datetime import datetime


def generate_data_to_group():
    data = [('first',), ('second',), ('third',)]

    return data


def generate_data_to_student():
    data = []
    fake = faker.Faker()

    for index in range(1, 11):
        data.append((index, fake.name(), 'first'))

    for index in range(11, 21):
        data.append((index, fake.name(), 'second'))

    for index in range(21, 31):
        data.append((index, fake.name(), 'third'))

    return data


def generate_data_to_subjects():
    data = []
    subject_1 = "MATH"
    subject_2 = "PHYSICS"
    subject_3 = "HISTORY"
    subject_4 = "ECONOMICS"
    subject_5 = "MUSIC"

    teacher_1 = faker.Faker().name()
    teacher_2 = faker.Faker().name()
    teacher_3 = faker.Faker().name()

    date_1 = datetime(2022, randint(9, 10), randint(1, 30)).date()
    date_2 = datetime(2022, randint(11, 12), randint(1, 20)).date()
    date_3 = datetime(2023, randint(1, 4), randint(1, 28)).date()
    date_4 = datetime(2023, randint(4, 6), randint(1, 20)).date()

    date_5 = datetime(2022, randint(9, 10), randint(1, 30)).date()
    date_6 = datetime(2022, randint(11, 12), randint(1, 20)).date()
    date_7 = datetime(2023, randint(1, 4), randint(1, 28)).date()
    date_8 = datetime(2023, randint(4, 6), randint(1, 20)).date()

    date_9 = datetime(2022, randint(9, 10), randint(1, 30)).date()
    date_10 = datetime(2022, randint(11, 12), randint(1, 20)).date()
    date_11 = datetime(2023, randint(1, 4), randint(1, 28)).date()
    date_12 = datetime(2023, randint(4, 6), randint(1, 20)).date()

    date_13 = datetime(2022, randint(9, 10), randint(1, 30)).date()
    date_14 = datetime(2022, randint(11, 12), randint(1, 20)).date()
    date_15 = datetime(2023, randint(1, 4), randint(1, 28)).date()
    date_16 = datetime(2023, randint(4, 6), randint(1, 20)).date()

    date_17 = datetime(2022, randint(9, 10), randint(1, 30)).date()
    date_18 = datetime(2022, randint(11, 12), randint(1, 20)).date()
    date_19 = datetime(2023, randint(1, 4), randint(1, 28)).date()
    date_20 = datetime(2023, randint(4, 6), randint(1, 20)).date()

    for id in range(1, 31):
        data.append((
            id,
            subject_1,
            teacher_1,
            randint(1, 5),
            date_1,
            randint(1, 5),
            date_2,
            randint(1, 5),
            date_3,
            randint(1, 5),
            date_4,
            subject_2,
            teacher_2,
            randint(1, 5),
            date_5,
            randint(1, 5),
            date_6,
            randint(1, 5),
            date_7,
            randint(1, 5),
            date_8,
            subject_3,
            teacher_3,
            randint(1, 5),
            date_9,
            randint(1, 5),
            date_10,
            randint(1, 5),
            date_11,
            randint(1, 5),
            date_12,
            subject_4,
            teacher_1,
            randint(1, 5),
            date_13,
            randint(1, 5),
            date_14,
            randint(1, 5),
            date_15,
            randint(1, 5),
            date_16,
            subject_5,
            teacher_3,
            randint(1, 5),
            date_17,
            randint(1, 5),
            date_18,
            randint(1, 5),
            date_19,
            randint(1, 5),
            date_20,)
        )

    return data


def insert_data(group_data, student_data, subjects_data):

    with sqlite3.connect('university.db') as con:
        cur = con.cursor()

        sql_1 = """INSERT INTO stud_group(name) VALUES (?)"""
        sql_2 = """INSERT INTO student(id, name, group_name)
        VALUES (?, ?, ?)"""
        sql_3 = """INSERT INTO subjects(
            stud_id,
            subj_1,
            subj_1_teacher,
            subj_1_m_1,
            subj_1_m_1_date,
            subj_1_m_2,
            subj_1_m_2_date,
            subj_1_m_3,
            subj_1_m_3_date,
            subj_1_m_4,
            subj_1_m_4_date,
            subj_2,
            subj_2_teacher,
            subj_2_m_1,
            subj_2_m_1_date,
            subj_2_m_2,
            subj_2_m_2_date,
            subj_2_m_3,
            subj_2_m_3_date,
            subj_2_m_4,
            subj_2_m_4_date,
            subj_3,
            subj_3_teacher,
            subj_3_m_1,
            subj_3_m_1_date,
            subj_3_m_2,
            subj_3_m_2_date,
            subj_3_m_3,
            subj_3_m_3_date,
            subj_3_m_4,
            subj_3_m_4_date,
            subj_4,
            subj_4_teacher,
            subj_4_m_1,
            subj_4_m_1_date,
            subj_4_m_2,
            subj_4_m_2_date,
            subj_4_m_3,
            subj_4_m_3_date,
            subj_4_m_4,
            subj_4_m_4_date,
            subj_5,
            subj_5_teacher,
            subj_5_m_1,
            subj_5_m_1_date,
            subj_5_m_2,
            subj_5_m_2_date,
            subj_5_m_3,
            subj_5_m_3_date,
            subj_5_m_4,
            subj_5_m_4_date) VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?)"""

        cur.executemany(sql_1, group_data)
        cur.executemany(sql_2, student_data)
        cur.executemany(sql_3, subjects_data)

        con.commit()


if __name__ == '__main__':
    group_data = generate_data_to_group()
    student_data = generate_data_to_student()
    subjects_data = generate_data_to_subjects()
    insert_data(group_data, student_data, subjects_data)
