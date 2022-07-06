# Write your MySQL query statement below
select
    u.user_id as buyer_id,
    u.join_date, 
    sum(
        case
            when YEAR(o.order_date) = 2019 then 1
            else 0
        end
    ) as orders_in_2019
from Users as u
left outer join Orders as o
on u.user_id = o.buyer_id
group by u.user_id