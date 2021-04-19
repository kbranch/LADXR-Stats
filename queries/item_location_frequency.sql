select printf('%s: %s - %s', location.name, location.area, location.description) as 'location'
       ,item.name
	   ,sum(case when item.locationId = location.id then 1 else 0 end) as 'count'
from item
join location
  on location.name = '0x2A3'
group by location.name
        ,location.area
		,location.description
		,item.name
order by count, item.name