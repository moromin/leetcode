# Write your MySQL query statement below
select
    name as warehouse_name, 
    sum(units * Width * Length * Height) as volume
from Warehouse as w
join Products as p
on w.product_id = p.product_id
group by name;