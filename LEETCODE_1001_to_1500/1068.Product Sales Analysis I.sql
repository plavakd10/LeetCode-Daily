select product_name, year, price
from Product p
inner join Sales s
on p.product_id = s.product_id