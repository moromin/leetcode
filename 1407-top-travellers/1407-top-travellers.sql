# Write your MySQL query statement below
select
    u.name,
    case
        when r.total is NULL then 0
        else r.total
    end as travelled_distance
from Users as u
left outer join (
    select user_id, sum(distance) as total
    from Rides
    group by user_id
) as r
on u.id = r.user_id
order by travelled_distance desc, u.name asc