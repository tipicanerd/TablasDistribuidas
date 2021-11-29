###Tabla Clientes (Id, Nombre, ApellidoPaterno, ApellidoMaterno, RFC)
###Tabla Direcciones (Id, Calle, Numero, Colonia, Estado, CP, idCliente)


### ADMIN ###
CREATE TABLE idConstructor(
	number INT(6) ZEROFILL NOT NULL,
	base CHAR(3) NOT NULL
);

#INSERT INTO idConstructor VALUES
#(1,'MOR'), (1,'APA');

PREPARE idGen FROM 'SET @lastid = (SELECT CONCAT(base,number) FROM adminSucursales.idConstructor WHERE base=?)';
PREPARE idUp FROM 'UPDATE adminSucursales.idConstructor SET number= number+1 WHERE base=?';

CREATE TABLE sucursales(
	id INT(6) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(250) NOT NULL
);

#-----

CREATE TABLE clientes(
	id CHAR(9) PRIMARY KEY,
	nombre VARCHAR(250) NOT NULL,
	apellidoPaterno VARCHAR(250),
	apellidoMaterno VARCHAR(250),
	RFC CHAR(13) UNIQUE NOT NULL
);

CREATE TABLE direcciones(
	id_cliente CHAR(9),
	id INT(6) ZEROFILL NOT NULL AUTO_INCREMENT  PRIMARY KEY,
	calle VARCHAR(250),
	numero INT,
	Colonia VARCHAR(250),
	Estado VARCHAR(250),
	CP CHAR(5),
	FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

