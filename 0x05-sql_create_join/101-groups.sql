-- Write a script that lists the number of records
-- with the same score in the table second_table of the database hbtn_0c_0
-- in your MySQL server.
SELECT second_table.score
FROM second_table
WHERE second_table.score IN (
  SELECT second_table.score
  FROM second_table
  GROUP BY score
  HAVING COUNT AS `number` > 1
);
