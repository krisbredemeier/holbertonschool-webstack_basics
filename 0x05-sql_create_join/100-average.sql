-- Write a script that computes the score average of all records
-- in the table second_table of the database hbtn_0c_0 in your MySQL server.
-- SELECT `second_table.scores`
-- FROM `second_table`
USE `hbtn_0c_0`;
SELECT AVG(second_table.scores);
