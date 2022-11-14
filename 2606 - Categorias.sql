select prod.id, prod.name
from products as prod
join categories as cat on prod.id_categories = cat.id
where cat.name LIKE 'super%'