SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `Brew_App` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Brew_App`;

DROP TABLE IF EXISTS `Drinks`;
CREATE TABLE `Drinks` (
  `DrinkID` int NOT NULL AUTO_INCREMENT,
  `DrinkName` varchar(100) DEFAULT NULL,
  `Alcoholic` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`DrinkID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Drinks` (`DrinkID`, `DrinkName`, `Alcoholic`) VALUES
(1,	'Mai Tai',	1),
(2,	'Mojito',	1),
(3,	'Stella Artois',	1),
(4,	'Mahou',	1),
(5,	'Pina Colada',	1),
(6,	'Irn Bru',	0),
(7,	'Dr. Pepper',	0),
(8,	'Coca Cola',	0),
(9,	'Tango',	0);

DROP TABLE IF EXISTS `Person`;
CREATE TABLE `Person` (
  `PersonID` int NOT NULL AUTO_INCREMENT,
  `Person_First_Name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Person_Surname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Person_Age` int DEFAULT NULL,
  `Favourite_Drink` int DEFAULT NULL,
  PRIMARY KEY (`PersonID`),
  KEY `Favourite_Drink` (`Favourite_Drink`),
  CONSTRAINT `Person_ibfk_1` FOREIGN KEY (`Favourite_Drink`) REFERENCES `Drinks` (`DrinkID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Person` (`PersonID`, `Person_First_Name`, `Person_Surname`, `Person_Age`, `Favourite_Drink`) VALUES
(1,	'Jack',	'Palmer',	24,	2),
(2,	'Jimothy',	'Lacoste',	22,	NULL),
(3,	'John',	'Doe',	40,	NULL),
(4,	'Silvia',	'Potter',	24,	NULL);