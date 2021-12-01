-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: apatzingan
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES ('APA000001','Jazmín','López','Chacón','LOCJ010807BE5'),('APA000002','Patricia Ximena','Sánchez','X','SAXP970328AQ2'),('APA000003','Carlota','Gómez','Mendoza','GOMC939101ASG'),('APA000004','Felicia','Pérez','Morales','PEMF990101AST'),('APA000005','Camila','Aguilar','Romero','AGRC870202JKN'),('APA000006','Ramiro','Rojas','Ibarra','ROIR030303AFG'),('APA000007','Pablo','Rosales','Navarro','RONP990404AQW'),('APA000008','Pablo','Rosales','Navarro','RONP990404QWD'),('APA000009','Karina','Trejo','Acosta','TRAK000927ASR'),('APA000010','Juan Gabriel','Santos','Valencia','SAVJ901020AST'),('APA000011','Luis','Miranda','Nava','MINL850818GHT'),('APA000012','Felipe','Aguilar','Torres','AGTF781111ATH'),('APA000013','Ulises','Reyes','López','RELU010122ATR'),('APA000014','Miguel','Castillo','Lara','CALM770909THI'),('APA000015','Emilia','López','Vega','LOVE010118YUI'),('APA000016','Yamilet','Ochoa','Zamora','OCZY880508AND');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `direcciones`
--

LOCK TABLES `direcciones` WRITE;
/*!40000 ALTER TABLE `direcciones` DISABLE KEYS */;
INSERT INTO `direcciones` VALUES ('APA000002',000001,'Av. Constitución',1521,'Lázaro Cárdenas','Michoacán','60630'),('APA000001',000016,'Aquiles Serdán',25,'Lázaro Cárdenas','Michoacán','60630'),('APA000002',000017,'HermanosFlores Magón',156,'Lázaro Cárdenas','Michoacán','630'),('APA000004',000018,'Víctor Rosales',180,'Ferrocarril','Michoacán','60690'),('APA000005',000019,'Manuel Morelos',321,'Ferrocarril','Michoacán','60690'),('APA000006',000020,'Nicolás Bravo',129,'Varillero','Michoacán','60660'),('APA000007',000021,'Emiliano Zapata',418,'La Florida','Michoacán','60698'),('APA000008',000022,'Emiliano Zapata',420,'La Florida','Michoacán','60698'),('APA000009',000023,'De Antonio L. Cinfuentes',678,'Apatzingán','Michoacán','60696'),('APA000010',000024,'Azahar',329,'Tierras Blancas II','Michoacán','60663'),('APA000011',000025,'Pablo Torres',239,'Emiliano Zapata','Michoacán','60616'),('APA000012',000026,'Felipe Ángeles',567,'Josefa Ortiz de Dominguez','Michoacán','60630'),('APA000013',000027,'Aldama',345,'Adolfo Ruíz Cortinez','Michoacán','60673'),('APA000014',000028,'Pedro Ascencio',908,'El Tarepe','Michoacán','60677'),('APA000015',000029,'Diana Laura',523,'Luis Donaldo Colosio','Michoacán','60633'),('APA000016',000030,'Emiliano Zapata',420,'La Florida','Michoacán','60698');
/*!40000 ALTER TABLE `direcciones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-30 20:46:15
