# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: bioed.bu.edu (MySQL 5.5.5-10.1.44-MariaDB)
# Database: groupA
# Generation Time: 2020-03-19 18:33:00 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table relationship
# ------------------------------------------------------------

DROP TABLE IF EXISTS `relationship`;

CREATE TABLE `relationship` (
  `relationship_id` int(11) NOT NULL AUTO_INCREMENT,
  `species_id` int(11) DEFAULT NULL,
  `transposon_id` int(11) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `coverage` int(11) DEFAULT NULL,
  PRIMARY KEY (`relationship_id`),
  KEY `species_id` (`species_id`),
  KEY `transposon_id` (`transposon_id`),
  CONSTRAINT `relationship_ibfk_1` FOREIGN KEY (`species_id`) REFERENCES `species` (`species_id`),
  CONSTRAINT `relationship_ibfk_2` FOREIGN KEY (`transposon_id`) REFERENCES `transposon` (`transposon_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table species
# ------------------------------------------------------------

DROP TABLE IF EXISTS `species`;

CREATE TABLE `species` (
  `species_id` int(11) NOT NULL AUTO_INCREMENT,
  `species_name` char(50) DEFAULT NULL,
  PRIMARY KEY (`species_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table transcript
# ------------------------------------------------------------

DROP TABLE IF EXISTS `transcript`;

CREATE TABLE `transcript` (
  `transcript_id` int(11) NOT NULL AUTO_INCREMENT,
  `sequence` char(50) DEFAULT NULL,
  `length` int(11) DEFAULT NULL,
  `transposon_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`transcript_id`),
  KEY `transposon_id` (`transposon_id`),
  CONSTRAINT `transcript_ibfk_1` FOREIGN KEY (`transposon_id`) REFERENCES `transposon` (`transposon_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table transposon
# ------------------------------------------------------------

DROP TABLE IF EXISTS `transposon`;

CREATE TABLE `transposon` (
  `transposon_id` int(11) NOT NULL AUTO_INCREMENT,
  `accession` char(20) DEFAULT NULL,
  `type` char(20) DEFAULT NULL,
  `name` char(20) DEFAULT NULL,
  `header` char(100) DEFAULT NULL,
  PRIMARY KEY (`transposon_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
