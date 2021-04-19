createSmallItemQuery = """
create table if not exists smallitem as 
select *
from item
where 0;
"""

clearSmallItemQuery = """
delete from smallitem;
"""
randomPopulateSmallItemQuery = """
insert into smallitem
select item.*
from (select id
      from rom
      order by random()
	  limit ?) as r
join item
  on item.romId = r.id;
"""
incrementalPopulateSmallItemQuery = """
insert into smallitem
select item.*
from (select id
      from rom
	  limit ? offset ?) as r
join item
  on item.romId = r.id;
"""

itemPointsQuery = """
select location.name,
       location.area,
	   location.description,
	   (select avg(ifnull(itemWeights.value, 0))
		from smallitem
		left join itemWeights
		       on itemWeights.itemName = smallitem.name
		where smallitem.locationId = location.id) as avgPoints
from location
order by avgPoints desc
"""

weightsTableQuery = """
drop table if exists itemWeights;

create table itemWeights(itemName text primary key, value real not null);

insert into itemWeights(itemName, value)
values
"""

getRomCountQuery = """
select count(*)
from rom
"""

itemFrequencyQuery = """
select location
      ,item
	  ,count(item) - 1 as 'count'
from (
select printf('%s: %s - %s', location.name, location.area, location.description) as 'location'
       ,item.name as 'item'
from location
join item
  on item.locationId = location.id
where location.name = '{0}'

union all

select printf('%s: %s - %s', location.name, location.area, location.description) as 'location'
       ,item.name as 'item'
from item
join location
  on location.name = '{0}'
group by item.name
)
group by location
		,item
order by item
"""

getAllLocationNamesQuery = """
select distinct location.name
from location
order by location.area, location.description
"""

getAllItemNamesQuery = """
select distinct item.name
from item
order by item.name
"""

getFullLocationNameQuery = """
select printf('%s: %s - %s', location.name, location.area, location.description)
from location
where location.name = ?
"""