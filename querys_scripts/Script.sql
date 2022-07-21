select count(g.id),g.name  from public."groups" g, public."statistic_profiles" s
where g.id = s.group_id and g.id <> 5
group by g."name"


select t.id, t.name from public.trainings t



select (select count(spt.statistic_profile_id) from public.statistic_profile_trainings spt
	where spt.created_at  between '2022-02-01 00:00:00' and '2022-03-01 00:00:00') as "Fevereiro 2022"
	
select sp.id, sp.group_id, g2."name", t."name"  from public.trainings t  ,public."groups" g2 ,public.statistic_profiles sp
	inner join public.statistic_profile_trainings spt on
	sp.id = spt.statistic_profile_id and spt.training_id = 24
	inner join public."groups" g on
	sp.group_id = g.id
	where spt.created_at  between '2022-02-01 00:00:00' and '2022-03-02 00:00:00'
	and g2.id = sp.group_id
	


select count(F.group_id), F.name from (select sp.id, sp.group_id, g2.name  from public.groups g2 ,public.statistic_profiles sp
	left join public.statistic_profile_trainings spt on
	sp.id = spt.statistic_profile_id
	where spt.created_at >= '2022-06-30 20:00:00' and spt.created_at < '2022-07-01 00:00:00'
	and g2.id = sp.group_id) as F
	group by F.name
	


	select spt from public.statistic_profile_trainings spt
	where spt.created_at >= '2022-06-29 00:00:00' and spt.created_at < '2022-07-01 00:00:00'
	

select count(u.id), g."name"  from public.users u
	inner join public.statistic_profiles sp on
	u.id = sp.user_id
	inner join public.statistic_profile_trainings spt on
	sp.id = spt.statistic_profile_id
	inner join public.trainings t on
	t.id = spt.training_id 
	inner join public."groups" g on
	sp.group_id = g.id 
	where spt.updated_at between '2022-06-30 20:00:00' and '2022-07-01 20:00:00'
	group by g."name"
	
	
select count(*), g.name from public.statistic_profiles sp 
	inner join public.reservations r on
	r.statistic_profile_id = sp.id
	inner join public.slots_reservations sr on
	sr.reservation_id = r.id 
	inner join public.slots s on
	sr.slot_id = s.id
	inner join public."groups" g on
	g.id = sp.group_id
	inner join public.machines m on
	m.id = r.reservable_id 
	where r.reservable_type ='Machine' and r.created_at > '2022-01-01 08:00:00' and m.id = 11
	group by g.name
	
	
	
	
	

	
	
	
	
