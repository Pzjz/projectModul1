CREATE TABLE `pacientes` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`nombre` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`apellido` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`cedula` INT(10) NOT NULL,
	`enfermedad` VARCHAR(100) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`fecha_consulta` DATE NOT NULL,
	`registro_medico` VARCHAR(150) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	PRIMARY KEY (`id`) USING BTREE
)