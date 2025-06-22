USE `evolve_scrm`;

INSERT INTO `bill_status` (`status`) VALUES
('Pendiente'),
('Pagada'),
('Cancelada');

INSERT INTO `users` (`name`, `surname`, `email`) VALUES
('John', 'Doe', 'j.doe@gmail.com'),
('Diana', 'Miller', 'd.miller@hotmail.com');

INSERT INTO `users` (`name`, `surname`, `email`, `phone`, `address`) VALUES
('Jane', 'Smith', 'j.smith@hotmail.com', '123-456-7890', '123 Elm St, Springfield'),
('Alice', 'Johnson', 'a.johnson@yahoo.com', '987-654-3210', '456 Oak St, Springfield');

INSERT INTO `users` (`name`, `surname`, `email`, `address`) VALUES
('Bob', 'Brown', 'b.brown@googlemail.com', '789 Pine St, Springfield');

INSERT INTO `users` (`name`, `surname`, `email`, `phone`) VALUES
('Charlie', 'Davis', 'c.davis@gmail.com', '555-123-4567');

INSERT INTO `bills` (`user_id`, `description`, `status_id`, `monto_total`) VALUES
(1, 'Servicio de internet', 1, 59.99),
(1, 'Servicio de internet', 1, 59.99),
(1, 'Servicio de internet', 1, 59.99),
(2, 'Factura de electricidad', 2, 120.50),
(3, 'Pago de agua', 1, 45.00),
(4, 'Suscripción mensual de software', 3, 15.00),
(5, 'Mantenimiento de equipo', 1, 75.00),
(6, 'Compra de suministros de oficina', 2, 30.00);