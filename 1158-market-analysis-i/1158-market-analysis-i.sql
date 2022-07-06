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

# SELECT
#     u.user_id AS buyer_id,
#     join_date, 
#     COUNT(order_date) AS orders_in_2019 
# FROM Users as u
# LEFT JOIN Orders as o
# ON u.user_id = o.buyer_id
# AND YEAR(order_date) = '2019'
# GROUP BY u.user_id
