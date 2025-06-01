select p.product_id, product_name
from Product p
left join Sales s
on p.product_id = s.product_id
group by p.product_id
having min(sale_date)>= CAST('2019-01-01' as date) and max(sale_date)<= cast('2019-03-31' as date)