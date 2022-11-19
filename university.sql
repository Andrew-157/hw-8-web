CREATE TABLE stud_group
(
    name VARCHAR(56) PRIMARY KEY
);

CREATE TABLE student
(
    id INT PRIMARY KEY,
    name VARCHAR(56),
    group_name VARCHAR(56),
    FOREIGN KEY(group_name) REFERENCES stud_group(name)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE subjects
(
    stud_id INT,
    subj_1 VARCHAR(56),
    subj_1_teacher VARCHAR(56),
    subj_1_m_1 TINYINT,
    subj_1_m_1_date DATE NOT NULL,
    subj_1_m_2 TINYINT,
    subj_1_m_2_date DATE NOT NULL,
    subj_1_m_3 TINYINT,
    subj_1_m_3_date DATE NOT NULL,
    subj_1_m_4 TINYINT,
    subj_1_m_4_date DATE NOT NULL,
    subj_2 VARCHAR(56),
    subj_2_teacher VARCHAR(56),
    subj_2_m_1 TINYINT,
    subj_2_m_1_date DATE NOT NULL,
    subj_2_m_2 TINYINT,
    subj_2_m_2_date DATE NOT NULL,
    subj_2_m_3 TINYINT,
    subj_2_m_3_date DATE NOT NULL,
    subj_2_m_4 TINYINT,
    subj_2_m_4_date DATE NOT NULL,
    subj_3 VARCHAR(56),
    subj_3_teacher VARCHAR(56),
    subj_3_m_1 TINYINT,
    subj_3_m_1_date DATE NOT NULL,
    subj_3_m_2 TINYINT,
    subj_3_m_2_date DATE NOT NULL,
    subj_3_m_3 TINYINT,
    subj_3_m_3_date DATE NOT NULL,
    subj_3_m_4 TINYINT,
    subj_3_m_4_date DATE NOT NULL,
    subj_4 VARCHAR(56),
    subj_4_teacher VARCHAR(56),
    subj_4_m_1 TINYINT,
    subj_4_m_1_date DATE NOT NULL,
    subj_4_m_2 TINYINT,
    subj_4_m_2_date DATE NOT NULL,
    subj_4_m_3 TINYINT,
    subj_4_m_3_date DATE NOT NULL,
    subj_4_m_4 TINYINT,
    subj_4_m_4_date DATE NOT NULL,
    subj_5 VARCHAR(56),
    subj_5_teacher VARCHAR(56),
    subj_5_m_1 TINYINT,
    subj_5_m_1_date DATE NOT NULL,
    subj_5_m_2 TINYINT,
    subj_5_m_2_date DATE NOT NULL,
    subj_5_m_3 TINYINT,
    subj_5_m_3_date DATE NOT NULL,
    subj_5_m_4 TINYINT,
    subj_5_m_4_date DATE NOT NULL,
    FOREIGN KEY (stud_id) REFERENCES student(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);