DROP TABLE IF EXISTS public.H_news;
CREATE TABLE public.H_news (
	pk_news_id integer NOT NULL UNIQUE,
	sk_news_id serial NOT NULL UNIQUE,
	title varchar NOT NULL,
	CONSTRAINT H_news_pk PRIMARY KEY (pk_news_id)
) WITH (
	OIDS=FALSE
);


DROP TABLE IF EXISTS public.S_news;
CREATE TABLE public.S_news (
	sk_news_id integer NOT NULL,
	link varchar NOT NULL,
	description varchar NOT NULL,
	keyword varchar NOT NULL
) WITH (
	OIDS=FALSE
);


DROP TABLE IF EXISTS public.L_date_news;
CREATE TABLE public.L_date_news (
	sk_news_id integer NOT NULL,
	date_id date NOT NULL,
	pub_time TIME NOT NULL
) WITH (
	OIDS=FALSE
);


DROP TABLE IF EXISTS public.H_date;
CREATE TABLE public.H_date (
	date_id date NOT null UNIQUE
) WITH (
	OIDS=FALSE
);

DROP TABLE IF EXISTS public.S_date;
CREATE TABLE public.S_date
(
	date_id DATE NOT NULL,
	year SMALLINT NOT NULL, -- 2000 to 2070
	month SMALLINT NOT NULL, -- 1 to 12
	day SMALLINT NOT NULL, -- 1 to 31
	quarter SMALLINT NOT NULL, -- 1 to 4
	day_of_week SMALLINT NOT NULL, -- 0 () to 6 ()
	day_of_year SMALLINT NOT NULL, -- 1 to 366
	week_of_year SMALLINT NOT NULL, -- 1 to 53
	CONSTRAINT con_month CHECK (month >= 1 AND month <= 31),
	CONSTRAINT con_day_of_year CHECK (day_of_year >= 1 AND day_of_year <= 366), -- 366 allows for leap years
	CONSTRAINT con_week_of_year CHECK (week_of_year >= 1 AND week_of_year <= 53),
	CONSTRAINT S_date_pk PRIMARY KEY (date_id)
) WITH (
	OIDS = FALSE
);



DROP TABLE IF EXISTS public.L_news_publisher;
CREATE TABLE public.L_news_publisher (
	sk_news_id integer NOT NULL,
	publisher_id integer NOT NULL
) WITH (
	OIDS=FALSE
);


DROP TABLE IF EXISTS public.H_publisher;
CREATE TABLE public.H_publisher (
	publisher_id serial NOT NULL,
	publisher_name varchar NOT NULL,
	CONSTRAINT H_publisher_pk PRIMARY KEY (publisher_id)
) WITH (
	OIDS=FALSE
);


DROP TABLE IF EXISTS public.S_publisher;
CREATE TABLE public.S_publisher (
	publisher_id integer NOT NULL,
	country varchar NOT NULL,
	language varchar NOT NULL,
	CONSTRAINT S_publisher_pk PRIMARY KEY (publisher_id)
) WITH (
	OIDS=FALSE
);




ALTER TABLE s_news ADD CONSTRAINT s_news_fk0 FOREIGN KEY (sk_news_id) REFERENCES H_news(sk_news_id);

ALTER TABLE L_date_news ADD CONSTRAINT L_date_news_fk0 FOREIGN KEY (sk_news_id) REFERENCES H_news(sk_news_id);
ALTER TABLE L_date_news ADD CONSTRAINT L_date_news_fk1 FOREIGN KEY (date_id) REFERENCES H_date(date_id);


ALTER TABLE S_date ADD CONSTRAINT S_date_fk0 FOREIGN KEY (date_id) REFERENCES H_date(date_id);

ALTER TABLE L_news_publisher ADD CONSTRAINT L_news_publisher_fk0 FOREIGN KEY (sk_news_id) REFERENCES H_news(sk_news_id);
ALTER TABLE L_news_publisher ADD CONSTRAINT L_news_publisher_fk1 FOREIGN KEY (publisher_id) REFERENCES H_publisher(publisher_id);


ALTER TABLE S_publisher ADD CONSTRAINT S_publisher_fk0 FOREIGN KEY (publisher_id) REFERENCES H_publisher(publisher_id);