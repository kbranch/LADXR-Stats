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

## Processing the Data
`parseResults.py` has a few rough functions that process the data once it's in the database.

- `suggestSampleSize` selects progressively larger subsets of the database to estimate what sample size is required to minimize run-to-run variation. Expects `ladxr_stats.sqlite` to contain around 10,000 seeds for best results.
- `createItemFrequencyTable` uses the data in `ladxr_stats.sqlite` to create a table showing how often each item shows up in each location. See [suggested formatting](https://docs.google.com/spreadsheets/d/1fYG7p9YDfY1eE3eNhBL02JhMHmFbWfvb7rgd81bnsVc/edit?usp=sharing), shamelessly stolen from the ALTTPR community.
