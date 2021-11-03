/*
 * запускать один раз в начале выборов, вместо num_tik вставиь реальные названия ТИК 
 */

insert into mainapp_tik
(num_tik, sum_votes, population,presence,open_uik ,sum_numb_votes_fin,bad_form,perc_final_bul,update_time)
values
('1',0,0,0,0,0,0,0,now()),
('2',0,0,0,0,0,0,0,now()),
('3',0,0,0,0,0,0,0,now()),
('4',0,0,0,0,0,0,0,now()),
('5',0,0,0,0,0,0,0,now()),
('6',0,0,0,0,0,0,0,now()),
('7',0,0,0,0,0,0,0,now()),
('8',0,0,0,0,0,0,0,now()),
('9',0,0,0,0,0,0,0,now()),
('10',0,0,0,0,0,0,0,now());



/*
 * Запускать во время, обозначенное аналитиками
 */


insert into mainapp_tik
(num_tik, sum_votes, population,presence,open_uik ,sum_numb_votes_fin,bad_form,perc_final_bul,update_time)
select num_tik_id, sum_votes, population,cast(sum_votes as float)/cast(population as float) as "presence",
status, sum_numb_votes_fin,bad_form,
cast(sum_numb_votes_fin as float)/cast(sum_votes as float) as "perc_final_bul",now()
from (
	select num_tik_id, sum(sum_votes) as "sum_votes",sum(population) as "population",
	count(status)  as "status",sum(sum_numb_votes_fin) as "sum_numb_votes_fin",sum(bad_form) as "bad_form"
	from mainapp_uik 
	where status = True
	group by num_tik_id
) as t;


