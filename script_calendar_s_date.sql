create or replace procedure load_s_date() as 
$$
truncate s_date;
INSERT INTO public.s_date
(	
	date_id
  , year
  , month
  , day
  , quarter
  , day_of_week
  , day_of_year
  , week_of_year
)
(
  select
    ts::date AS date_id
  , EXTRACT(YEAR FROM ts) AS year
  , EXTRACT(MONTH FROM ts) AS month
  , EXTRACT(DAY FROM ts) AS day
  , EXTRACT(QUARTER FROM ts) AS quarter
  , EXTRACT(DOW FROM ts) AS day_of_week
  , EXTRACT(DOY FROM ts) AS day_of_year
  , EXTRACT(WEEK FROM ts) AS week_of_year 
  FROM (select date_id as ts from h_date) as t  
  ORDER BY date_id ASC
);
$$ language sql;

-- call load_s_date();