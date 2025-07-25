CREATE DATABASE IF NOT EXISTS REPLACE_ME_DB_NAME;

DROP TABLE IF EXISTS REPLACE_ME_DB_NAME.REPLACE_ME_TABLE_NAME;

CREATE TABLE REPLACE_ME_DB_NAME.REPLACE_ME_TABLE_NAME (
    `employee_full_name` VARCHAR(12),
    `employee_age` VARCHAR(3),
    `contact_email` VARCHAR(22),
    `contact_phone` VARCHAR(9),
    `birth_date` VARCHAR(11),
    `annual_salary` VARCHAR(6),
    INDEX idx_employee_name (`employee_full_name`),
    INDEX idx_contact_email (`contact_email`)
);
