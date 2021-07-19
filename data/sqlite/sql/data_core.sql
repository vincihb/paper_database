PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS `PAPERS`;

CREATE TABLE `PAPERS`{
    `ID` VARCHAR(100) PRIMARY KEY,
    `TITLE` VARCHAR(500) NOT NULL,
    `ABSTRACT` VARCHAR(500) DEFAULT NULL,
    `PUBLISHED_YEAR` INT NOT NULL,
    `JOURNAL` VARCHAR(100) DEFAULT NULL,
    `VOLUME` INT DEFAULT NULL,
    `PAGES` VARCHAR(100) DEFAULT NULL,
    `COVIDENCE` INT DEFAULT NULL,
    `NOTES` VARCHAR(100) DEFAULT NULL
};

DROP TABLE IF EXISTS `PAPER_KEYWORDS`;

CREATE TABLE `PAPER_KEYWORDS`{
    `KEYWORD` VARCHAR(100) NOT NULL,
    `PAPER_ID` VARCHAR(100) NOT NULL,
    UNIQUE(KEYWORD, PAPER_ID),
    FOREIGN KEY(PAPER_ID) REFERENCES PAPERS(ID)
};

DROP TABLE IF EXISTS `AUTHORS`;

CREATE TABLE `AUTHORS`{
    `AUTHOR` VARCHAR(100) NOT NULL,
    `PAPER_ID` VARCHAR(100) NOT NULL,
    UNIQUE(AUTHOR, PAPER_ID),
    FOREIGN KEY(PAPER_ID) REFERENCES PAPERS(ID)
};

DROP TABLE IF EXISTS `TAGS`;

CREATE TABLE `PAPER_KEYWORDS`{
    `SECTOR` VARCHAR(100) NOT NULL,
    `PAPER_ID` VARCHAR(100) NOT NULL,
    UNIQUE(SECTOR, PAPER_ID),
    FOREIGN KEY(PAPER_ID) REFERENCES PAPERS(ID)
};