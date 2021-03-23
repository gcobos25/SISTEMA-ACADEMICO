-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: kairos
-- ------------------------------------------------------
-- Server version	5.7.31-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `academicokairos_configuracionusuario`
--

LOCK TABLES `academicokairos_configuracionusuario` WRITE;
/*!40000 ALTER TABLE `academicokairos_configuracionusuario` DISABLE KEYS */;
INSERT INTO `academicokairos_configuracionusuario` VALUES (1,'Jioska','Jioska1290');
/*!40000 ALTER TABLE `academicokairos_configuracionusuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add (\'Usuario\',)',7,'add_configuracionusuario'),(26,'Can change (\'Usuario\',)',7,'change_configuracionusuario'),(27,'Can delete (\'Usuario\',)',7,'delete_configuracionusuario'),(28,'Can view (\'Usuario\',)',7,'view_configuracionusuario');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$6vKcGyTVlwg8$spI3a0oRJkH7palNpFvhnSC/EtZMDpPPQ4zCB5srlf0=','2021-03-22 00:59:39.612666',1,'J10SK4','','','JIOSKA@gmail.com',1,1,'2021-03-22 00:53:53.046587');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-03-22 01:12:45.703233','1','Jioska',1,'[{\"added\": {}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (7,'AcademicoKairos','configuracionusuario'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-03-22 00:38:43.645124'),(2,'auth','0001_initial','2021-03-22 00:38:47.666952'),(3,'admin','0001_initial','2021-03-22 00:39:03.428630'),(4,'admin','0002_logentry_remove_auto_add','2021-03-22 00:39:06.730935'),(5,'admin','0003_logentry_add_action_flag_choices','2021-03-22 00:39:06.846923'),(6,'contenttypes','0002_remove_content_type_name','2021-03-22 00:39:09.313956'),(7,'auth','0002_alter_permission_name_max_length','2021-03-22 00:39:09.807479'),(8,'auth','0003_alter_user_email_max_length','2021-03-22 00:39:10.116147'),(9,'auth','0004_alter_user_username_opts','2021-03-22 00:39:10.230146'),(10,'auth','0005_alter_user_last_login_null','2021-03-22 00:39:11.878906'),(11,'auth','0006_require_contenttypes_0002','2021-03-22 00:39:11.945638'),(12,'auth','0007_alter_validators_add_error_messages','2021-03-22 00:39:12.028669'),(13,'auth','0008_alter_user_username_max_length','2021-03-22 00:39:12.276548'),(14,'auth','0009_alter_user_last_name_max_length','2021-03-22 00:39:12.531041'),(15,'auth','0010_alter_group_name_max_length','2021-03-22 00:39:12.764338'),(16,'auth','0011_update_proxy_permissions','2021-03-22 00:39:12.837606'),(17,'auth','0012_alter_user_first_name_max_length','2021-03-22 00:39:13.047089'),(18,'sessions','0001_initial','2021-03-22 00:39:13.571581'),(19,'AcademicoKairos','0001_initial','2021-03-22 01:12:17.035652');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ouu4c1ceof8zl8xr15xqqrcmkh3agvq8','.eJxVjMEOwiAQRP-FsyEsLcvq0bvfQBaWStXQpLQn47_bJj3obTLvzbxV4HUpYW15DqOoiwJ1-u0ip2euO5AH1_uk01SXeYx6V_RBm75Nkl_Xw_07KNzKtkbImIRsz94LbsEbAAQrAAznPiN5zylbI466aFyXBodEBMQ4OEjq8wW_zDbn:1lO8ux:UGeoYdX5JFPJZ-cW9nxshAUBI3ZPzQNTahz9QuxdhP0','2021-04-05 00:59:39.703664');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-21 20:16:49
