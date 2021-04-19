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