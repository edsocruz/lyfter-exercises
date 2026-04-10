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

-- Obtenga todos los libros y sus autores
SELECT Books.ID, Books.Name, Authors.Name as Author FROM Books LEFT JOIN Authors on Books.Author = Authors.ID;

-- Obtenga todos los libros que no tienen autor
SELECT * FROM Books b WHERE b.Author IS NULL;

-- Obtenga todos los autores que no tienen libros
SELECT Authors.ID , Authors.Name from Authors LEFT JOIN Books on Authors.ID = Books.Author Where Books.ID IS NULL;

-- Obtenga todos los libros que han sido rentados en algún momento
SELECT DISTINCT b.ID, b.Name from Books b INNER JOIN Rents r on b.ID = r.BookID;
--SELECT b.ID, b.Name from Books b LEFT join Rents r on b.ID = r.BookID where r.BookID is not null GROUP by b.ID;

-- Obtenga todos los libros que nunca han sido rentados
SELECT b.ID, b.Name from Books b FULL OUTER JOIN Rents r on b.ID = r.BookID WHERE b.ID Is not r.BookID;

-- Obtenga todos los clientes que nunca han rentado un libro
SELECT c.ID, c.Name, c.Email from Customers c LEFT JOIN Rents r on c.ID = r.CustomerID WHERE r.ID is null;

-- Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT b.ID, b.Name from Books b LEFT JOIN Rents r on b.ID = r.BookID WHERE r.State = "Overdue";
