-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 01, 2024 at 05:28 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `py_test_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `delays`
--

CREATE TABLE `delays` (
  `Car_ID` longtext NOT NULL,
  `Start_Gate` varchar(255) NOT NULL,
  `End_Gate` varchar(255) NOT NULL,
  `Start_Date` longtext NOT NULL,
  `Arrival_End_Date` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `delays`
--

INSERT INTO `delays` (`Car_ID`, `Start_Gate`, `End_Gate`, `Start_Date`, `Arrival_End_Date`) VALUES
('1_Car', 'Giza', 'Qalyubia', '2024-03-11 16:13:25', '2024-03-11 17:19:47'),
('1_Car', 'Giza', 'Qalyubia', '2024-03-11 16:13:25', '2024-03-11 17:30:29'),
('2_Car', 'Cairo', 'Giza', '2024-03-12 14:46:06', '2024-03-12 14:49:49'),
('3_Car', 'Cairo', 'Giza', '2024-03-14 16:54:28', '2024-03-14 16:58:16'),
('1_Car', 'Cairo', 'Giza', '2024-03-14 20:59:54', '2024-03-14 21:05:41');

-- --------------------------------------------------------

--
-- Table structure for table `travels`
--

CREATE TABLE `travels` (
  `ID` varchar(255) DEFAULT NULL,
  `Start_Gate` varchar(255) DEFAULT NULL,
  `End_Gate` varchar(255) DEFAULT NULL,
  `Distance` int(10) DEFAULT NULL,
  `Start_Travel_Date` longtext NOT NULL,
  `End_Travel_Date` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `travels`
--

INSERT INTO `travels` (`ID`, `Start_Gate`, `End_Gate`, `Distance`, `Start_Travel_Date`, `End_Travel_Date`) VALUES
('3_Car-CA', 'Cairo', 'Giza', 7, '2024-03-12 17:53:18', '2024-03-12 17:56:45'),
('3_Car-CA', 'Cairo', 'Giza', 7, '2024-03-12 17:53:43', '2024-03-12 17:57:10'),
('3_Car-GIZ', 'Giza', 'Qalyubia', 32, '2024-03-12 21:01:09', '2024-03-12 21:17:03'),
('6_Car-GIZ', 'Giza', 'Qalyubia', 32, '2024-03-14 15:26:26', '2024-03-14 15:42:20'),
('6_Car-GIZ', 'Giza', 'Qalyubia', 32, '2024-03-14 16:44:23', '2024-03-14 17:00:17'),
('3_Car-CA', 'Cairo', 'Giza', 7, '2024-03-14 16:44:34', '2024-03-14 16:48:01'),
('3_Car-CA', 'Cairo', 'Giza', 7, '2024-03-14 16:54:25', '2024-03-14 16:57:52'),
('3_Car-GIZ', 'Giza', 'Qalyubia', 32, '2024-03-14 16:58:10', '2024-03-14 17:14:04'),
('51_Car-CA', 'Cairo', 'Giza', 7, '2024-03-14 17:06:14', '2024-03-14 17:09:41'),
('51_Car-GIZ', 'Giza', 'Qalyubia', 32, '2024-03-14 17:06:19', '2024-03-14 17:22:13'),
('51_Car-GIZ', 'Giza', 'Qalyubia', 32, '2024-03-14 17:06:29', '2024-03-14 17:22:23'),
('4_Car-GIZ', 'Giza', 'Qalyubia', 32, '2024-03-14 17:29:16', '2024-03-14 17:45:10'),
('4_Car-CA', 'Cairo', 'Giza', 7, '2024-03-14 17:32:17', '2024-03-14 17:35:44'),
('4_Car-GIZ', 'Giza', 'Qalyubia', 32, '2024-03-14 17:35:20', '2024-03-14 17:51:14'),
('4_Car-CA', 'Cairo', 'Giza', 7, '2024-03-14 17:40:47', '2024-03-14 17:44:14'),
('1_Car-CA', 'Cairo', 'Giza', 7, '2024-03-14 20:59:54', '2024-03-14 21:03:21'),
('1_Car-GIZ', 'Giza', 'Qalyubia', 32, '2024-03-14 21:05:36', '2024-03-14 21:21:30'),
('1_Car-GIZ', 'Giza', 'Qalyubia', 32, '2024-03-16 16:59:35', '2024-03-16 17:15:29');

-- --------------------------------------------------------

--
-- Table structure for table `violations`
--

CREATE TABLE `violations` (
  `Car_ID` longtext DEFAULT NULL,
  `Start_Gate` varchar(255) DEFAULT NULL,
  `End_Gate` varchar(255) DEFAULT NULL,
  `Start_Date` longtext DEFAULT NULL,
  `Arrival_End_Date` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `violations`
--

INSERT INTO `violations` (`Car_ID`, `Start_Gate`, `End_Gate`, `Start_Date`, `Arrival_End_Date`) VALUES
('1_Car', 'Cairo', 'Giza', '2024-03-11 14:32:11', '2024-03-11 14:32:47'),
('1_Car', 'Cairo', 'Giza', '2024-03-11 15:11:18', '2024-03-11 15:14:03'),
('2_Car', 'Cairo', 'Giza', '2024-03-11 15:21:56', '2024-03-11 15:22:15'),
('2_Car', 'Cairo', 'Giza', '2024-03-11 15:21:56', '2024-03-11 15:22:19'),
('2_Car', 'Giza', 'Qalyubia', '2024-03-11 15:22:12', '2024-03-11 15:22:47'),
('2_Car', 'Giza', 'Qalyubia', '2024-03-11 15:22:12', '2024-03-11 15:23:52'),
('1_Car', 'Giza', 'Qalyubia', '2024-03-11 15:34:01', '2024-03-11 15:35:53'),
('1_Car', 'Giza', 'Qalyubia', '2024-03-11 16:12:46', '2024-03-11 16:12:59'),
('1_Car', 'Cairo', 'Giza', '2024-03-11 16:12:55', '2024-03-11 16:13:29'),
('1_Car', 'Giza', 'Qalyubia', '2024-03-11 17:42:32', '2024-03-11 17:51:21'),
('2_Car', 'Giza', 'Qalyubia', '2024-03-12 14:43:34', '2024-03-12 14:46:13'),
('4_Car', 'Giza', 'Qalyubia', '2024-03-14 17:35:20', '2024-03-14 17:40:52');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
