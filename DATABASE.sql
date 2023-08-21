use evaluacionvaleria;
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_de_control VARCHAR(20) NOT NULL,
    usuario VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    municipio VARCHAR(100)
);
select * from usuarios;
INSERT INTO usuarios (numero_de_control, usuario, password, email, nombre, telefono, municipio)
VALUES
    (1220100603, 'ANZO001', 'Valeria', 'anzo.maric@gmail.com', 'ANZO AVALOS MARIA CITLALLI', '4181234567', 'Dolores Hidalgo'),
    (1219100524, 'ARRE001', 'Valeria', 'arredondo.daniel@gmail.com', 'ARREDONDO GONZALEZ DANIEL ENRIQUE', '4182345678', 'Dolores Hidalgo'),
    (1220100317, 'DUAR001', 'Valeria', 'duarte.daniel@gmail.com', 'DUARTE VELAZQUEZ DANIEL', '4183456789', 'San Felipe'),
    (1220100629, 'GUTI001', 'Valeria', 'gutierrez.valeria@gmail.com', 'GUTIERREZ MARTINEZ VALERIA IVONNE', '4184567890', 'Dolores Hidalgo'),
    (1220100632, 'LUNA001', 'Valeria', 'luna.angel@gmail.com', 'LUNA CANTERO ANGEL IVAN', '4185678901', 'San Miguel de Allende'),
    (1220100209, 'MART001', 'Valeria', 'martinez.guadalupe@gmail.com', 'MARTINEZ RAMIREZ GUADALUPE MONSERRAT', '4186789012', 'San Miguel de Allende'),
    (1220100053, 'REYE001', 'Valeria', 'reyes.salvador@gmail.com', 'REYES MORALES SALVADOR', '4187890123', 'Dolores Hidalgo'),
    (1220100597, 'SALA001', 'Valeria', 'salazar.maria@gmail.com', 'SALAZAR LEON MARIA GUADALUPE', '4188901234', 'San Felipe'),
    (1220100596, 'TADE001', 'Valeria', 'tadeo.alejandro@gmail.com', 'TADEO MARTINEZ ALEJANDRO', '4189012345', 'Dolores Hidalgo'),
    (1220100075, 'TORR001', 'Valeria', 'torres.jose@gmail.com', 'TORRES GARCIA JOSE ROGELIO', '4180123456', 'Dolores Hidalgo'),
    (1220100595, 'TRAN001', 'Valeria', 'tranqueño.oscar@gmail.com', 'TRANQUEÑO HERNANDEZ OSCAR ARMANDO', '4181234567', 'Dolores Hidalgo');