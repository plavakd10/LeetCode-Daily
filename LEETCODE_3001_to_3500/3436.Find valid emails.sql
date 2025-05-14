select user_id, email
from Users
where length(email)-length(replace(email,'@','')) = 1
and email like '%.com' 
and email REGEXP '^[A-Za-z0-9_]+@'
and email REGEXP '@[A-Za-z]+\\.com$'
order by user_id