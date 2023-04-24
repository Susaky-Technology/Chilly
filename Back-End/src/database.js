const mysql = require('mysql2');

// Define las variables de entorno
const db_url = process.env.DB_URL;
const db_user = process.env.DB_USER;
const db_passwd= process.env.DB_PASSWD;

const mysqlConnection = mysql.createConnection({
  host: db_url,
  user: db_user,
  database: 'aplicacion',
  password: db_passwd,
  // multipleStatements: true
});
mysqlConnection.connect(function (err) {
  if (err) {
    console.error(err);
    return;
  } else {
    console.log('db is connected');
  }
});
module.exports = mysqlConnection;
