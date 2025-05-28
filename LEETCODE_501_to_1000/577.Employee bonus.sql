select name, bonus
from Employee e
left join Bonus b
ON e.empId = b.empId
where bonus < 1000 or bonus is null