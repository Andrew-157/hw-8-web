import sqlite3


def run_query(sql):

    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql_1 = """SELECT students.name, ROUND(AVG(mark), 0) as max_aver
FROM marks
    LEFT JOIN students ON marks.stud_id=students.id
GROUP BY stud_id
HAVING ROUND(AVG(mark), 0)=
(SELECT ROUND(MAX(aver), 0)
FROM
    (SELECT ROUND(AVG(mark), 0) as aver
    FROM marks
    GROUP BY stud_id))
LIMIT 5;"""

sql_2 = """SELECT students.name, ROUND(AVG(mark), 0) as max_aver
FROM marks
    LEFT JOIN students ON marks.stud_id=students.id
WHERE subject_name="HISTORY"
GROUP BY stud_id
HAVING ROUND(AVG(mark), 0)=
(SELECT ROUND(MAX(aver), 0)
FROM
    (SELECT ROUND(AVG(mark), 0) as aver
    FROM marks
    GROUP BY stud_id))
LIMIT 1;"""

sql_3 = """SELECT groups.name, marks.subject_name, AVG(mark) as aver
FROM marks
    INNER JOIN students ON students.id = marks.stud_id
    INNER JOIN groups ON students.group_name = groups.name
WHERE marks.subject_name = "MATH"
GROUP BY  groups.name
;"""

sql_4 = """SELECT groups.name , AVG(mark) as aver
FROM marks
    INNER JOIN students ON students.id = marks.stud_id
    INNER JOIN groups ON students.group_name = groups.name
GROUP BY  groups.name
;"""

sql_5 = """SELECT teacher, name as subject
FROM subjects;"""

sql_6 = """SELECT students.group_name as students_group, students.name as student
from students;"""

sql_7 = """SELECT students.group_name as group_, students.name as student, marks.subject_name as subject, marks.mark as mark
from marks
    INNER JOIN students ON students.id=marks.stud_id
where marks.subject_name="HISTORY";"""

sql_8 = """SELECT students.group_name as group_, students.name as student, marks.subject_name as subject, marks.mark as mark, date_of_mark as date_
from marks
    INNER JOIN students ON students.id=marks.stud_id
WHERE NOT date_of_mark < '2022-11-15' AND marks.subject_name ='HISTORY';"""

sql_9 = """SELECT students.name , marks.subject_name
FROM marks
    INNER JOIN students ON marks.stud_id=students.id
WHERE students.id=2
GROUP BY  subject_name, students.name
;"""

sql_10 = """SELECT subjects.teacher as teacher, marks.subject_name, students.name as student
FROM marks
    INNER JOIN students ON marks.stud_id=students.id
    INNER JOIN subjects ON marks.subject_name = subjects.name
GROUP BY students.name, subject_name;"""

sql_11 = """SELECT subjects.teacher, subjects.name as subject, AVG(mark) as average, students.name as student
FROM subjects
    INNER JOIN marks ON subjects.name=marks.subject_name
    INNER JOIN students ON students.id=marks.stud_id
group by students.name, marks.subject_name
;"""

sql_12 = """SELECT subjects.teacher, AVG(mark) as average
FROM subjects
    INNER JOIN marks ON subjects.name=marks.subject_name
group by subjects.teacher;"""

if __name__ == '__main__':
    print(run_query(sql_1))
    print(run_query(sql_2))
    print(run_query(sql_3))
    print(run_query(sql_4))
    print(run_query(sql_5))
    print(run_query(sql_6))
    print(run_query(sql_7))
    print(run_query(sql_8))
    print(run_query(sql_9))
    print(run_query(sql_10))
    print(run_query(sql_11))
    print(run_query(sql_12))
