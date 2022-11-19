import sqlite3
from time import sleep

sql_1 = """SELECT student.name, ((subj_1_m_1 + subj_1_m_2 + subj_1_m_3 + subj_1_m_4)+
(subj_2_m_1 + subj_2_m_2 + subj_2_m_3 + subj_2_m_4)+
(subj_3_m_1 + subj_3_m_2 + subj_3_m_3 + subj_3_m_4)+
(subj_4_m_1 + subj_4_m_2 + subj_4_m_3 + subj_4_m_4)+
(subj_5_m_1 + subj_5_m_2 + subj_5_m_3 + subj_5_m_4))/20 as max_average_mark
FROm subjects
    LEFT JOIN student ON stud_id = student.id
WHERE (((subj_1_m_1 + subj_1_m_2 + subj_1_m_3 + subj_1_m_4)+
(subj_2_m_1 + subj_2_m_2 + subj_2_m_3 + subj_2_m_4)+
(subj_3_m_1 + subj_3_m_2 + subj_3_m_3 + subj_3_m_4)+
(subj_4_m_1 + subj_4_m_2 + subj_4_m_3 + subj_4_m_4)+
(subj_5_m_1 + subj_5_m_2 + subj_5_m_3 + subj_5_m_4))/20)=(SELECT max(((subj_1_m_1 + subj_1_m_2 + subj_1_m_3 + subj_1_m_4)+
(subj_2_m_1 + subj_2_m_2 + subj_2_m_3 + subj_2_m_4)+
(subj_3_m_1 + subj_3_m_2 + subj_3_m_3 + subj_3_m_4)+
(subj_4_m_1 + subj_4_m_2 + subj_4_m_3 + subj_4_m_4)+
(subj_5_m_1 + subj_5_m_2 + subj_5_m_3 + subj_5_m_4))/20)
FROM subjects)
LIMIT 5;"""

sql_2 = """SELECT subj_1, student.name, MAX((subj_1_m_1 + subj_1_m_2 + subj_1_m_3 + subj_1_m_4)/4) as max_aver_subj
FROM subjects
    LEFT JOIN student ON student.id = stud_id;"""

sql_3 = """SELECT stud_group.name as group_, AVG((subj_1_m_1+subj_1_m_2+subj_1_m_3+subj_1_m_4)/4) as aver
FROM subjects
    INNER JOIN student ON student.id = subjects.stud_id
    INNER JOIN stud_group ON student.group_name = stud_group.name
GROUP by stud_group.name;"""

sql_4 = """SELECT stud_group.name as group_, AVG(((subj_1_m_1 + subj_1_m_2 + subj_1_m_3 + subj_1_m_4)+
(subj_2_m_1 + subj_2_m_2 + subj_2_m_3 + subj_2_m_4)+
(subj_3_m_1 + subj_3_m_2 + subj_3_m_3 + subj_3_m_4)+
(subj_4_m_1 + subj_4_m_2 + subj_4_m_3 + subj_4_m_4)+
(subj_5_m_1 + subj_5_m_2 + subj_5_m_3 + subj_5_m_4))/20) as aver_group
FROM subjects
    INNER JOIN student ON subjects.stud_id = student.id
    INNER JOIN stud_group ON stud_group.name = student.group_name
group by stud_group.name;"""

sql_5 = """SELECT subjects.subj_1_teacher, subjects.subj_1, subjects.subj_2_teacher, subjects.subj_2,
    subjects.subj_3_teacher, subjects.subj_3, subjects.subj_4_teacher, subjects.subj_4,
    subjects.subj_5_teacher, subjects.subj_5
FROM subjects
LIMIT 1;"""

sql_6 = """SELECT student.name as student, stud_group.name as group_
FROM student
    INNER JOIN stud_group ON stud_group.name=student.group_name
;"""

