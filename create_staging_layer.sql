drop table if exists News;
create table News (
    id serial primary key,
    title varchar(255),
    link varchar(255),
    keyword varchar(255),
    description text,
    source_id varchar(50),
    country varchar(50),
    language varchar(50),
    pubDate date,
    pubTime time
);

/*
    id serial primary key - Primary data key
    title varchar(255) - title of news
    link varchar(255) - link to news
    keywords varchar(255) - news category
    description text - short description of the news
    source_id varchar(50) - publisher of news
    country varchar(50) - publisher country
    language varchar(50) - language of news
    pubDate date - news publication date
    pubTime time - time of news publishing
*/