SET search_path TO modulo2_pgsql;

-- Borramos tablas si existen para empezar desde cero
DROP TABLE IF EXISTS shipping;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS users;

-- 1. Tabla de Clientes
CREATE TABLE customers (
  customer_id VARCHAR(50) PRIMARY KEY, 
  name VARCHAR(100), 
  last_purchase DATE
);

-- 2. Tabla de Inventario
CREATE TABLE inventory (
  product_id VARCHAR(50) PRIMARY KEY, 
  product_name VARCHAR(100), 
  quantity INTEGER CHECK (quantity >= 0)
);

-- 3. Tabla de Órdenes
CREATE TABLE orders (
  order_id VARCHAR(50) PRIMARY KEY, 
  customer_id VARCHAR(50) REFERENCES customers(customer_id), 
  total DECIMAL(10, 2), 
  status VARCHAR(20), 
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Tabla de Envíos
CREATE TABLE shipping (
  shipping_id SERIAL PRIMARY KEY, 
  order_id VARCHAR(50) REFERENCES orders(order_id), 
  address VARCHAR(255), 
  status VARCHAR(20)
);



-- Creacion de Cliente
INSERT INTO customers (customer_id, name) 
VALUES ('C001', 'Juan Pérez');

-- Creacion de producto en el inventario
INSERT INTO inventory (product_id, product_name, quantity) 
VALUES ('P001', 'Laptop Gamer', 1);



DO $$
DECLARE
    -- Definimos variables para almacenar datos durante la ejecución
    v_available_stock INTEGER;
    v_shipping_address VARCHAR(255);
BEGIN
    -- 1. Validar el stock
    -- Obtenemos la cantidad disponible y la guardamos en nuestra variable
    SELECT quantity INTO v_available_stock
    FROM inventory
    WHERE product_id = 'P001';
    
    -- Si no hay stock suficiente, lanzamos un error y detenemos todo
    IF v_available_stock IS NULL OR v_available_stock < 1 THEN
      RAISE EXCEPTION 'Stock insuficiente. Abortando transacción.';
    END IF;

    -- 2. Si hay stock, procedemos a crear la orden
    INSERT INTO orders (order_id, customer_id, total, status)
    VALUES ('O001', 'C001', 100.00, 'Pending');

    -- 3. Actualizamos el stock inmediatamente
    UPDATE inventory
    SET quantity = quantity - 1
    WHERE product_id = 'P001';

    -- 4. Bloque interno de protección
    -- Usamos este BEGIN...EXCEPTION para que un fallo no borre la orden anterior
    BEGIN
        -- 4.1. Intentamos generar el envío
        INSERT INTO shipping (order_id, address, status)
        VALUES ('O001', '123 Main St', 'Pending');

        -- 4.2. Actualizamos la fecha del cliente
        UPDATE customers
        SET last_purchase = CURRENT_DATE
        WHERE customer_id = 'C001';

        -- 4.3. Validación de dirección
        SELECT address INTO v_shipping_address
        FROM shipping
        WHERE order_id = 'O001';
        
        -- Si la dirección es inválida, forzamos un error
        IF v_shipping_address = '' OR v_shipping_address IS NULL THEN
          RAISE EXCEPTION 'Error en dirección de envío';
        END IF;

        RAISE NOTICE 'Envío y actualización de cliente completados.';

    EXCEPTION
        WHEN OTHERS THEN
            -- Si algo falla AQUÍ, solo se revierte el envío y el cliente
            -- La orden y el stock se mantienen porque están fuera de este bloque
            RAISE NOTICE 'Error en envío/cliente: %. Orden e inventario YA fueron procesados.', SQLERRM;
    END;

    RAISE NOTICE 'Transacción finalizada.';
END $$;






