CREATE DATABASE IF NOT EXISTS `evolve_scrm`;
USE `evolve_scrm`;

CREATE TABLE IF NOT EXISTS `users` (
  `id` VARCHAR(10) PRIMARY KEY,
  `name` VARCHAR(50) NOT NULL,
  `surname` VARCHAR(255) NOT NULL,
  `email` VARCHAR(100) NOT NULL UNIQUE,
  `phone` VARCHAR(20) DEFAULT NULL,
  `address` VARCHAR(255) DEFAULT NULL,
  `registration_date` DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `bill_status` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `status` VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS `bills` (
  `id` VARCHAR(10) PRIMARY KEY,
  `user_id` VARCHAR(10) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `status_id` INT NOT NULL,
  `monto` DECIMAL(10, 2) NOT NULL,
  `bill_date` DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`status_id`) REFERENCES `bill_status`(`id`) ON DELETE CASCADE
);

DELIMITER $$
CREATE TRIGGER `before_insert_users` BEFORE INSERT ON `users` FOR EACH ROW BEGIN
    DECLARE next_num INT;
    SELECT IFNULL(MAX(CAST(SUBSTRING(id, 4) AS UNSIGNED)), 0) + 1 INTO next_num FROM users;
    SET NEW.id = CONCAT('USR', LPAD(next_num, 3, '0'));
END
$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER `before_insert_bills` BEFORE INSERT ON `bills` FOR EACH ROW BEGIN
    DECLARE next_num INT;
    DECLARE year_part CHAR(2);
    DECLARE month_part CHAR(2);
    SET year_part = DATE_FORMAT(NEW.bill_date, '%Y');
    SET month_part = DATE_FORMAT(NEW.bill_date, '%m');
    SELECT IFNULL(MAX(CAST(SUBSTRING(id, 8, 3) AS UNSIGNED)), 0) + 1
    INTO next_num
    FROM bills
    WHERE SUBSTRING(id, 4, 2) = year_part AND SUBSTRING(id, 6, 2) = month_part;
    SET NEW.id = CONCAT('FAC', year_part, month_part, LPAD(next_num, 3, '0'));
END
$$
DELIMITER ;