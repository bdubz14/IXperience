-- SQL Exercises
-- --------------------
-- Use the nobel database from class to answer the following questions.

-- 1. Select the nobel database.

USE nobel;

-- 2. List the tables.

SHOW TABLES;

-- 3. Select the first ten records from the laureate table.

SELECT *
FROM laureate
LIMIT 10;

-- 4. Find the birth and death dates for Albert Einstein.

SELECT birth_date, death_date
FROM laureate
WHERE name='Albert Einstein';

-- 5. Find the Nobel Laureates who died in 2015 and whose name begins with 'Y'.

SELECT *
FROM laureate
WHERE death_date LIKE '2015%' AND name LIKE 'Y%';

-- 6. Find the last three Nobel Laureates born in 1900.

SELECT *
FROM laureate
WHERE birth_date LIKE '1900%'
ORDER BY birth_date DESC
LIMIT 3;


-- 7. Find the number of Nobel Prizes awarded between 1950 and 1960.

SELECT COUNT(*)
FROM prize
WHERE year >= 1950 AND year < 1960;

-- 8. Find the number of Nobel Prizes awarded in each year.

SELECT year, COUNT(*)
FROM prize
GROUP BY year;

-- 9. In which year was the greatest number of Nobel Prizes awarded?

SELECT year
FROM prize
GROUP BY year
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 10. What is the average number of Nobel Prizes awarded per year? Do we know how to do this yet?

SELECT MAX(id) / (MAX(year) - MIN(year) + 1)
FROM prize;

SELECT AVG(total_year)
FROM (SELECT COUNT(year) AS total_year
	  FROM prize
	  GROUP BY year) AS T1;

-- 11. In which years were more than fifteen Nobel Prizes awarded?

SELECT year
FROM prize
GROUP BY year
HAVING COUNT(*) > 15;

-- 12. Who is the Nobel Laureate with the shortest name?

SELECT name
FROM laureate
ORDER BY LENGTH(name)
LIMIT 1;

-- 13. Which Nobel Laureate had the longest life? You might need to use IFNULL().

SELECT name, TIMESTAMPDIFF(year, IFNULL(birth_date, CURDATE()), IFNULL(death_date, 0)) as age
FROM laureate
ORDER BY age DESC
LIMIT 1;

-- 14. Which year has the most women Nobel Laureates?

SELECT year, sex, COUNT(sex) AS sex_count
FROM laureate a
JOIN prize b ON a.id = b.laureate_id WHERE sex = 'F'
GROUP BY year, sex
ORDER BY sex_count DESC
LIMIT 1;


-- 15. Which category has the most women Nobel Laureates?

SELECT category, sex, COUNT(*)
FROM laureate 
JOIN prize ON laureate.id = prize.laureate_id WHERE sex = 'F'
GROUP BY category
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 16. What is the average number of Nobel Prizes awarded per year?

SELECT AVG(total_year)
FROM (SELECT COUNT(year) AS total_year
	  FROM prize
	  GROUP BY year) AS T1;
