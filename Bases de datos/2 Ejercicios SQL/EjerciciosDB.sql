-- SQLite

-- PARTE 2

CREATE TABLE metodos_pago(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_monto VARCHAR(15) NOT NULL,
    nombre_banco VARCHAR(20) NOT NULL
    );
ALTER TABLE metodos_pago RENAME tipo_monto TO tipo_metodo;

INSERT INTO metodos_pago (tipo_metodo, nombre_banco) VALUES ('Transferencia','BAC');
INSERT INTO metodos_pago (tipo_metodo, nombre_banco) VALUES ('Transferencia','BN');
INSERT INTO metodos_pago (tipo_metodo, nombre_banco) VALUES ('Transferencia','BCR');
INSERT INTO metodos_pago (tipo_metodo, nombre_banco) VALUES ('Transferencia','BP');
INSERT INTO metodos_pago (tipo_metodo, nombre_banco) VALUES ('Transferencia','Davivienda');

INSERT INTO metodos_pago (tipo_metodo, nombre_banco) VALUES ('Tarjeta Crédito/Débito','BAC');
INSERT INTO metodos_pago (tipo_metodo, nombre_banco) VALUES ('Tarjeta Crédito/Débito','BN');
INSERT INTO metodos_pago (tipo_metodo, nombre_banco) VALUES ('Tarjeta Crédito/Débito','BCR');
INSERT INTO metodos_pago (tipo_metodo, nombre_banco) VALUES ('Tarjeta Crédito/Débito','BP');
INSERT INTO metodos_pago (tipo_metodo, nombre_banco) VALUES ('Tarjeta Crédito/Débito','Davivienda');

SELECT * FROM metodos_pago;

CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_completo VARCHAR(30) NOT NULL,
    correo VARCHAR(40) NOT NULL,
    fecha_ingreso DATE NOT NULL
);
INSERT INTO usuarios (nombre_completo, correo, fecha_ingreso) VALUES ('Selmer Wilderman','SelmerWilderman@gmail.com','2001-05-17');
INSERT INTO usuarios (nombre_completo, correo, fecha_ingreso) VALUES ('Lauren Thiel','LaurenThiel@gmail.com','2016-07-17');
INSERT INTO usuarios (nombre_completo, correo, fecha_ingreso) VALUES ('Vesta Cassin','VestaCassin@gmail.com','2020-08-17');
INSERT INTO usuarios (nombre_completo, correo, fecha_ingreso) VALUES ('Bertram Ankunding','BertramAnkunding@gmail.com','2016-09-17');
INSERT INTO usuarios (nombre_completo, correo, fecha_ingreso) VALUES ('Verlie Heaney','VerlieHeaney@gmail.com','2017-04-17');
INSERT INTO usuarios (nombre_completo, correo, fecha_ingreso) VALUES ('Freddy Collins','FreddyCollins@gmail.com','2021-05-17');
INSERT INTO usuarios (nombre_completo, correo, fecha_ingreso) VALUES ('Samara Balistreri','SamaraBalistreri@gmail.com','2011-05-17');

SELECT * from usuarios ORDER BY fecha_ingreso desc;

CREATE TABLE producto(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo VARCHAR(10) NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    precio INT NOT NULL,
    fecha_ingreso DATE NOT NULL,
    marca VARCHAR(15)
);
INSERT INTO producto (codigo, nombre, precio, fecha_ingreso, marca) VALUES ('CP123','Contorno de ojos' ,10900 , '2025-01-01','MAC');
INSERT INTO producto (codigo, nombre, precio, fecha_ingreso, marca) VALUES ('LB748','Olla arrocera' ,45500 ,'2025-02-01' ,'Oster');
INSERT INTO producto (codigo, nombre, precio, fecha_ingreso, marca) VALUES ('AT748','Limpia parabrisas' , 4900, '2025-03-01','Motul');
INSERT INTO producto (codigo, nombre, precio, fecha_ingreso, marca) VALUES ('MT748','Liquido de frenos' , 7000, '2025-04-01','Repsol');
INSERT INTO producto (codigo, nombre, precio, fecha_ingreso, marca) VALUES ('CC748', 'Sartén Inox', 10000,'2025-05-01' ,'Renaware');
INSERT INTO producto (codigo, nombre, precio, fecha_ingreso, marca) VALUES ('LM748', 'Desinfectante', 4000, '2025-06-01','Clorox');
INSERT INTO producto (codigo, nombre, precio, fecha_ingreso, marca) VALUES ('DC748', 'Vela aromática', 3500, '2025-07-01','Basic Home');
INSERT INTO producto (codigo, nombre, precio, fecha_ingreso, marca) VALUES ('LB001', 'Refrigeradora', 700000, '2026-06-01','Samsung');
INSERT INTO producto (codigo, nombre, precio, fecha_ingreso, marca) VALUES ('LB002', 'Horno empotrable', 450000, '2026-01-01','Xiaomi');


CREATE TABLE carrito(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email VARCHAR(40) NOT NULL
    );

INSERT INTO carrito (user_email) VALUES ('SelmerWilderman@gmail.com');
INSERT INTO carrito (user_email) VALUES ('LaurenThiel@gmail.com');
INSERT INTO carrito (user_email) VALUES ('VestaCassin@gmail.com');
INSERT INTO carrito (user_email) VALUES ('BertramAnkunding@gmail.com');
INSERT INTO carrito (user_email) VALUES ('VerlieHeaney@gmail.com');
INSERT INTO carrito (user_email) VALUES ('FreddyCollins@gmail.com');
INSERT INTO carrito (user_email) VALUES ('SamaraBalistreri@gmail.com');


CREATE TABLE producto_carrito(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    carrito_fk INT  REFERENCES carrito(id),
    producto_fk INT  REFERENCES producto(id)
);

