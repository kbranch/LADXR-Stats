drop table if exists fantasyPoints;

create table fantasyPoints(itemName text primary key, value real not null);

insert into fantasyPoints(itemName, value)
values
("SHIELD",0.5),
("SWORD",3),
("TOADSTOOL",2),
("MAGIC_POWDER",1),
("MAX_POWDER_UPGRADE",1),
("SHOVEL",2),
("BOMB",1.25),
("MAX_BOMBS_UPGRADE",2),
("BOW",3),
("MAX_ARROWS_UPGRADE",1),
("FEATHER",5),
("POWER_BRACELET",3),
("PEGASUS_BOOTS",5),
("FLIPPERS",4),
("HOOKSHOT",3),
("MAGIC_ROD",3),
("RED_TUNIC",-2),
("BLUE_TUNIC",3),
("OCARINA",2),
("SONG1",2),
("SONG2",3),
("SONG3",-1),
("BOWWOW",2),
("BOOMERANG",2),
("SEASHELL",1),
("TAIL_KEY",3),
("ANGLER_KEY",3),
("FACE_KEY",3),
("BIRD_KEY",3),
("SLIME_KEY",3),
("GOLD_LEAF",1),
("MEDICINE",1),
("HEART_PIECE",1),
("RUPEES_20",-1),
("RUPEES_50",0.01),
("RUPEES_100",1),
("RUPEES_200",1),
("SINGLE_ARROW",-5),
("ARROWS_10",0),
("GEL",-3),
("MESSAGE",-10),
("KEY1",1),
("KEY2",1),
("KEY3",1),
("KEY4",1),
("KEY5",1),
("KEY6",1),
("KEY7",1),
("KEY8",1),
("KEY9",1),
("NIGHTMARE_KEY1",2),
("NIGHTMARE_KEY2",2),
("NIGHTMARE_KEY3",2),
("NIGHTMARE_KEY4",2),
("NIGHTMARE_KEY5",2),
("NIGHTMARE_KEY6",2),
("NIGHTMARE_KEY7",2),
("NIGHTMARE_KEY8",2),
("NIGHTMARE_KEY9",2),
("STONE_BEAK1",0.5),
("STONE_BEAK2",0.5),
("STONE_BEAK3",0.5),
("STONE_BEAK4",0.5),
("STONE_BEAK5",0.5),
("STONE_BEAK6",0.5),
("STONE_BEAK7",0.5),
("STONE_BEAK8",0.5),
("STONE_BEAK9",0.5),
("COMPASS1",-1),
("COMPASS2",-1),
("COMPASS3",-1),
("COMPASS4",-1),
("COMPASS5",-1),
("COMPASS6",-1),
("COMPASS7",-1),
("COMPASS8",-1),
("COMPASS9",-1),
("MAP1",-1),
("MAP2",-1),
("MAP3",-1),
("MAP4",-1),
("MAP5",-1),
("MAP6",-1),
("MAP7",-1),
("MAP8",-1),
("MAP9",-1);

select location.name,
       location.area,
	   location.description,
	   (select avg(ifnull(fantasyPoints.value, 0))
		from item
		left join fantasyPoints
		       on fantasyPoints.itemName = item.name
		where item.locationId = location.id) as avgPoints
from location
order by avgPoints desc