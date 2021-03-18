# LADXR-Stats
LADXR-Stats is a tool to generate LADXR seeds in bulk, load the resulting logs into a database, then run reports to hopefully learn things.

## Generating Seeds
`makeSeeds.py` runs LADXR in parallel to generate seeds in bulk. The example args file turns on json logging and discards the actual generated ROMs. It needs a copy of LADXR to do its thing.

## Consuming Logs
`consumeLogs.py` consumes the json logs that LADXR spits out and loads them into an SQLite database. Remains to be seen how well performance holds up with large amounts of data, but it seems workable so far.

This is a really basic example query that pulls all of the spoiler logs back out of the database:
```
select *
from rom
join item
  on item.romId = rom.id
join location
  on location.id = item.locationId
order by rom.id, item.sphere
```
