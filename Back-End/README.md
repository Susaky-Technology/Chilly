# Importante
Para la creacion de la API se han usado los modulos de npm:
 - mysql2
 - morgan
 - nodemon
 - express

# Configuración Basica
En la carpeta `src/` existe un subdirectorio con el nombre `database.js` en el cual se debera configurar tanto el usuario al igual que la IP del servidor, o donde este corriendo el contenedor de Docker
> Se planea integrar todo en un solo contenedor de Docker para eliminar este paso.

```javascript
const mysql = require('mysql2');

const mysqlConnection = mysql.createConnection({
  host: 'localhost', // Direccion IP del servidor
  user: 'root', // Usuario de la base de datos
  database: 'aplicacion', //base de datos
  password: 'root', // Contraseña
  // port: 3306, // En caso de tener otro puerto para MySQL
});
```

# Uso
## Trabajadores (Ejemplo)
```json
{
    "id":1, //Este valor es opcional en caso que se trabaje con un PUT o un POST
    "nombres":"Jorge Alexander",
    "apellidos":"Arguello Gusqui",
    "cedula":1600644353,
    "correo":"jorge.arguello1999@gmail.com",
    "direccion":"Dorado",
    "telefono":989402524,
    "area":"admin", // Admin, Cajero o Bodega.
    "foto_trabajador":null //Aqui se coloca una fotografia
}
```

# Docker 
> Primero debemos crear el contenedor de Docker
```bash
docker run -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 --name chilly_db -d mysql
```

> Segundo podemos entrar a configurar la base de datos
```bash
docker exec -it chilly_db -u root -p
```



# Base de Datos
Para la creación de la base de datos primero tenemos que crear la base de datos, siguiendo estos pasos:

## Base de Datos
```sql
CREATE DATABASE aplicacion;
USE aplicacion;
``` 

## Productos
```sql
CREATE TABLE productos( 
    id INTEGER(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(30), 
    cantidad INTEGER(11), 
    precio FLOAT,
    valor_total FLOAT,
    foto_producto BLOB)
    ENGINE= 'InnoDB' DEFAULT CHAR SET= latin1;
```

```text
+---------------+-------------+------+-----+---------+----------------+
| Field         | Type        | Null | Key | Default | Extra          |
+---------------+-------------+------+-----+---------+----------------+
| id            | int(11)     | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(30) | YES  |     | NULL    |                |
| cantidad      | int(11)     | YES  |     | NULL    |                |
| precio        | float       | YES  |     | NULL    |                |
| valor_total   | float       | YES  |     | NULL    |                |
| foto_producto | blob        | YES  |     | NULL    |                |
+---------------+-------------+------+-----+---------+----------------+
```
## Clientes
```sql
CREATE TABLE clientes( 
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    nombres VARCHAR(20) NOT NULL, 
    apellidos VARCHAR(20) NOT NULL, 
    cedula INT NOT NULL,
    correo VARCHAR(50) NOT NULL,
    direccion VARCHAR(20)NOT NULL,
    telefono INT NOT NULL) 
    ENGINE= 'InnoDB' DEFAULT CHAR SET= latin1;
```

```text
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| nombres   | varchar(20) | NO   |     | NULL    |                |
| apellidos | varchar(20) | NO   |     | NULL    |                |
| cedula    | int(11)     | NO   |     | NULL    |                |
| correo    | varchar(50) | NO   |     | NULL    |                |
| direccion | varchar(20) | NO   |     | NULL    |                |
| telefono  | int(11)     | NO   |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
```

## Trabajadores
```sql
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
```

```text
+-----------------+-------------+------+-----+---------+----------------+
| Field           | Type        | Null | Key | Default | Extra          |
+-----------------+-------------+------+-----+---------+----------------+
| id              | int(11)     | NO   | PRI | NULL    | auto_increment |
| nombres         | varchar(20) | YES  |     | NULL    |                |
| apellidos       | varchar(20) | YES  |     | NULL    |                |
| cedula          | int(11)     | YES  |     | NULL    |                |
| correo          | varchar(50) | YES  |     | NULL    |                |
| direccion       | varchar(20) | YES  |     | NULL    |                |
| telefono        | int(11)     | YES  |     | NULL    |                |
| area            | varchar(20) | YES  |     | NULL    |                |
| foto_trabajador | blob        | YES  |     | NULL    |                |
+-----------------+-------------+------+-----+---------+----------------+
```

## Factura
```sql
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
```

```text
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| cliente   | varchar(20) | NO   |     | NULL    |                |
| fecha     | int(11)     | YES  |     | NULL    |                |
| ciudad    | varchar(20) | YES  |     | NULL    |                |
| compras   | blob        | YES  |     | NULL    |                |
| subtotal  | float       | YES  |     | NULL    |                |
| descuento | float       | YES  |     | NULL    |                |
| iva       | float       | YES  |     | NULL    |                |
| total     | float       | YES  |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
```
