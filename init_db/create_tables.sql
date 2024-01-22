DROP TABLE IF EXISTS game_details;
DROP TABLE IF EXISTS access;

ALTER TABLE game_details DROP FOREIGN KEY game_details_ibfk_1;
ALTER TABLE game_details DROP FOREIGN KEY game_details_ibfk_2;

DROP TABLE IF EXISTS game;

DROP TABLE IF EXISTS set_words;
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(80) NOT NULL,
    email VARCHAR(80) NOT NULL,
    login VARCHAR(80) NOT NULL,
    password VARCHAR(80) NOT NULL,
    creat_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS access(
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT,
    creat_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS set_words(
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT,
    name VARCHAR(255) NOT NULL,
    value TEXT NOT NULL,
    creat_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS game(
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT,
    word_id INT NOT NULL,
    creat_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE,
    FOREIGN KEY (word_id)
        REFERENCES set_words(id)
        ON DELETE CASCADE
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS game_details(
    game_id INT NOT NULL,
    user_id INT NOT NULL,
    line INT,
    hits INT,
    miss INT,
    time BIGINT,
    FOREIGN KEY (game_id)
        REFERENCES game(id)
        ON DELETE CASCADE,
    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
) ENGINE=INNODB;