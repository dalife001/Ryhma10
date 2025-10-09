CREATE TABLE `country` (

    `iso_country` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_uca1400_ai_ci',

    `name` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_uca1400_ai_ci',

    `continent` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_uca1400_ai_ci',

    `wikipedia_link` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_uca1400_ai_ci',

    `keywords` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_uca1400_ai_ci',

    PRIMARY KEY (`iso_country`) USING BTREE

)

COLLATE='utf8mb4_uca1400_ai_ci'

ENGINE=InnoDB

;



CREATE TABLE airport

(`id` int(11) NOT NULL,

  `ident` varchar(40) NOT NULL,

  `type` varchar(40) DEFAULT NULL,

  `name` varchar(40) DEFAULT NULL,

  `latitude_deg` double DEFAULT NULL,

  `longitude_deg` double DEFAULT NULL,

  `elevation_ft` int(11) DEFAULT NULL,

  `continent` varchar(40) DEFAULT NULL,

  `iso_country` varchar(40) DEFAULT NULL,

  `iso_region` varchar(40) DEFAULT NULL,

  `municipality` varchar(40) DEFAULT NULL,

  `scheduled_service` varchar(40) DEFAULT NULL,

  `gps_code` varchar(40) DEFAULT NULL,

  `iata_code` varchar(40) DEFAULT NULL,

  `local_code` varchar(40) DEFAULT NULL,

  `home_link` varchar(40) DEFAULT NULL,

  `wikipedia_link` varchar(40) DEFAULT NULL,

  `keywords` varchar(40) DEFAULT NULL,

  PRIMARY KEY (`ident`),

  FOREIGN KEY (iso_country) REFERENCES country(iso_country)

);

CREATE TABLE `player` (

    `Name` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_uca1400_ai_ci',

    `Points` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_uca1400_ai_ci',

    `Guessed` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_uca1400_ai_ci',

    `info` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_uca1400_ai_ci',

    `ident` VARCHAR(40) NULL DEFAULT NULL COLLATE 'utf8mb4_uca1400_ai_ci',

    `iso_country` VARCHAR(40) NULL DEFAULT NULL COLLATE 'utf8mb4_uca1400_ai_ci',

    PRIMARY KEY (`Name`) USING BTREE,

    INDEX `ident` (`ident`) USING BTREE,

    INDEX `iso_country` (`iso_country`) USING BTREE,

    CONSTRAINT `player_ibfk_1` FOREIGN KEY (`ident`) REFERENCES `airport` (`ident`) ON UPDATE RESTRICT ON DELETE RESTRICT,

    CONSTRAINT `player_ibfk_2` FOREIGN KEY (`iso_country`) REFERENCES `country` (`iso_country`) ON UPDATE RESTRICT ON DELETE RESTRICT

)

COLLATE='utf8mb4_uca1400_ai_ci'

ENGINE=InnoDB

;
CREATE TABLE `airport_co2` (
  `ident` VARCHAR(10) NOT NULL,
  `co2` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_uca1400_ai_ci',
  `co2_impact` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_uca1400_ai_ci',
  FOREIGN KEY (`ident`) REFERENCES `airport` (`ident`)
)
COLLATE='utf8mb4_uca1400_ai_ci'
ENGINE=InnoDB;
