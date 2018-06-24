DROP DATABASE IF EXISTS activeDB;

CREATE DATABASE activeDB;

USE activeDB;

CREATE TABLE User (

  user_id INT(50) NOT NULL,
  status INT(3) DEFAULT NULL,
  PRIMARY KEY(user_id)
) Engine=InnoDB CHARACTER SET=UTF8;



CREATE TABLE FileOVPN (

  file_name VARCHAR(50) NOT NULL,
  login VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  countryName VARCHAR(50),
  stateProv VARCHAR(50),
  district VARCHAR(50),
  city VARCHAR(50),
  zip_code VARCHAR(16) NOT NULL,
  status TINYINT(1) DEFAULT NULL,
  PRIMARY KEY (file_name)
) Engine=InnoDB CHARACTER SET=UTF8;

CREATE TABLE Payment (
    pay_id INT AUTO_INCREMENT NOT NULL,
    token VARCHAR(12) NOT NULL,
    user_id INT(50) NOT NULL,
    file_name VARCHAR(50) NOT NULL,
    data_req TIMESTAMP,
    status TINYINT(1) DEFAULT NULL,
    PRIMARY KEY(pay_id),
    FOREIGN KEY(file_name) REFERENCES FileOVPN(file_name)   ON UPDATE cascade,
    FOREIGN KEY(user_id) REFERENCES User(user_id)
  ) Engine=InnoDB CHARACTER SET=UTF8;



CREATE TABLE Characteristics (
 file_name VARCHAR(50) NOT NULL,
 site VARCHAR(50) NOT NULL,
 ip VARCHAR(50),
 continentCode VARCHAR(50),
 continentName VARCHAR(50),
 countryCode VARCHAR(50),
 countryName VARCHAR(50),
 isEuMember VARCHAR(50),
 currencyCode VARCHAR(50),
 currencyName VARCHAR(50),
 phonePrefix VARCHAR(50),
 languages1 VARCHAR(50),
 languages2 VARCHAR(50),
 geonameId VARCHAR(50),
 latitude VARCHAR(50),
 longitude VARCHAR(50),
 gmtOffset VARCHAR(50),
 timeZone VARCHAR(50),
 asNumber VARCHAR(50),
 asName VARCHAR(50),
 isp VARCHAR(50),
 linkType VARCHAR(50),
 organization VARCHAR(50),
 isCrawler VARCHAR(50),
 isProxy VARCHAR(50),
 threatLevel VARCHAR(50),
 PRIMARY KEY(site)
) Engine=InnoDB CHARACTER SET=UTF8;


load data local infile '/home/admin1/Desktop/vpnbot/resources/tableFILEovpn.csv'

into table FileOVPN fields terminated  by ';' lines terminated by '\n'
ignore 1 rows
(file_name, login, password, countryName, stateProv, district, city, zip_code)
;


load data local infile '/home/admin1/Desktop/vpnbot/resources/characteristic.csv'

into table Characteristics fields terminated  by ';' lines terminated by '\n'
ignore 1 rows
(file_name, site, ip, continentCode, continentName, countryCode, countryName, isEuMember, currencyCode, currencyName, phonePrefix, languages1, languages2,   latitude, longitude, gmtOffset, timeZone, asNumber, asName, isp, linkType, organization, isCrawler, isProxy, threatLevel);
;
