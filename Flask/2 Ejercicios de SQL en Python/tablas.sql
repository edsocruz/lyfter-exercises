SET search_path TO lyfter_car_rental;


DROP TABLE IF EXISTS Users cascade;
DROP TABLE IF EXISTS Cars cascade;
DROP TABLE IF EXISTS Users_Cars cascade;

--Tarea 1

Create table Users(
id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
name varchar(30) not null ,
email varchar(35)not null ,
username varchar(20)not null ,
password varchar(20)not null ,
birth_date date not null ,
account_status varchar(10) not null 
);

insert into Users(name, email, username, password, birth_date, account_status) values ('Gilburt Weyland', 'gweyland0@telegraph.co.uk', 'gweyland0', 'aJ6"Ce91MMWA', '3/9/2005', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Imelda Peach', 'ipeach1@simplemachines.org', 'ipeach1', 'rK7%<0)a', '8/7/1996', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Mureil Sothern', 'msothern2@ehow.com', 'msothern2', 'tU2''U`,L5M_,.B', '9/10/1999', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Burg McWhirter', 'bmcwhirter3@examiner.com', 'bmcwhirter3', 'xO7@o|=@rQ?b', '1/1/2002', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Farleigh Punch', 'fpunch4@businessinsider.com', 'fpunch4', 'aH2\a=`jR?l', '8/26/2004', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Christabella Feldmann', 'cfeldmann5@wp.com', 'cfeldmann5', 'sV7`@vsW{DNvKc!', '11/14/2004', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Lauree Paddison', 'lpaddison6@prweb.com', 'lpaddison6', 'zL3?yQF}r{%!Vi3', '1/24/2000', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Niko Cowmeadow', 'ncowmeadow7@npr.org', 'ncowmeadow7', 'kT7\rp3(.d@O/u2', '3/21/2004', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Dyanna Cotterel', 'dcotterel8@jimdo.com', 'dcotterel8', 'nB2|$Cg%HoKz?', '2/26/2002', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Kalila Wilhelmy', 'kwilhelmy9@drupal.org', 'kwilhelmy9', 'qX7.ngpD0Dm', '6/24/1995', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Hewe Darrington', 'hdarringtona@ox.ac.uk', 'hdarringtona', 'wK5%!''}s?~}KJ', '9/7/2001', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Bron Flook', 'bflookb@usatoday.com', 'bflookb', 'sI8$k91d0,?~7tF', '9/23/1998', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Joby Hammersley', 'jhammersleyc@surveymonkey.com', 'jhammersleyc', 'zF2,|_NBp', '2/28/2001', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Garland Clampett', 'gclampettd@globo.com', 'gclampettd', 'hI3?k(Zh|Np"&Y', '12/14/1999', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Vin Biagi', 'vbiagie@independent.co.uk', 'vbiagie', 'kC3$yElnXc5E`', '7/12/2002', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Gardy Einchcombe', 'geinchcombef@java.com', 'geinchcombef', 'qD4#=dl_f', '11/6/2003', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Port Manie', 'pmanieg@mozilla.com', 'pmanieg', 'jJ6+rERn_@', '5/11/2005', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Paulo Manley', 'pmanleyh@ucoz.ru', 'pmanleyh', 'cK2*~_2lp=u@/Vv', '9/24/2003', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Ricki Dorey', 'rdoreyi@bizjournals.com', 'rdoreyi', 'qH6*Wvu2nWwJ', '5/11/2005', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Shanie Conaghy', 'sconaghyj@apache.org', 'sconaghyj', 'kP7{0_zIH,em`''EW', '3/26/1996', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Theo Thurlbeck', 'tthurlbeckk@histats.com', 'tthurlbeckk', 'aW6*nG!3', '2/28/2000', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Alexandro Parfrey', 'aparfreyl@wiley.com', 'aparfreyl', 'sI6&a=iV79_ftmCF', '6/7/1998', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Bobbie Dearsley', 'bdearsleym@qq.com', 'bdearsleym', 'xC3&kZQsbG2>T\', '4/3/2004', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Sherie Gooda', 'sgoodan@acquirethisname.com', 'sgoodan', 'tG9!TPlw~X''R<T', '2/24/1999', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Ebony Roux', 'erouxo@epa.gov', 'erouxo', 'iF8|GSK"*N', '1/23/1996', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Dredi Ruselin', 'druselinp@technorati.com', 'druselinp', 'wA5??MyUCG}75f7', '4/24/2000', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Devinne Flipek', 'dflipekq@virginia.edu', 'dflipekq', 'fQ4=Y{\O)#U5', '6/5/1998', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Arlan Gladding', 'agladdingr@omniture.com', 'agladdingr', 'rM6`?8n~#', '1/6/2000', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Cobbie Cotton', 'ccottons@phoca.cz', 'ccottons', 'rH7~~SU!/dOm', '8/16/1997', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Isidor Figgures', 'ifiggurest@nymag.com', 'ifiggurest', 'pU4=tx2Ts@7pl4', '12/26/2001', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Cristian Bawcock', 'cbawcocku@sbwire.com', 'cbawcocku', 'aO9)_vL{Eo', '11/14/2004', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Marilee Phizackarley', 'mphizackarleyv@xing.com', 'mphizackarleyv', 'gC6"X9sdTW5gA9E', '7/30/1996', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Sherie Tackes', 'stackesw@washingtonpost.com', 'stackesw', 'kJ2!.5FJn*q<\{8', '2/5/1996', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Pryce Mildenhall', 'pmildenhallx@google.fr', 'pmildenhallx', 'pL5|P~rx0Dn', '8/30/2002', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Eudora Mordey', 'emordeyy@umn.edu', 'emordeyy', 'dI0?=E%?@zh=', '12/23/2002', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Viki Richardt', 'vrichardtz@friendfeed.com', 'vrichardtz', 'sY5}gc)*F', '9/13/1998', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Rea Emmanuele', 'remmanuele10@elegantthemes.com', 'remmanuele10', 'aG2%zeF*X)i<`+A', '3/2/2001', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Evangeline Baumert', 'ebaumert11@exblog.jp', 'ebaumert11', 'zC4@PceW"6_sc`W', '9/2/2001', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Cati Bercevelo', 'cbercevelo12@dion.ne.jp', 'cbercevelo12', 'kH5.`+Jisg3{&Z', '8/15/2002', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Shelby Meiklem', 'smeiklem13@goodreads.com', 'smeiklem13', 'kY0%k5GvZWwd4A', '1/16/1998', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Franny Fairholm', 'ffairholm14@sphinn.com', 'ffairholm14', 'nQ4~6%f=GJ5pqmSb', '7/29/2003', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Penny Wikey', 'pwikey15@google.de', 'pwikey15', 'aU0"rhbQWbev', '4/26/1999', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Arte Gedney', 'agedney16@amazon.co.jp', 'agedney16', 'iB5@#c=~', '4/8/2005', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Aili Boylin', 'aboylin17@tiny.cc', 'aboylin17', 'gK2/hc/S\@D>', '2/18/2001', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Ozzie Ryding', 'oryding18@un.org', 'oryding18', 'mE6\R''&(d)cbR6''T', '1/3/2005', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Bradan Pervoe', 'bpervoe19@feedburner.com', 'bpervoe19', 'aO1/S"/&)', '3/14/2004', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Darwin Duberry', 'dduberry1a@time.com', 'dduberry1a', 'mN7!kA>R+E@1~K', '4/3/2001', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Salim Drowsfield', 'sdrowsfield1b@free.fr', 'sdrowsfield1b', 'eU0+N@?w<', '5/4/2000', 'active');
insert into Users(name, email, username, password, birth_date, account_status) values ('Livia Drew-Clifton', 'ldrewclifton1c@slate.com', 'ldrewclifton1c', 'kS3{TzEJ9@wFev', '10/4/1996', 'inactive');
insert into Users(name, email, username, password, birth_date, account_status) values ('Conant Wornum', 'cwornum1d@netscape.com', 'cwornum1d', 'fD2@F%<x%?s', '4/26/2004', 'inactive');


