BEGIN;
--
-- Create model Author
--
CREATE TABLE "authors" (
  "author_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "last_name" varchar(50) NOT NULL, 
  "first_name" varchar(50) NOT NULL
);

--
-- Create model Book
--
CREATE TABLE "books" (
  "book_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "title" varchar(100) NOT NULL, 
  "author_id" smallint NOT NULL REFERENCES "authors" ("author_id") 
    DEFERRABLE INITIALLY DEFERRED
);

--
-- Create model Publisher
--
CREATE TABLE "publishers" (
  "publisher_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "name" varchar(100) NOT NULL
);

CREATE TABLE "publishers_authors" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "publisher_id" smallint NOT NULL REFERENCES "publishers" ("publisher_id") 
    DEFERRABLE INITIALLY DEFERRED, 
  "author_id" smallint NOT NULL REFERENCES "authors" ("author_id") 
    DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE "publishers_books" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "publisher_id" smallint NOT NULL REFERENCES "publishers" ("publisher_id") 
    DEFERRABLE INITIALLY DEFERRED, 
  "book_id" integer NOT NULL REFERENCES "books" ("book_id") 
    DEFERRABLE INITIALLY DEFERRED
);


CREATE INDEX "books_author_id_c90d3b48" ON "books" ("author_id");
CREATE UNIQUE INDEX "publishers_authors_publisher_id_author_id_6c42d3ca_uniq" ON "publishers_authors" ("publisher_id", "author_id");

CREATE INDEX "publishers_authors_publisher_id_13c72537" ON "publishers_authors" ("publisher_id");
CREATE INDEX "publishers_authors_author_id_5c59c3c2" ON "publishers_authors" ("author_id");
CREATE UNIQUE INDEX "publishers_books_publisher_id_book_id_d2f7d931_uniq" ON "publishers_books" ("publisher_id", "book_id");

CREATE INDEX "publishers_books_publisher_id_9319f5d0" ON "publishers_books" ("publisher_id");
CREATE INDEX "publishers_books_book_id_c37e42a2" ON "publishers_books" ("book_id");

COMMIT;
