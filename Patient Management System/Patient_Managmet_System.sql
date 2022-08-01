create database patient_db

use patient_db

create table patientDetails(
	patientId int primary key,
	patientName varchar(25),
	gender varchar(5),
	age varchar(5),
	bloodGroup varchar(5)
	);