Create table Cars(
id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
brand varchar(10)not null ,
model varchar(10)not null , 
production_year varchar(4)not null ,
status varchar(15) not null 
);

create table Users_Cars(
id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
id_user integer REFERENCES Users(id) not null ,
id_car integer REFERENCES Cars(id) not null ,
rental_date date default NOW() not null ,
return_date date not null ,
rental_status varchar(15) not null 
);

--Tarea 2
--Un script que agregue un usuario nuevo
insert into Users(name, email, username, password, birth_date, account_status) values ('Edso Cruz', 'edso.cruz@gmail.com', 'edscruz', 'sdfsdfeeda', '9/23/1999', 'inactive');

--Un script que agregue un automovil nuevo
insert into Cars(brand, model, production_year, status) values ('Ford', 'Raptor', '2024', 'rented');
insert into Cars(brand, model, production_year, status) values ('RAM', 'RHO', '2026', 'available');
insert into Cars(brand, model, production_year, status) values ('Fiat', '500e', '2026', 'maintenance');
insert into Cars(brand, model, production_year, status) values ('Dodge', 'Durango', '2025', 'unavailable');

select * from Users;
select * from Cars;
select * from Users_Cars;


--Un script que cambie el estado de un usuario
update Users set account_status = 'active' where id = 51;

