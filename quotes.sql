-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: quotesDB
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `favorites`
--

DROP TABLE IF EXISTS `favorites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `favorites` (
  `users_id` int(11) NOT NULL,
  `quotes_id` int(11) NOT NULL,
  PRIMARY KEY (`users_id`,`quotes_id`),
  KEY `fk_users_has_quotes_quotes1_idx` (`quotes_id`),
  KEY `fk_users_has_quotes_users_idx` (`users_id`),
  CONSTRAINT `fk_users_has_quotes_users` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_quotes_quotes1` FOREIGN KEY (`quotes_id`) REFERENCES `quotes` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorites`
--

LOCK TABLES `favorites` WRITE;
/*!40000 ALTER TABLE `favorites` DISABLE KEYS */;
INSERT INTO `favorites` VALUES (3,3),(3,4),(3,6),(3,8);
/*!40000 ALTER TABLE `favorites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quotes`
--

DROP TABLE IF EXISTS `quotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quotes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author` varchar(45) DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  `poster_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_quotes_users1_idx` (`poster_id`),
  CONSTRAINT `fk_quotes_users1` FOREIGN KEY (`poster_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quotes`
--

LOCK TABLES `quotes` WRITE;
/*!40000 ALTER TABLE `quotes` DISABLE KEYS */;
INSERT INTO `quotes` VALUES (1,'Ralph Waldo Emerson','Do not go where the path may lead, go instead where there is no path and leave a trail',2,'2016-07-22 09:43:33','2016-07-22 09:43:33'),(2,'Aldous Huxley','Experience is not what happens to you; it\'s what you do with what happens to you',3,'2016-07-22 09:43:33','2016-07-22 09:43:33'),(3,'Will Arthur Ward','The pessimist complains about the wind; the optimist expects it to change; the realist adjusts the sails.',4,'2016-07-22 09:43:33','2016-07-22 09:43:33'),(4,'Nelson Mandela','If you talk to a man in a language he understands, that goes to his head. If you talk to him in his language, that goes to his heart.',5,'2016-07-22 09:43:33','2016-07-22 09:43:33'),(5,'John Maxwell','A man must be big enough to admit his mistakes, smart enough to profit from them, and strong enough to correct them',3,'2016-07-22 09:43:33','2016-07-22 09:43:33'),(6,'Henry Thoreau','It\'s not what you look at that matters, it\'s what you see.',4,'2016-07-22 09:43:33','2016-07-22 09:43:33'),(7,'Brendan','Take the test!',3,'2016-07-22 12:56:54','2016-07-22 12:56:54'),(8,'Brendan','Take the test!',3,'2016-07-22 12:57:24','2016-07-22 12:57:24');
/*!40000 ALTER TABLE `quotes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `alias` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `birthday` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'Gracia','Gracia','gr@gmail.com','password',NULL,'2016-07-22 09:43:33','2016-07-22 09:43:33'),(3,'user','user','user@gmail.com','$2b$12$BRFrHg89/.rs68iSoa64GON309GwCHXSdWVoJr4GOpBuKDmsxs4CW',NULL,'2016-07-22 09:43:33','2016-07-22 09:43:33'),(4,'Oliver','Oliver','ol@gmail.com','password',NULL,'2016-07-22 09:43:33','2016-07-22 09:43:33'),(5,'KB','KB','kb@gmail.com','password',NULL,'2016-07-22 09:43:33','2016-07-22 09:43:33'),(12,'Jim','Jim','ji@gmail.com','$2b$12$BRFrHg89/.rs68iSoa64GON309GwCHXSdWVoJr4GOpBuKDmsxs4CW','1986-01-01 00:00:00','2016-07-22 12:12:30','2016-07-22 12:12:30');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-22 13:08:57
