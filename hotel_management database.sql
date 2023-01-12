-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 12, 2023 at 09:51 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking_details`
--

CREATE TABLE `booking_details` (
  `bill_id` int(11) NOT NULL,
  `room_number` varchar(100) NOT NULL,
  `book_date` date NOT NULL,
  `book_time` time NOT NULL,
  `payment_amount` int(11) NOT NULL,
  `payment_method` varchar(50) NOT NULL,
  `number_of_people` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `Complimentary_breakfast` tinyint(1) NOT NULL,
  `check_out_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking_details`
--

INSERT INTO `booking_details` (`bill_id`, `room_number`, `book_date`, `book_time`, `payment_amount`, `payment_method`, `number_of_people`, `customer_id`, `Complimentary_breakfast`, `check_out_date`) VALUES
(1, '1', '2022-01-01', '09:08:01', 8000, 'UPI', 3, 1, 0, '2022-01-04'),
(2, '2', '2022-01-02', '10:15:07', 7000, 'Net banking', 1, 2, 0, '2023-01-05'),
(3, '3', '2022-01-03', '11:11:11', 6000, 'Credit card', 2, 3, 0, '2022-01-06'),
(4, '6', '2023-01-08', '10:51:56', 56678, 'UPI', 8, 4, 1, '2023-01-11');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `age` int(11) NOT NULL,
  `sex` varchar(10) NOT NULL,
  `address` varchar(255) NOT NULL,
  `adhaar_number` bigint(12) NOT NULL,
  `room_number` varchar(100) NOT NULL,
  `bill_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `name`, `phone`, `age`, `sex`, `address`, `adhaar_number`, `room_number`, `bill_id`) VALUES
(1, 'amit', 9863789370, 23, 'male', 'address1', 123456789001, '1', 1),
(2, 'sumit', 7793628373, 29, 'male', 'address2', 123456789002, '2', 2),
(3, 'rajlakshmi', 8796574984, 19, 'female', 'address3', 123456789003, '3', 3),
(4, 'dfghj', 9876543212, 98, 'f', 'adfhj', 98765432123, '6', 4);

-- --------------------------------------------------------

--
-- Table structure for table `managers`
--

CREATE TABLE `managers` (
  `manager_id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `managers`
--

INSERT INTO `managers` (`manager_id`, `username`, `password`) VALUES
(1, 'reva', '827ccb0eea8a706c4c34a16891f84e7b'),
(2, 'test', '81dc9bdb52d04dc20036dbd8313ed055');

-- --------------------------------------------------------

--
-- Table structure for table `manager_logins`
--

CREATE TABLE `manager_logins` (
  `manager_id` varchar(10) NOT NULL,
  `username` varchar(30) NOT NULL,
  `time_of_login` time DEFAULT NULL,
  `date_of_login` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `manager_logins`
--

INSERT INTO `manager_logins` (`manager_id`, `username`, `time_of_login`, `date_of_login`) VALUES
('1', 'reva', '19:45:19', '2023-01-10'),
('1', 'reva', '19:46:46', '2023-01-10'),
('2', 'test', '19:58:06', '2023-01-10'),
('2', '1234', '19:59:32', '2023-01-10'),
('3', '3', '13:08:41', '2023-01-11'),
('4', '4', '13:17:27', '2023-01-11'),
('4', '4', '13:21:54', '2023-01-11'),
('4', '4', '13:24:38', '2023-01-11'),
('4', '4', '13:51:09', '2023-01-11'),
('4', '4', '14:17:46', '2023-01-11'),
('4', '4', '14:18:49', '2023-01-11'),
('4', '4', '14:20:29', '2023-01-11'),
('4', '4', '14:22:11', '2023-01-11'),
('4', '4', '14:23:06', '2023-01-11'),
('4', '4', '14:24:59', '2023-01-11'),
('4', '4', '14:48:03', '2023-01-11'),
('4', '4', '16:43:35', '2023-01-11'),
('4', '4', '10:07:05', '2023-01-12'),
('1', 'reva', '13:34:39', '2023-01-12'),
('1', 'reva', '13:43:28', '2023-01-12'),
('1', 'reva', '13:56:04', '2023-01-12'),
('1', 'reva', '13:57:19', '2023-01-12'),
('1', 'reva', '14:04:52', '2023-01-12'),
('1', 'reva', '14:12:11', '2023-01-12'),
('1', 'reva', '14:19:36', '2023-01-12');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `room_number` varchar(100) NOT NULL DEFAULT '000',
  `room_type` varchar(100) NOT NULL,
  `room_rate` int(11) NOT NULL,
  `availability` tinyint(1) NOT NULL DEFAULT 1,
  `occupant` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`room_number`, `room_type`, `room_rate`, `availability`, `occupant`) VALUES
('1', '1 Bed AC', 8000, 0, 1),
('2', '1 Bed Non-AC', 7000, 0, 2),
('3', '2 Bed AC', 6000, 0, 3),
('4', '2 Bed Non-AC', 5000, 1, 0),
('5', '3 Bed AC', 4000, 1, 0),
('6', '3 Bed Non-AC', 3000, 0, 4),
('7', '4 Bed AC', 2000, 1, 0),
('8', '4 Bed Non-AC', 1000, 1, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking_details`
--
ALTER TABLE `booking_details`
  ADD PRIMARY KEY (`bill_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `adhaar_number` (`adhaar_number`);

--
-- Indexes for table `managers`
--
ALTER TABLE `managers`
  ADD PRIMARY KEY (`manager_id`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`room_number`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking_details`
--
ALTER TABLE `booking_details`
  MODIFY `bill_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
