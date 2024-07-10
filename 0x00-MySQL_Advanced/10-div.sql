-- Creates a function that divides and returns the first
-- by the second numnber or returns 0 if the second 
-- is equal to 0

DELIMITER $$
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
    RETURN (IF (b = 0, 0, a / b));
END
$$
DELIMITER ;
