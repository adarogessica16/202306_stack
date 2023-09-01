-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_datos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_datos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_datos` DEFAULT CHARACTER SET utf8 ;
USE `esquema_datos` ;

-- -----------------------------------------------------
-- Table `esquema_datos`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_datos`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(225) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
