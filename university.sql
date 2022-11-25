CREATE TABLE groups
(
    name VARCHAR(56) PRIMARY KEY
);

CREATE TABLE students
(
    id INT PRIMARY KEY,
    name VARCHAR(56),
    group_name VARCHAR(56),
    FOREIGN KEY (group_name) REFERENCES groups(name)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE subjects
(
    name VARCHAR(56) PRIMARY KEY,
    teacher VARCHAR(56)
);

CREATE TABLE marks
(
    stud_id INT,
    subject_name VARCHAR(56),
    mark TINYINT,
    date_of_mark DATE NOT NULL,
    FOREIGN KEY (stud_id) REFERENCES students(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (subject_name) REFERENCES subjects(name)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);