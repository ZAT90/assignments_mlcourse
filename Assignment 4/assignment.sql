create schema movie_db;

use movie_db;

create table Movies(
MovieId int primary key,
Title varchar(150),
Genre varchar(50),
ReleaseYear int,
Rating decimal(2,1),
BoxOfficeRevenue bigint,
Director varchar(100)
);

insert into Movies values
(1,"Inception","Sci-Fi",2010,8.8,830000000,"Christopher Nolan"),
(2,"Titanic","Romance",1997,7.8,2200000000,"James Cameron"),
(3,"The Godfather","Crime",1972,9.2,134000000,"Francis Ford Coppola"),
(4,"Avatar","Sci-Fi",2009,7.9,2840000000,"James Cameron"),
(5,"Interstellar", "Sci-Fi",2014,8.6,677000000,"Christopher Nolan"),
(6,"Parasite","Thriller",2019,8.6,264000000,"Bong Joon Ho"),
(7,"The Dark Knight","Action",2008,9.0,1000000000,"Christopher Nolan"),
(8,"Schindler's List","Drama",1993,9.0,322000000,"Steven Spielberg"),
(9,"The ShawShank Redemption","Drama",1994,9.3,28300000,"Frank Darabont"),
(10,"Pulp Fiction","Crime",1994,8.9,213000000,"Quentin Tarantino");

-- 1. Retrieve all information about movies directed by Christopher Nolan.

select * from Movies
where Director = "Christopher Nolan";

-- 2. Find all distinct genres in the Movies table.
select distinct Genre from Movies;

-- 3. Display the top 5 highest-rated movies, sorted by their rating in descending order.
select * from Movies 
order by Rating desc
limit 5;

-- 4. List all movies released before the year 2000.
select * from Movies 
where ReleaseYear<2000;

-- 5. Show the total number of movies in each genre.
select Genre,count(*) as MovieCount 
from Movies
group by Genre;

--  6. Find the total revenue of all movies in the Sci-Fi genre.
select Genre,sum(BoxOfficeRevenue) as TotalRevenue
from Movies
where Genre = "Sci-Fi";

-- 7. Retrieve the titles of movies with a rating greater than 8.5 but less than 9.0.
select Title,Rating 
from Movies
where Rating>8.5 and Rating<9.0;

-- 8. Display the names of all movies that have the word 'The' in their title.
select Title,Director
from Movies
where Title like '%The%';

-- 9. Find the movie with the highest box office revenue.
select Title,BoxOfficeRevenue
from Movies
where BoxOfficeRevenue = (select max(BoxOfficeRevenue) from Movies);

-- 10. Retrieve the average rating of all movies released after the year 2000.
select avg(Rating) as average_rating
from Movies
where ReleaseYear>2000;
