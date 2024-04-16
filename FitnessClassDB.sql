CREATE DATABASE fitness_class;
USE fitness_class;

CREATE TABLE `class_bookings` (
  `class_id` int(11) AUTO_INCREMENT PRIMARY KEY,
  `class_name` varchar(100) DEFAULT NULL,
  `12-13` int(11) DEFAULT NULL,
  `12-13_booking_id` varchar(20) DEFAULT NULL,
  `13-14` int(11) DEFAULT NULL,
  `13-14_booking_id` varchar(20) DEFAULT NULL,
  `14-15` int(11) DEFAULT NULL,
  `14-15_booking_id` varchar(20) DEFAULT NULL,
  `15-16` int(11) DEFAULT NULL,
  `15-16_booking_id` varchar(20) DEFAULT NULL,
  `16-17` int(11) DEFAULT NULL,
  `16-17_booking_id` varchar(20) DEFAULT NULL,
  `17-18` int(11) DEFAULT NULL,
  `17-18_booking_id` varchar(20) DEFAULT NULL,
  `booking_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `fill_dates`(dateStart DATE, dateEnd DATE, className VARCHAR(100))
BEGIN
  WHILE dateStart <= dateEnd DO
    INSERT INTO class_bookings (class_name, booking_date) VALUES (className, dateStart);
    SET dateStart = date_add(dateStart, INTERVAL 1 DAY);
  END WHILE;
END$$
DELIMITER ;
