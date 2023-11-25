--
-- Create model Doctor
--
CREATE TABLE `doctors` (
  `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
  `last_name` varchar(100) NOT NULL, 
  `first_name` varchar(100) NOT NULL, 
  `patr_name` varchar(100) NOT NULL, 
  `salary` numeric(8, 2) NOT NULL, 
  `premium` numeric(8, 2) NOT NULL, 
  `user_id` integer NOT NULL UNIQUE
);
--
-- Create model Vacation
--
CREATE TABLE `vacations` (
  `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
  `start_date` date NOT NULL, 
  `end_date` date NOT NULL, 
  `doctor_id` integer NOT NULL
);
--
-- Create model Specialization
--
CREATE TABLE `specializations` (
  `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
  `specialization` varchar(120) NOT NULL
);

CREATE TABLE `specializations_doctors` (
  `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
  `specialization_id` integer NOT NULL, 
  `doctor_id` integer NOT NULL
);
--
-- Create constraint chk_end_gt_start on model vacation
--
ALTER TABLE `vacations` 
  ADD CONSTRAINT `chk_end_gt_start` CHECK (`end_date` > (`start_date`));

ALTER TABLE `doctors` 
  ADD CONSTRAINT `doctors_user_id_480f6e79_fk_auth_user_id` 
    FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
  
ALTER TABLE `vacations` 
  ADD CONSTRAINT `vacations_doctor_id_cb1b35d7_fk_doctors_id` 
      FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`);

ALTER TABLE `specializations_doctors` 
  ADD CONSTRAINT `specializations_doctors_specialization_id_doctor_ba303afa_uniq` 
    UNIQUE (`specialization_id`, `doctor_id`);

ALTER TABLE `specializations_doctors` 
  ADD CONSTRAINT `specializations_doct_specialization_id_c97f939e_fk_specializ` 
    FOREIGN KEY (`specialization_id`) REFERENCES `specializations` (`id`);
    
ALTER TABLE `specializations_doctors` 
  ADD CONSTRAINT `specializations_doctors_doctor_id_0a2a65f6_fk_doctors_id` 
    FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`);
