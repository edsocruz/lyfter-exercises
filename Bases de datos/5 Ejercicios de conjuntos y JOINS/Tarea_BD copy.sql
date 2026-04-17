-- All = {1,2,3,4,5,6,7,8,9,10}
-- Even = {2,4,6,8,10}
-- Odd = {1,3,5,7,9}

CREATE TABLE Alll (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Number INTEGER NOT NULL
);

CREATE TABLE Even (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Number INTEGER NOT NULL
);

CREATE TABLE Odd (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Number INTEGER NOT NULL
);

INSERT INTO Alll ( Number) VALUES (1),(2),(3),(4),(5),(6),(7),(8),(9),(10);
INSERT INTO Even ( Number) VALUES (2),(4),(6),(8),(10);
INSERT INTO Odd ( Number) VALUES (1),(3),(5),(7),(9);

SELECT * from Alll;
SELECT * from Even;
SELECT * from Odd;
SELECT a.ID, a.Number from Alll a;

--All - Odd
SELECT a.ID as "All ID", a.Number as "All Number", o.ID as "Odd ID", o.Number as "Odd Number" 
from Alll a left JOIN Odd o on a.Number = o.Number
WHERE o.ID is null;







-- EJERCICIOS EXTRA DE JOINS 
-- All = {1,2,3,4,5,6,7,8,9,10}
-- Even = {2,4,6,8,10}
-- Odd = {1,3,5,7,9}

-- 1.1 Analice la operación de conjuntos All - Odd.

-- Acá se restan los elementos de un conjunto con el otro, los elementos del lado izquierdo de la
-- operacion se mantienen, mientras que se eliminan los elementos que coinciden en ambos y los del lado derecho

-- En este caso el resultado de la consulta debería ser {2,4,6,8,10}
