select prod.name, prov.name
from products as prod
join providers as prov on prod.id_providers = prov.id
where prod.id_categories = 6