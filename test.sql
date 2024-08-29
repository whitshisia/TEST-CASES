SELECT field1, 
       COUNT(field2) AS field2_count, 
       SUM(field3) AS field3_sum, 
       AVG(field4) AS field4_avg
FROM table1
INNER JOIN table2 ON table1.id = table2.id
LEFT JOIN table3 ON table1.id = table3.id
WHERE condition = 'value'
GROUP BY field1
ORDER BY field2_count DESC
LIMIT 10;

-- the lines below are the explanations 
/* 
The LIMIT clause should come after the ORDER BY clause, not before the JOIN clauses.

The INNER JOIN and LEFT JOIN should come before the WHERE clause.

The GROUP BY is missing. Since COUNT, SUM, and AVG are used, GROUP BY should be there to specify how the rows should be grouped before applying aggregates, allowing the functions to operate correctly over grouped data.
*/
