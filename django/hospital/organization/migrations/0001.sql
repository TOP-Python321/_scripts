BEGIN;
--
-- Create model Department
--
CREATE TABLE "departments" (
"department_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"department" varchar(100) NOT NULL
);
--
-- Create model Sponsor
--
CREATE TABLE "sponsors" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"sponsor" varchar(250) NOT NULL
);
--
-- Create model Wards
--
CREATE TABLE "wards" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"ward" varchar(10) NOT NULL, 
"department_id" integer NOT NULL REFERENCES "departments" ("department_id") 
  DEFERRABLE INITIALLY DEFERRED
);
--
-- Create model Donation
--
CREATE TABLE "donations" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"amount" decimal NOT NULL, 
"date" date NOT NULL, 
"department_id" integer NOT NULL REFERENCES "departments" ("department_id") 
  DEFERRABLE INITIALLY DEFERRED, 
"sponsor_id" integer NOT NULL REFERENCES "sponsors" ("id") 
  DEFERRABLE INITIALLY DEFERRED
);
--
-- Add field sponsors to department
--
CREATE TABLE "new__departments" (
  "department_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "department" varchar(100) NOT NULL
);

INSERT INTO "new__departments" (
  "department_id", "department"
) SELECT "department_id", "department" FROM "departments";

DROP TABLE "departments";

ALTER TABLE "new__departments" RENAME TO "departments";

CREATE INDEX "wards_department_id_41a5498f" ON "wards" ("department_id");
CREATE INDEX "donations_department_id_d0dd379b" ON "donations" ("department_id");
CREATE INDEX "donations_sponsor_id_5f266113" ON "donations" ("sponsor_id");

COMMIT;