--Un script que cambie el estado de un automovil
update Cars set status = 'available' where id = 4;

--Un script que genere un alquiler nuevo con los datos de un usuario y un automovil
DO $$
declare
	--variables
	v_user_id INTEGER;
	v_user_status varchar;
	v_car_id INTEGER;
	v_car_status varchar;
	v_return_date date;
	v_rental_id INTEGER;

begin
	begin
		v_user_id = 51; -- el usuario que acabamos de modificar
		v_car_id = 4; -- el carro que acabamos de modificar
		v_return_date = '7/10/2026';
		
		IF not exists(select 1 from Users u where u.id = v_user_id) then raise exception 'El usuario con el id(%) no existe', v_user_id;
		END IF;
		IF not exists(select 1 from Cars c where c.id = v_car_id) then raise exception 'El carro con el id(%) no existe', v_car_id;
		END IF;
		
		-- Si llegamos hasta acá quiere decir que el carro y el usuario existen
		select account_status into v_user_status from Users u where u.id = v_user_id;
		select status into v_car_status from Cars c where c.id = v_car_id;
		
		-- Ahora debemos validar que se encuentran disponibles para hacer el alquiler del carro 
		IF not v_user_status = 'active' then raise exception 'El usuario con el id(%) esta inactivo o moroso', v_user_id; -- acá v_user_status es un boolean 
		END IF;
		if not v_car_status = 'available' then raise 'El carro con el id(%) no esta disponible para ser alquilado', v_car_id;
		END IF;
		
		-- Si el usuario  y el carro existen y estan disponibles, entonces creamos el registro de la renta
		insert into Users_Cars(id_user, id_car, return_date, rental_status) values (v_user_id, v_car_id, v_return_date, 'active')
		returning id into v_rental_id;
		-- modificamos el status del carro
		update Cars c set status = 'rented' where c.id = v_car_id;
	
	EXCEPTION
		WHEN OTHERS THEN
		--En caso de error, revertir los cambios
		RAISE EXCEPTION 'Error en la transacción: %', SQLERRM;
	END;
END $$;


--Un script que confirme la devolución del auto al completar el alquiler, 
--colocando el auto como disponible y completando el estado del alquiler

DO $$ 
declare
	--variables
	v_rental_id INTEGER;
	v_car_id INTEGER;

begin
	v_rental_id = 1; -- Asignamos el id del alquiler que queremos finalizar
	
	-- Devolver un carro implica:
	--	cambiar el status del carro a maintenance (maintenance/unavailable -> available -> rented)
	select id_car into v_car_id from Users_Cars uc where uc.id = v_rental_id; --obtenemos el id del carro asociado al alquiler
	update Cars c set status = 'maintenance' where c.id = v_car_id;
	--	cambiar el status de la renta a completada
	update Users_Cars set rental_status = 'completed' where id = v_rental_id;
end $$;



--Un script que deshabilite un automovil del alquiler
DO $$
declare
	--variables
	v_car_id INTEGER;
	v_car_status varchar;

begin
	v_car_id = 3; -- el carro que acabamos de modificar

	IF not exists(select 1 from Cars c where c.id = v_car_id) then raise exception 'El carro con el id(%) no existe', v_car_id;
	END IF;
	
	update Cars c set status = 'unavailable' where c.id = v_car_id;
END $$;

--Un script que obtenga todos los automoviles alquilados, y otro que obtenga todos los disponibles.
select * from Cars c where status = 'available';
select * from Cars c where status = 'rented';
select * from Cars c where status = 'maintenance';


select * from lyfter_car_rental.Users where id = 48;
select * from lyfter_car_rental.Cars;
select * from Users_Cars;

select * from lyfter_car_rental.users where id = 100;
delete from lyfter_car_rental.Users where id = 49;





