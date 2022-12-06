BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Categorias_productos" (
	"codigo"	INTEGER,
	"categoria"	TEXT,
	PRIMARY KEY("codigo")
);
CREATE TABLE IF NOT EXISTS "Productos" (
	"codigo"	INTEGER,
	"id"	TEXT NOT NULL,
	"marca"	TEXT NOT NULL,
	"stock"	INTEGER NOT NULL,
	"precio"	REAL NOT NULL,
	"categoria"	INTEGER,
	FOREIGN KEY("categoria") REFERENCES "Categorias_productos"("codigo"),
	PRIMARY KEY("codigo" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Pedidos" (
	"codigo"	INTEGER,
	"fecha"	TEXT,
	"usuario"	TEXT,
	"monto_total"	REAL,
	PRIMARY KEY("codigo" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Detalle_pedidos" (
	"producto"	TEXT,
	"precio_unitario"	REAL,
	"id"	INTEGER,
	"codigo_pedido"	INTEGER,
	FOREIGN KEY("codigo_pedido") REFERENCES "Pedidos"("codigo"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Roles" (
	"id"	INTEGER,
	"tipo"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Usuarios" (
	"id"	TEXT UNIQUE,
	"password"	TEXT NOT NULL,
	"fecha_nacimiento"	TEXT,
	"email"	TEXT NOT NULL,
	"telefono"	REAL NOT NULL,
	"domicilio"	TEXT NOT NULL,
	"tipo"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("tipo") REFERENCES "Roles"("id")
);
COMMIT;
