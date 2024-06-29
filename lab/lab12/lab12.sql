.read data.sql


CREATE TABLE bluedog AS
  SELECT color,pet from students where color='blue' and pet = 'dog' ;

CREATE TABLE bluedog_songs AS
  SELECT color,pet ,song from students where color='blue' and pet = 'dog' ;


CREATE TABLE smallest_int AS
  SELECT time ,smallest  from students where smallest >2 order  by sm limit 20  ;


CREATE TABLE matchmaker AS
  SELECT first.pet,first.song,first.color,second,color from students as first ,students as second
  where first.time<second.time and first.pet =second.pet and first.song = second.song  ;


CREATE TABLE sevens AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

