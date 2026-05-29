SET search_path TO modulo2_pgsql;

-- Borramos tablas si existen para empezar desde cero


DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS cart CASCADE;
DROP TABLE IF EXISTS cart_products CASCADE;
DROP TABLE IF EXISTS bills CASCADE;

-- 1. Tabla de Productos
CREATE TABLE products (
  product_id SERIAL PRIMARY KEY, 
  name VARCHAR(100), 
  quantity INTEGER CHECK (quantity>=0),
  price INTEGER
);

-- 2. Tabla de Usuarios
CREATE TABLE users (
  user_id SERIAL PRIMARY KEY, 
  user_name VARCHAR(30), 
  user_email VARCHAR(50)
);

-- 3. Tabla del carrito
CREATE TABLE cart (
  cart_id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(user_id)
);

-- 3. Tabla del carrito x producto 
CREATE TABLE cart_products (
  cart_products_id SERIAL PRIMARY KEY,
  cart_id INTEGER REFERENCES cart(cart_id),
  product_id INTEGER REFERENCES products(product_id),
  quantity INTEGER CHECK (quantity > 0),
  total NUMERIC(10,2) CHECK (quantity >= 0)
);


-- 5. Tabla de Facturas
CREATE TABLE bills (
  bill_id SERIAL PRIMARY KEY, 
  cart_id INTEGER REFERENCES cart(cart_id),
  status VARCHAR(10)
);


-- Creacion de productos 
INSERT INTO products ( name,quantity, price) VALUES ('iPhone 17 Pro Max 512GB',2, 1199);
INSERT INTO products ( name,quantity, price) VALUES ('iPhone 17 256GB',1, 1099);
INSERT INTO products ( name,quantity, price) VALUES ('iPhone 17 Air 128GB',10, 999);
INSERT INTO products ( name,quantity, price) VALUES ('iPhone 16 Pro Max 256GB',7, 1099);

-- Creacion de usuarios
INSERT INTO users(user_name, user_email) VALUES ('Leonardo Cruz', 'leonardo@gmail.com');
INSERT INTO users(user_name, user_email) VALUES ('Sonia Viquez', 'sonia@gmail.com');
INSERT INTO users(user_name, user_email) VALUES ('Edgar Perez', 'edgar@gmail.com');

--select * from products;
--select * from users;
--select * from cart;
--select * from cart_products;


DO $$
DECLARE
	v_available_stock INTEGER;
	v_user_id INTEGER;
	v_cart_id INTEGER;
	i_product RECORD;

BEGIN
	BEGIN
		-- Asignamos el ID del usuario que queremos probar
		v_user_id = 1;
		-- Confirmar que el usuario existe en la DB
		IF NOT EXISTS(SELECT 1 from users where user_id = v_user_id) --Select 1, es una forma común de verificar si hay al menos una fila que cumple con cierta condición en una consulta SQL
			THEN RAISE EXCEPTION 'El usuario no existe';
		END IF;

		-- Insertar la factura con el usuario relacionado 
		INSERT INTO cart(user_id) VALUES (v_user_id)
		RETURNING cart_id INTO v_cart_id; -- Se guarda el ID que se insertó 
		
		-- Creacion de una lista de productos para el carrito 
		INSERT INTO cart_products (cart_id, product_id, quantity, total) VALUES (v_cart_id, 1, 2, (select price from products where product_id =1)*2);
		INSERT INTO cart_products (cart_id, product_id, quantity, total) VALUES (v_cart_id, 3, 5, (select price from products where product_id =3)*5);
		INSERT INTO cart_products (cart_id, product_id, quantity, total) VALUES (v_cart_id, 4, 5, (select price from products where product_id =4)*5);

		
		-- Validar cada producto en la factura
		-- A continuacion vamos a ir metiendo cada registro de cart_products en este iterador/variable i_product
		FOR i_product IN
    		SELECT cart_id, product_id, quantity, total
    		FROM cart_products
    		WHERE cart_id = v_cart_id -- Seleccionamos solo los registros relacionados al carrito que creamos antes

			LOOP
				
				--Validar que hay existencias del producto
				SELECT quantity into v_available_stock -- Acá accedemos a la cantidad y la guardamos
				FROM products
				WHERE product_id = i_product.product_id;
	
				-- Acá validamos 
				IF v_available_stock < i_product.quantity
					THEN RAISE EXCEPTION 'Stock insuficiente para el producto: ID: %, Nombre: %', i_product.product_id,(select name from products where product_id = i_product.product_id);
				END IF;

				-- Reducir el inventario 
				UPDATE products
				SET quantity = quantity - i_product.quantity
				WHERE product_id = i_product.product_id;

			END LOOP;
			
				-- Si todo lo anterior es correcto entonces creamos la factua con los datos del carrito y la lista de productos
				INSERT INTO bills(cart_id, status) VALUES (v_cart_id,'Delivered');

			-- Confirmar la transaccion
			RAISE NOTICE 'Compra realizada con éxito.';
			
	EXCEPTION
		WHEN OTHERS THEN
		--En caso de error, revertir los cambios
		RAISE EXCEPTION 'Error en la transacción: %', SQLERRM;
		RAISE;
	END;
	
