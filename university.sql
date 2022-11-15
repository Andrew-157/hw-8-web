CREATE TABLE student
(
    id INT PRIMARY KEY,
    name VARCHAR(56),
);

CREATE TABLE subject
(
    name_of_sub VARCHAR(56),
    teacher_name VARCHAR(56),
    student_id INT,
    mark_1 INT,
    mark_1_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    mark_2 INT,
    mark_2_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    mark_3 INT,
    mark_3_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    mark_4 INT,
    mark_4_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students (id)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE student_group
(
    student_1 INT,
    student_2 INT,
    student_3 INT,
    student_4 INT,
    student_5 INT,
    student_6 INT,
    student_7 INT,
    student_8 INT,
    student_9 INT,
    student_10 INT,
    FOREIGN KEY (student_1) REFERENCES students (id)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (student_2) REFERENCES students (id)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (student_3) REFERENCES students (id)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (student_4) REFERENCES students (id)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (student_5) REFERENCES students (id)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (student_6) REFERENCES students (id)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (student_7) REFERENCES students (id)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (student_8) REFERENCES students (id)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (student_9) REFERENCES students (id)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (student_10) REFERENCES students (id)
		ON UPDATE CASCADE
        ON DELETE CASCADE
);