BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "usuario_registrado" (
	"nombre_usuario"	TEXT,
	"password"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"direccion"	TEXT,
	PRIMARY KEY("nombre_usuario")
);
CREATE TABLE IF NOT EXISTS "administrador" (
	"usuario"	TEXT,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("usuario")
);
CREATE TABLE IF NOT EXISTS "producto" (
	"marca"	TEXT NOT NULL,
	"descripcion"	TEXT NOT NULL,
	"stock"	INTEGER,
	"precio"	REAL NOT NULL,
	"codigo"	INTEGER NOT NULL,
	PRIMARY KEY("codigo" AUTOINCREMENT)
);
COMMIT;
