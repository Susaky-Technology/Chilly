CREATE DATABASE aplicacion;
USE aplicacion;

CREATE TABLE productos(
    id INTEGER(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(30),
    cantidad INTEGER(11),
    precio FLOAT,
    valor_total FLOAT,
    foto_producto BLOB)
ENGINE= 'InnoDB' DEFAULT CHAR SET= latin1;

CREATE TABLE clientes(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombres VARCHAR(20) NOT NULL,
    apellidos VARCHAR(20) NOT NULL,
    cedula INT NOT NULL,
    correo VARCHAR(50) NOT NULL,
    direccion VARCHAR(20)NOT NULL,
    telefono INT NOT NULL)
ENGINE= 'InnoDB' DEFAULT CHAR SET= latin1;

CREATE TABLE trabajadores(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombres VARCHAR(20) ,
    apellidos VARCHAR(20) ,
    cedula VARCHAR(20),
    correo VARCHAR(50) ,
    direccion VARCHAR(20),
    telefono INT ,
    area VARCHAR(20) ,
    foto_trabajador BLOB)
ENGINE= 'InnoDB' DEFAULT CHAR SET= latin1;

CREATE TABLE factura(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cliente VARCHAR(20) NOT NULL,
    fecha INT,
    ciudad VARCHAR(20) NOT NULL,
    compras BLOB,
    subtotal FLOAT,
    descuento FLOAT,
    iva FLOAT,
    total FLOAT)
ENGINE= 'InnoDB' DEFAULT CHAR SET= latin1;