END $$;
	
select 
	b.bill_id,
	c.cart_id,
	u.user_name,
	p.name,
	cp.quantity as "cantidad comprada",
	b.status,
	p.quantity as "Disponible",
	cp.total
from bills b
join cart c on b.cart_id = c.cart_id
join users u on u.user_id = c.user_id
join cart_products cp on c.cart_id = cp.cart_id
join products p on p.product_id = cp.product_id;


--select * from products order by product_id;



--Devolucion de una factura 
DO $$

DECLARE
	v_available_stock INTEGER;
	v_bill_id INTEGER;
	v_cart_id INTEGER;
	i_product RECORD;
BEGIN
	BEGIN
		-- Asignamos el ID de la factura que queremos devolver
		v_bill_id = 1; 

		-- Verificar que la factura existe en la base de datos.
		IF NOT EXISTS(SELECT 1 from bills where bill_id = v_bill_id) --Select 1, es una forma común de verificar si hay al menos una fila que cumple con cierta condición en una consulta SQL
			THEN RAISE EXCEPTION 'La factura con el ID#% no existe',v_bill_id;
		END IF;

		--Si la factura existe entonces tomamos el cart_id que tiene asociado
		SELECT cart_id
		INTO v_cart_id
		FROM bills
		WHERE bill_id = v_bill_id;
		
		-- Aumentar el stock de los productos en la cantidad que se registró la compra
		FOR i_product IN
			select 
			p.product_id,
			p.name,
			cp.quantity
			from bills b
			join cart c on b.cart_id = c.cart_id
			join cart_products cp on c.cart_id = cp.cart_id
			join products p on p.product_id = cp.product_id
			where c.cart_id = v_cart_id

			LOOP
				-- Aumentar el inventario 
				UPDATE products
				SET quantity = quantity + i_product.quantity
				WHERE product_id = i_product.product_id;

			END LOOP;
			
				-- Si todo lo anterior es correcto entonces modificamos el estatus de la factua 
				UPDATE bills 
				SET status = 'Returned'
				WHERE bill_id = v_bill_id;

			-- Confirmar la transaccion
			RAISE NOTICE 'Devolución realizada con éxito.';
			
	EXCEPTION
		WHEN OTHERS THEN
		--En caso de error, revertir los cambios
		RAISE EXCEPTION 'Error en la transacción: %', SQLERRM;
	END;
END $$;


select 
	b.bill_id,
	c.cart_id,
	u.user_name,
	p.name,
	cp.quantity as "cantidad comprada",
	b.status,
	p.quantity as "Disponible",
	cp.total
from bills b
join cart c on b.cart_id = c.cart_id
join users u on u.user_id = c.user_id
join cart_products cp on c.cart_id = cp.cart_id
join products p on p.product_id = cp.product_id;


--select * from products order by product_id;