sql_7 = """SELECT stud_group.name as group_, student.name, subj_1, subj_1_m_1, subj_1_m_2, subj_1_m_3, subj_1_m_4,
    subj_2, subj_2_m_1, subj_2_m_2, subj_2_m_3, subj_2_m_4,
    subj_3, subj_3_m_1, subj_3_m_2, subj_3_m_3, subj_3_m_4,
    subj_4, subj_4_m_1, subj_4_m_2, subj_4_m_3, subj_4_m_4,
    subj_5, subj_5_m_1, subj_5_m_2, subj_5_m_3, subj_5_m_4
FROM subjects
    INNER JOIN student ON student.id=subjects.stud_id
    INNER JOIn stud_group ON student.group_name = stud_group.name;"""

sql_8 = """SELECT stud_group.name, student.name, subj_4, subj_4_m_4, subj_4_m_4_date
FROm subjects
    INNER JOIn student ON student.id = subjects.stud_id
    INNER JOIN stud_group ON student.group_name = stud_group.name;"""

sql_9 = """SELECT student.name, subj_1, subj_2, subj_3, subj_4, subj_5
FROM student
RIGHT JOIN subjects ON student.id=subjects.stud_id;"""

sql_10 = """SELECT student.name, subj_1_teacher, subj_1, subj_2_teacher, subj_2, subj_3_teacher, subj_3, subj_4_teacher, subj_4, subj_5_teacher, subj_5
FROM student
    INNER JOIN subjects ON student.id=subjects.stud_id;"""

sql_11 = """SELECT student.name, subj_1_teacher, (subj_1_m_1+subj_1_m_2+subj_1_m_3+subj_1_m_4)/4 as aver_1,
    subj_2_teacher, (subj_2_m_1+subj_2_m_2+subj_2_m_3+subj_2_m_4)/4 as aver_2,
    subj_3_teacher, (subj_3_m_1+subj_3_m_2+subj_3_m_3+subj_3_m_4)/4 as aver_3,
    subj_4_teacher, (subj_4_m_1+subj_4_m_2+subj_4_m_3+subj_4_m_4)/4 as aver_4,
    subj_5_teacher, (subj_5_m_1+subj_5_m_2+subj_5_m_3+subj_5_m_4)/4 as aver_5
FROM student
    INNER JOIN subjects ON student.id = subjects.stud_id;"""

sql_12 = """SELECT subj_1_teacher, AVG((subj_1_m_1+subj_1_m_2+subj_1_m_3+subj_1_m_4)/4) as aver_teacher_1,
    subj_2_teacher, AVG((subj_2_m_1+subj_2_m_2+subj_2_m_3+subj_2_m_4)/4) as aver_teacher_2,
    subj_3_teacher, AVG((subj_3_m_1+subj_3_m_2+subj_3_m_3+subj_3_m_4)/4) as aver_teacher_3,
    subj_4_teacher, AVG((subj_4_m_1+subj_4_m_2+subj_4_m_3+subj_4_m_4)/4) as aver_teacher_4,
    subj_5_teacher, AVG((subj_5_m_1+subj_5_m_2+subj_5_m_3+subj_5_m_4)/4) as aver_teacher_5
FROM subjects;"""


def run_query(sql):
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


if __name__ == '__main__':
    print("1 QUERY START...")
    print(run_query(sql_1))
    print("1 QUERY END...")
    sleep(1)
    print("2 QUERY START...")
    print(run_query(sql_2))
    print("2 QUERY END...")
    sleep(1)
    print("3 QUERY START...")
    print(run_query(sql_3))
    print("3 QUERY END...")
    sleep(1)
    print("4 QUERY START...")
    print(run_query(sql_4))
    print("4 QUERY END...")
    sleep(1)
    print("5 QUERY START...")
    print(run_query(sql_5))
    print("5 QUERY END...")
    sleep(1)
    print("SECOND QUERY START...")
    print(run_query(sql_6))
    print("6 QUERY END...")
    sleep(1)
    print("7 QUERY START...")
    print(run_query(sql_7))
    print("7 QUERY END...")
    sleep(1)
    print("8 QUERY START...")
    print(run_query(sql_8))
    print("8 QUERY END...")
    sleep(1)
    print("9 QUERY START...")
    print(run_query(sql_10))
    print("10 QUERY END...")
    sleep(1)
    print("11 QUERY START...")
    print(run_query(sql_11))
    print("11 QUERY END...")
    sleep(1)
    print("12 QUERY START...")
    print(run_query(sql_12))
    print("12 QUERY END...")
