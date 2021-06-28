-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: moving
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `application_of_moving`
--

DROP TABLE IF EXISTS `application_of_moving`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `application_of_moving` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `departure_point` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `departure_floor` int NOT NULL,
  `destination_point` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `destination_floor` int NOT NULL,
  `moving_date` date NOT NULL,
  `storaging_moving` tinyint(1) NOT NULL,
  `customer_information_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `application_of_movin_customer_information_4fbee2cb_fk_customer_` (`customer_information_id`),
  CONSTRAINT `application_of_movin_customer_information_4fbee2cb_fk_customer_` FOREIGN KEY (`customer_information_id`) REFERENCES `customer_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `application_of_moving`
--

LOCK TABLES `application_of_moving` WRITE;
/*!40000 ALTER TABLE `application_of_moving` DISABLE KEYS */;
/*!40000 ALTER TABLE `application_of_moving` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,'1t'),(2,'2.5t'),(3,'5t'),(4,'etc');
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_car`
--

DROP TABLE IF EXISTS `company_car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_car` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `car_id` bigint NOT NULL,
  `company_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `company_car_company_id_e94858de_fk_company_information_id` (`company_id`),
  KEY `company_car_car_id_eb553286_fk_car_id` (`car_id`),
  CONSTRAINT `company_car_car_id_eb553286_fk_car_id` FOREIGN KEY (`car_id`) REFERENCES `car` (`id`),
  CONSTRAINT `company_car_company_id_e94858de_fk_company_information_id` FOREIGN KEY (`company_id`) REFERENCES `company_information` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_car`
--

LOCK TABLES `company_car` WRITE;
/*!40000 ALTER TABLE `company_car` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_information`
--

DROP TABLE IF EXISTS `company_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_information` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `master` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `phone_number` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `business_number` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `business_registration_date` date NOT NULL,
  `staff` int NOT NULL,
  `matching` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_information`
--

LOCK TABLES `company_information` WRITE;
/*!40000 ALTER TABLE `company_information` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_information`
--

DROP TABLE IF EXISTS `customer_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_information` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  `phone_number` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `terms_of_use` tinyint(1) NOT NULL,
  `personal_information` tinyint(1) NOT NULL,
  `marketing_information` tinyint(1) NOT NULL,
  `customer_registration_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_information`
--

LOCK TABLES `customer_information` WRITE;
/*!40000 ALTER TABLE `customer_information` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'contenttypes','contenttype'),(3,'information','application_of_moving'),(4,'information','car'),(5,'information','company_car'),(6,'information','customerinfomation'),(10,'information','customer_feedback_history'),(9,'information','moving_company_information'),(7,'information','moving_type'),(8,'information','satisfaction'),(2,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-06-28 13:20:52.932066'),(2,'contenttypes','0002_remove_content_type_name','2021-06-28 13:20:53.318027'),(3,'information','0001_initial','2021-06-28 13:20:57.205225'),(4,'sessions','0001_initial','2021-06-28 13:20:57.421431');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_history`
--

DROP TABLE IF EXISTS `feedback_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback_history` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `opening_information` tinyint(1) NOT NULL,
  `revisit` tinyint(1) NOT NULL,
  `price` int NOT NULL,
  `feeadback_date` date NOT NULL,
  `feedback` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `company_information_id` bigint NOT NULL,
  `information_id` bigint NOT NULL,
  `kindness_satisfaction_id` bigint NOT NULL,
  `moving_type_id` bigint NOT NULL,
  `price_satisfaction_id` bigint NOT NULL,
  `professional_satisfaction_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `feedback_history_company_information__9c0a777f_fk_company_i` (`company_information_id`),
  KEY `feedback_history_information_id_eb2c998a_fk_applicati` (`information_id`),
  KEY `feedback_history_kindness_satisfactio_408a67d8_fk_satisfact` (`kindness_satisfaction_id`),
  KEY `feedback_history_moving_type_id_d2336f7d_fk_moving_type_id` (`moving_type_id`),
  KEY `feedback_history_price_satisfaction_i_82553f12_fk_satisfact` (`price_satisfaction_id`),
  KEY `feedback_history_professional_satisfa_2275c2be_fk_satisfact` (`professional_satisfaction_id`),
  CONSTRAINT `feedback_history_company_information__9c0a777f_fk_company_i` FOREIGN KEY (`company_information_id`) REFERENCES `company_information` (`id`),
  CONSTRAINT `feedback_history_information_id_eb2c998a_fk_applicati` FOREIGN KEY (`information_id`) REFERENCES `application_of_moving` (`id`),
  CONSTRAINT `feedback_history_kindness_satisfactio_408a67d8_fk_satisfact` FOREIGN KEY (`kindness_satisfaction_id`) REFERENCES `satisfaction` (`id`),
  CONSTRAINT `feedback_history_moving_type_id_d2336f7d_fk_moving_type_id` FOREIGN KEY (`moving_type_id`) REFERENCES `moving_type` (`id`),
  CONSTRAINT `feedback_history_price_satisfaction_i_82553f12_fk_satisfact` FOREIGN KEY (`price_satisfaction_id`) REFERENCES `satisfaction` (`id`),
  CONSTRAINT `feedback_history_professional_satisfa_2275c2be_fk_satisfact` FOREIGN KEY (`professional_satisfaction_id`) REFERENCES `satisfaction` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_history`
--

LOCK TABLES `feedback_history` WRITE;
/*!40000 ALTER TABLE `feedback_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedback_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `moving_type`
--

DROP TABLE IF EXISTS `moving_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `moving_type` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moving_type`
--

LOCK TABLES `moving_type` WRITE;
/*!40000 ALTER TABLE `moving_type` DISABLE KEYS */;
INSERT INTO `moving_type` VALUES (1,'가정이사'),(2,'원룸이사');
/*!40000 ALTER TABLE `moving_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `satisfaction`
--

DROP TABLE IF EXISTS `satisfaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `satisfaction` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satisfaction`
--

LOCK TABLES `satisfaction` WRITE;
/*!40000 ALTER TABLE `satisfaction` DISABLE KEYS */;
INSERT INTO `satisfaction` VALUES (1,'매우만족'),(2,'만족'),(3,'보통'),(4,'불만족'),(5,'매우불만족');
/*!40000 ALTER TABLE `satisfaction` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-28 22:41:53
