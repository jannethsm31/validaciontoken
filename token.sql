DROP TABLE IF EXISTS usuarios;

CREATE TABLE IF NOT EXISTS usuarios(
    username VARCHAR(100) NOT NULL PRIMARY KEY,
    password VARCHAR(50) NOT NULL,
    token VARCHAR(130) NOT NULL
    timestamps TIMESTAMPS DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO usuarios (username, password, token) VALUES ('hola@example.com', 'd6e2dbac6191d56db007ca489fb83cff', '7d8d45fc32e6865adb9959ae033c0350')

INSERT INTO usuarios (username, password, token) VALUE ('jjj@example.com', '550167f3ca4205dca4d44a27dc24a3b6', '5c2e3a104b635a8d342f11176ecb3b2a')