LOAD DATA LOCAL INFILE 'REPLACE_ME_CSV_FULL_PATH'
INTO TABLE REPLACE_ME_DB_NAME.REPLACE_ME_TABLE_NAME
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    @person_name, @person_age, @email_addr, @phone_num, @birth_date, @yearly_salary
)
SET
    `person_name` = NULLIF(@person_name, ''),
    `person_age` = NULLIF(@person_age, ''),
    `email_addr` = NULLIF(@email_addr, ''),
    `phone_num` = NULLIF(@phone_num, ''),
    `birth_date` = NULLIF(@birth_date, ''),
    `yearly_salary` = NULLIF(@yearly_salary, '')
;