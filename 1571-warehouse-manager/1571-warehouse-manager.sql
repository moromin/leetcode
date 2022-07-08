# Write your MySQL query statement below
select
    # *
    w.name as warehouse_name, 
    sum(w.units * p.volume) as volume
from Warehouse as w
join (
    select product_id, Width * Length * Height as volume
    from Products
) as p
on w.product_id = p.product_id
group by w.name;