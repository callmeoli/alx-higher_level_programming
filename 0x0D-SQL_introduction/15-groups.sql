-- Delete entrie from table
SELECT score, count(score) 'number' 
FROM second_table
GROUP BY score
ORDER BY number DESC;

