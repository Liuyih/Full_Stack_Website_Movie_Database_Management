
# Dump of table actor
# ------------------------------------------------------------

DROP TABLE IF EXISTS `actor`;

CREATE TABLE `actor` (
  `actor_id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`actor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `actor` WRITE;
/*!40000 ALTER TABLE `actor` DISABLE KEYS */;

INSERT INTO `actor` (`actor_id`, `fname`, `lname`)
VALUES
	(1,'Callandraaaaa','Henderson'),
	(2,'linda','goober'),
	(3,'harry','humphery'),
	(4,'test_fname','goober'),
	(12,'linda','Walson'),
	(15,'Gerard','Butler');

/*!40000 ALTER TABLE `actor` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table director
# ------------------------------------------------------------

DROP TABLE IF EXISTS `director`;

CREATE TABLE `director` (
  `director_id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`director_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `director` WRITE;
/*!40000 ALTER TABLE `director` DISABLE KEYS */;

INSERT INTO `director` (`director_id`, `fname`, `lname`)
VALUES
	(2,'Harry','Goober'),
	(3,'Stephen','Spielberg'),
	(17,'linda','goober');

/*!40000 ALTER TABLE `director` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table genre
# ------------------------------------------------------------

DROP TABLE IF EXISTS `genre`;

CREATE TABLE `genre` (
  `genre_id` int(11) NOT NULL AUTO_INCREMENT,
  `genre_type` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;

INSERT INTO `genre` (`genre_id`, `genre_type`)
VALUES
	(1,'action'),
	(2,'kung fu'),
	(3,'science fiction'),
	(4,'horror'),
	(5,'Bollywood');

/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table movie
# ------------------------------------------------------------

DROP TABLE IF EXISTS `movie`;

CREATE TABLE `movie` (
  `movie_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `release_date` date DEFAULT NULL,
  PRIMARY KEY (`movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;

INSERT INTO `movie` (`movie_id`, `title`, `release_date`)
VALUES
	(1,'Four Rooms','1995-12-20'),
	(2,'Raptor','1998-01-21'),
	(3,'Viper2','1994-12-21'),
	(4,'Mechanic','2008-02-02'),
	(5,'Commander','2010-02-25');

/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table movie_cast
# ------------------------------------------------------------

DROP TABLE IF EXISTS `movie_cast`;

CREATE TABLE `movie_cast` (
  `movie_id` int(11) DEFAULT NULL,
  `actor_id` int(11) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL,
  KEY `movie_id` (`movie_id`),
  KEY `actor_id` (`actor_id`),
  CONSTRAINT `movie_cast_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`movie_id`),
  CONSTRAINT `movie_cast_ibfk_2` FOREIGN KEY (`actor_id`) REFERENCES `actor` (`actor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `movie_cast` WRITE;
/*!40000 ALTER TABLE `movie_cast` DISABLE KEYS */;

INSERT INTO `movie_cast` (`movie_id`, `actor_id`, `role`)
VALUES
	(1,1,'Jack Sparrow'),
	(2,2,'Will Turner'),
	(5,4,'Graves'),
	(3,4,'rap god'),
	(2,1,'miss fortune');

/*!40000 ALTER TABLE `movie_cast` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table movie_direct
# ------------------------------------------------------------

DROP TABLE IF EXISTS `movie_direct`;

CREATE TABLE `movie_direct` (
  `movie_id` int(11) DEFAULT NULL,
  `director_id` int(11) DEFAULT NULL,
  UNIQUE KEY `movie_id_2` (`movie_id`),
  KEY `movie_id` (`movie_id`),
  KEY `director_id` (`director_id`),
  CONSTRAINT `movie_direct_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`movie_id`),
  CONSTRAINT `movie_direct_ibfk_2` FOREIGN KEY (`director_id`) REFERENCES `director` (`director_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `movie_direct` WRITE;
/*!40000 ALTER TABLE `movie_direct` DISABLE KEYS */;

INSERT INTO `movie_direct` (`movie_id`, `director_id`)
VALUES
	(1,2),
	(2,2),
	(3,3),
	(4,17);

/*!40000 ALTER TABLE `movie_direct` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table movie_genre
# ------------------------------------------------------------

DROP TABLE IF EXISTS `movie_genre`;

CREATE TABLE `movie_genre` (
  `movie_id` int(11) DEFAULT NULL,
  `genre_id` int(11) DEFAULT NULL,
  KEY `movie_id` (`movie_id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `movie_genre_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`movie_id`),
  CONSTRAINT `movie_genre_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `genre` (`genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `movie_genre` WRITE;
/*!40000 ALTER TABLE `movie_genre` DISABLE KEYS */;

INSERT INTO `movie_genre` (`movie_id`, `genre_id`)
VALUES
	(1,1),
	(2,2),
	(4,2),
	(5,5),
	(5,4);

/*!40000 ALTER TABLE `movie_genre` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