ALTER TABLE producto_carrito add cantidad_productos INT NOT NULL;1

INSERT INTO producto_carrito(carrito_fk, producto_fk,cantidad_productos) VALUES (1,1,5);
INSERT INTO producto_carrito(carrito_fk, producto_fk,cantidad_productos) VALUES (2,2,5);
INSERT INTO producto_carrito(carrito_fk, producto_fk,cantidad_productos) VALUES (3,3,5);
INSERT INTO producto_carrito(carrito_fk, producto_fk,cantidad_productos) VALUES (4,4,5);
INSERT INTO producto_carrito(carrito_fk, producto_fk,cantidad_productos) VALUES (5,5,5);
INSERT INTO producto_carrito(carrito_fk, producto_fk,cantidad_productos) VALUES (6,6,5);
INSERT INTO producto_carrito(carrito_fk, producto_fk,cantidad_productos) VALUES (7,7,5);

SELECT * FROM producto_carrito;


CREATE TABLE productos_facturas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_fk INT REFERENCES producto(id) NOT NULL,
    factura_fk INT REFERENCES factura(id) NOT NULL,
    monto_total INT NOT NULL
);

CREATE TABLE factura(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_factura INT NOT NULL,
    fecha_compra DATE NOT NULL,
    correo_comprador VARCHAR(40) NOT NULL,
    monto_total INT NOT NULL,
    metodos_pago_fk INT REFERENCES metodos_pago(id) NOT NULL
);

INSERT INTO factura(numero_factura, fecha_compra, correo_comprador,monto_total, metodos_pago_fk)
    VALUES (123321, '2011-05-17','SelmerWilderman@gmail.com', 10000, 1);
INSERT INTO factura(numero_factura, fecha_compra, correo_comprador,monto_total, metodos_pago_fk)
    VALUES (123321, '2014-05-17','Seadsfasdrman@gmail.com', 20000, 2);
INSERT INTO factura(numero_factura, fecha_compra, correo_comprador,monto_total, metodos_pago_fk)
    VALUES (123321, '2021-05-17','Selenagomez@gmail.com', 50000, 3);
INSERT INTO factura(numero_factura, fecha_compra, correo_comprador,monto_total, metodos_pago_fk)
    VALUES (123321, '2015-05-17','Jeffrey@gmail.com', 90000, 4);
INSERT INTO factura(numero_factura, fecha_compra, correo_comprador,monto_total, metodos_pago_fk)
    VALUES (123321, '2026-09-23','edso@gmail.com', 900000, 1);
UPDATE factura set numero_factura = 2309 WHERE id = 5;

INSERT INTO productos_facturas (producto_fk, factura_fk, monto_total) VALUES (1,1,10000);
INSERT INTO productos_facturas (producto_fk, factura_fk, monto_total) VALUES (2,2,20000);
INSERT INTO productos_facturas (producto_fk, factura_fk, monto_total) VALUES (3,3,30000);
INSERT INTO productos_facturas (producto_fk, factura_fk, monto_total) VALUES (2,2,20000);
INSERT INTO productos_facturas (producto_fk, factura_fk, monto_total) VALUES (3,3,30000);
INSERT INTO productos_facturas (producto_fk, factura_fk, monto_total) VALUES (3,3,30000);

CREATE TABLE factura_usuario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    factura_fk INT REFERENCES factura(id) NOT NULL,
    usuarios_fk INT REFERENCES usuarios(id) NOT NULL
);

INSERT INTO factura_usuario(factura_fk, usuarios_fk) values (1,5);
INSERT INTO factura_usuario(factura_fk, usuarios_fk) values (2,6);
INSERT INTO factura_usuario(factura_fk, usuarios_fk) values (3,7);
INSERT INTO factura_usuario(factura_fk, usuarios_fk) values (2,6);
INSERT INTO factura_usuario(factura_fk, usuarios_fk) values (3,7);
INSERT INTO factura_usuario(factura_fk, usuarios_fk) values (1,5);
INSERT INTO factura_usuario(factura_fk, usuarios_fk) values (2,6);
INSERT INTO factura_usuario(factura_fk, usuarios_fk) values (1,5);
INSERT INTO factura_usuario(factura_fk, usuarios_fk) values (2,6);

CREATE TABLE resenas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_fk INT REFERENCES producto(id) NOT NULL,
    usuarios_fk INT REFERENCES usuarios(id) NOT NULL,
    comentario VARCHAR(300) not null,
    calificacion INT NOT NULL,
    fecha DATE NOT NULL
);

INSERT INTO resenas(producto_fk, usuarios_fk, comentario, calificacion, fecha) values(1,1,'Excelente',5,'2015-05-17');
INSERT INTO resenas(producto_fk, usuarios_fk, comentario, calificacion, fecha) values(2,2,'Buena relacion calidad precio',4,'2015-06-17');
INSERT INTO resenas(producto_fk, usuarios_fk, comentario, calificacion, fecha) values(3,3,'Me llegó dañado',2,'2015-07-17');



--PARTE 3
ALTER TABLE factura ADD telefono_comprador VARCHAR(15) NOT NULL DEFAULT '+50600000000';
ALTER TABLE factura ADD codigo_vendedor INT NOT NULL DEFAULT 0;

--PARTE 4
SELECT * FROM producto;
SELECT * FROM producto WHERE precio > 50000;
SELECT * FROM productos_facturas WHERE producto_fk = 1;
SELECT COUNT(*),* FROM productos_facturas GROUP BY producto_fk;
SELECT * FROM factura_usuario WHERE usuarios_fk = 7;
SELECT * FROM factura ORDER BY monto_total DESC;
SELECT * from factura where numero_factura = 2309;
