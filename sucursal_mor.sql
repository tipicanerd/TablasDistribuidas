-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 04, 2021 at 03:33 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Morelia`
--

-- --------------------------------------------------------

--
-- Table structure for table `clientes`
--

CREATE TABLE `clientes` (
  `id` char(9) NOT NULL,
  `nombre` varchar(250) NOT NULL,
  `apellidoPaterno` varchar(250) DEFAULT NULL,
  `apellidoMaterno` varchar(250) DEFAULT NULL,
  `RFC` char(13) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `clientes`
--

INSERT INTO `clientes` (`id`, `nombre`, `apellidoPaterno`, `apellidoMaterno`, `RFC`) VALUES
('MOR000001', 'Juan', 'Pedraza', 'Baltazar', 'ODH16578K9564'),
('MOR000002', 'Ana Sofía', 'Cruz', 'López', 'IKJ7864KL0981'),
('MOR000003', 'Juan Pablo', 'Maldonado', 'Castro', 'IUL198657UGH1'),
('MOR000004', 'Diego', 'Jimenez', 'Negrón', 'LNWT123456789'),
('MOR000005', 'Natalia', 'Pérez', 'García', 'HFO98356H8JK3'),
('MOR000006', 'Tania', 'Díaz', 'Mur', 'UIE78564J39K1'),
('MOR000007', 'Jorge', 'Fuentes', 'Zapata', 'LOP19847681K6'),
('MOR000008', 'Goku', 'Hernandez', 'López', 'KOFJ8196HKLM1'),
('MOR000009', 'Brayan', 'Castro', 'Piña', 'KID91H56781KM'),
('MOR000010', 'Azul', 'Maldonado', 'Zapata', 'HDF56783KMDHA'),
('MOR000011', 'Canela', 'Vázquez', 'Molina', 'LOQSJ81657JM3'),
('MOR000012', 'Montserrat', 'Fuentes', 'Fuentes', 'HGN185674H9K9'),
('MOR000013', 'José', 'Solís', 'Del Toro', 'LMK563HNJ8123'),
('MOR000014', 'Zoe', 'Martínez', 'González', 'POT1381892K13'),
('MOR000015', 'Valeria', 'Castro', 'Piña', 'HJA1758G8LNE5'),
('MOR000016', 'José', 'Carlos', 'Esparza', 'BRY17589LKMN1');

-- --------------------------------------------------------

--
-- Table structure for table `direcciones`
--

CREATE TABLE `direcciones` (
  `id_cliente` char(9) DEFAULT NULL,
  `id` int(6) UNSIGNED ZEROFILL NOT NULL,
  `calle` varchar(250) DEFAULT NULL,
  `numero` int(11) DEFAULT NULL,
  `Colonia` varchar(250) DEFAULT NULL,
  `Estado` varchar(250) DEFAULT NULL,
  `CP` char(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `direcciones`
--

INSERT INTO `direcciones` (`id_cliente`, `id`, `calle`, `numero`, `Colonia`, `Estado`, `CP`) VALUES
('MOR000001', 000001, 'Palomas', 192, 'Rincón de los Pájaros', 'Michoacán', '58012'),
('MOR000002', 000002, 'Avestruz', 741, 'Rincón de los Pájaros', 'Michoacán', '58012'),
('MOR000003', 000003, 'Avestruz', 812, 'Rincón de los Pájaros', 'Michoacán', '58192'),
('MOR000004', 000004, 'Avestruz', 113, 'Rincón de los Pájaros', 'Michoacán', '58192'),
('MOR000004', 000005, 'Pera', 999, 'Las Frutas', 'Michoacán', '58012'),
('MOR000005', 000006, 'Pera', 91, 'Las Frutas', 'Michoacán', '58001'),
('MOR000006', 000007, 'Mango', 83, 'Las Frutas', 'Michoacán', '58912'),
('MOR000007', 000008, 'Plátano', 12, 'Las Frutas', 'Michoacán', '58952'),
('MOR000008', 000009, 'Palomitas', 100, 'Las Botanas', 'Michoacán', '89123'),
('MOR000009', 000010, 'Papas', 812, 'Las Botanas', 'Michoacán', '89131'),
('MOR000010', 000011, 'Salami', 321, 'Las Carnes', 'Michoacán', '76182'),
('MOR000011', 000012, 'Salami', 321, 'Las Carnes', 'Michoacán', '76182'),
('MOR000012', 000013, 'Tierra', 3, 'Sistema Solar', 'Michoacán', '12345'),
('MOR000013', 000014, 'Venus', 2, 'Sistema Solar', 'Michoacán', '12345'),
('MOR000014', 000015, 'Mercurio', 1, 'Sistema Solar', 'Michoacán', '12345'),
('MOR000015', 000016, 'Golden Retriever', 100, 'Doggos', 'Michoacán', '54325'),
('MOR000016', 000017, 'Husky', 210, 'Doggos', 'Michoacán', '81313');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `RFC` (`RFC`);

--
-- Indexes for table `direcciones`
--
ALTER TABLE `direcciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_cliente` (`id_cliente`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `direcciones`
--
ALTER TABLE `direcciones`
  MODIFY `id` int(6) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `direcciones`
--
ALTER TABLE `direcciones`
  ADD CONSTRAINT `direcciones_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
