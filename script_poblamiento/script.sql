-- Usar la base de datos (asegúrate de que ya exista)
USE python;

-- Eliminar tablas si ya existen (para evitar conflictos)
DROP TABLE IF EXISTS agenda;
DROP TABLE IF EXISTS contactos;
DROP TABLE IF EXISTS usuarios;

-- Crear tabla Usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(100) NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Crear tabla Contactos
CREATE TABLE contactos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    mensaje VARCHAR(500) NOT NULL,
    fecha_contacto DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Crear tabla Agenda
CREATE TABLE agenda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(255) NOT NULL,
    celular VARCHAR(15) NOT NULL,
    edad INT NOT NULL,
    correo VARCHAR(255) NOT NULL,
    fecha_solicitud DATE NOT NULL,
    fecha_hora_agenda DATETIME NOT NULL,
    tipo_corte VARCHAR(100) NOT NULL
);

-- Insertar usuarios (los solicitados: José, Víctor, Germán y Julián)
INSERT INTO usuarios (nombre, apellido, correo, contraseña) VALUES
('Jose', 'Camargo', 'jose@example.com', 'pass123'),
('Victor', 'Yepes', 'victor@example.com', 'pass123'),
('German', 'Gutierrez', 'german@example.com', 'pass123'),
('Julian', 'Venegas', 'julian@example.com', 'pass123');

-- Insertar mensajes de contacto
INSERT INTO contactos (nombre, correo, mensaje) VALUES
('Carlos Mendoza', 'carlos@example.com', 'Excelente servicio. Me encantó el corte.'),
('Laura Torres', 'laura@example.com', 'El mejor lugar para arreglarse el pelo.'),
('Miguel Sánchez', 'miguel@example.com', 'Profesionales al 100. Recomendado.');

-- Insertar citas agendadas
INSERT INTO agenda (nombre_completo, celular, edad, correo, fecha_solicitud, fecha_hora_agenda, tipo_corte) VALUES
('Santiago Mejía', '3001234567', 29, 'santiagomejia@example.com', '2025-04-05', '2025-04-06 10:00:00', 'Degradado'),
('Andrés Pérez', '3109876543', 34, 'andresperez@example.com', '2025-04-05', '2025-04-06 11:00:00', 'Corte Clásico'),
('Daniel Rojas', '3201122334', 25, 'danielrojas@example.com', '2025-04-05', '2025-04-06 12:00:00', 'Barba estilo militar'),
('María Fernanda', '3159988776', 27, 'mariafernanda@example.com', '2025-04-05', '2025-04-06 14:00:00', 'Corte con tijera');