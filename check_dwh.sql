select
	*
from
	s_news
join h_news
		using(sk_news_id)
join l_date_news ldn
		using(sk_news_id)
join h_date hd
		using(date_id)
join s_date
		using(date_id)
join l_news_publisher lnp
		using(sk_news_id)
join h_publisher
		using(publisher_id)
join s_publisher sp
		using(publisher_id)