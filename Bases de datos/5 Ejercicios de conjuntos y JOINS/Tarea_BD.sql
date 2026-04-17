-- Crear tablas
CREATE TABLE Authors (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL
);

CREATE TABLE Books (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Author INTEGER,
    FOREIGN KEY (Author) REFERENCES Authors(ID)
);

CREATE TABLE Customers (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL
);

CREATE TABLE Rents (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    BookID INTEGER NOT NULL,
    CustomerID INTEGER NOT NULL,
    State TEXT NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Books(ID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(ID)
);

-- Insertar datos en Authors
INSERT INTO Authors (ID, Name) VALUES
(1, 'Miguel de Cervantes'),
(2, 'Dante Alighieri'),
(3, 'Takehiko Inoue'),
(4, 'Akira Toriyama'),
(5, 'Walt Disney');

-- Insertar datos en Books
INSERT INTO Books (ID, Name, Author) VALUES
(1, 'Don Quijote', 1),
(2, 'La Divina Comedia', 2),
(3, 'Vagabond 1-3', 3),
(4, 'Dragon Ball 1', 4),
(5, 'The Book of the 5 Rings', NULL);

-- Insertar datos en Customers
INSERT INTO Customers (ID, Name, Email) VALUES
(1, 'John Doe', 'j.doe@email.com'),
(2, 'Jane Doe', 'jane@doe.com'),
(3, 'Luke Skywalker', 'darth.son@email.com');

-- Insertar datos en Rents
INSERT INTO Rents (ID, BookID, CustomerID, State) VALUES
(1, 1, 2, 'Returned'),
(2, 2, 2, 'Returned'),
(3, 1, 1, 'On time'),
(4, 3, 1, 'On time'),
(5, 2, 2, 'Overdue');


SELECT * from Authors;
SELECT * from Books;

-- 1. Obtenga todos los libros y sus autores
SELECT Books.ID, Books.Name, Authors.Name as Author FROM Books LEFT JOIN Authors on Books.Author = Authors.ID;

-- 2. Obtenga todos los libros que no tienen autor
SELECT * FROM Books b WHERE b.Author IS NULL;

-- 3. Obtenga todos los autores que no tienen libros
SELECT Authors.ID , Authors.Name from Authors LEFT JOIN Books on Authors.ID = Books.Author Where Books.ID IS NULL;

-- 4. Obtenga todos los libros que han sido rentados en algún momento
SELECT DISTINCT b.ID, b.Name from Books b INNER JOIN Rents r on b.ID = r.BookID;
--SELECT b.ID, b.Name from Books b LEFT join Rents r on b.ID = r.BookID where r.BookID is not null GROUP by b.ID;

-- 5. Obtenga todos los libros que nunca han sido rentados
--SELECT b.ID, b.Name from Books b FULL OUTER JOIN Rents r on b.ID = r.BookID WHERE b.ID Is not r.BookID;
SELECT b.ID, b.Name from Books b LEFT JOIN Rents r on b.ID = r.BookID WHERE r.ID Is NULL;


-- 6. Obtenga todos los clientes que nunca han rentado un libro
SELECT c.ID, c.Name, c.Email from Customers c LEFT JOIN Rents r on c.ID = r.CustomerID WHERE r.ID is null;

-- 7. Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT b.ID, b.Name from Books b LEFT JOIN Rents r on b.ID = r.BookID WHERE r.State = "Overdue";





-- EJERCICIOS EXTRA DE JOINS 
-- All = {1,2,3,4,5,6,7,8,9,10}
-- Even = {2,4,6,8,10}
-- Odd = {1,3,5,7,9}

-- 1. Analice la operación de conjuntos All - Odd.

-- Acá se restan los elementos de un conjunto con el otro, los elementos del lado izquierdo de la
-- operacion se mantienen, mientras que se eliminan los elementos que coinciden en ambos y los del lado derecho

-- En este caso el resultado de la consulta debería ser {2,4,6,8,10}

-- Context
CREATE TABLE Alll (ID INTEGER PRIMARY KEY AUTOINCREMENT, Number INTEGER NOT NULL);

CREATE TABLE Even (ID INTEGER PRIMARY KEY AUTOINCREMENT, Number INTEGER NOT NULL);

CREATE TABLE Odd (ID INTEGER PRIMARY KEY AUTOINCREMENT, Number INTEGER NOT NULL);

INSERT INTO Alll ( Number) VALUES (1),(2),(3),(4),(5),(6),(7),(8),(9),(10);
INSERT INTO Even ( Number) VALUES (2),(4),(6),(8),(10);
INSERT INTO Odd ( Number) VALUES (1),(3),(5),(7),(9);

SELECT * from Alll;
SELECT * from Even;
SELECT * from Odd;

-- Respuesta: Usaría un left Join
--All - Odd
SELECT a.ID as "All ID", a.Number as "All Number", o.ID as "Odd ID", o.Number as "Odd Number" 
from Alll a left JOIN Odd o on a.Number = o.Number
WHERE o.ID is null;

-- 2. Usando las tablas de Books, Customers y Rents
--  Obtenga el número total de veces que cada cliente ha rentado un libro
--  Ordene de mayor a menor y limite el resultado a los 3 clientes más activos

-- Acá insertamos un valor más para tener mínimo 3 registros en esta consulta
INSERT INTO Rents (ID, BookID, CustomerID, State) VALUES
(6, 5, 3, 'On time');

SELECT 
    c.ID as "Client ID", c.Name as "Cliente",
    count(*) as "Libros rentados"
from 
    Rents r 
JOIN Books b on b.ID = r.BookID
LEFT JOIN Customers c on c.ID = r.CustomerID
GROUP by c.ID, c.Name 
ORDER BY count(*) DESC
LIMIT 3;


-- Genere un SELECT que devuelva lo siguiente:
--  Nombre del cliente
--  Nombre del libro
--  Nombre del autor
--  Estado del alquiler (Rents.State)


SELECT 
    c.Name as "Cliente",
    b.Name as "Libro",
    a.Name as "Autor",
    r.State as "Estado"
from 
    Rents r 
JOIN Books b on b.ID = r.BookID
JOIN Customers c on c.ID = r.CustomerID
LEFT JOIN Authors a on a.ID = b.Author;

SELECT * from Authors;
SELECT * from Books;
SELECT * from Rents;
SELECT * from Customers;