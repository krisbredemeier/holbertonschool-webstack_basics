-- Write a script that lists all records of the table second_table
-- of the database hbtn_0c_0 in your MySQL server.
SELECT second_table.score, second_table.name
FROM second_table
WHERE second_table.name IS NOT NULL
ORDER BY second_table.score
DESC;
