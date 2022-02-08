CREATE TABLE `personinfodb`.`persondata` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(65) NOT NULL,
  `age` INT NOT NULL,
  `salary` DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  PRIMARY KEY (`id`));