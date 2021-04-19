import os
import json
import datetime
import sqlalchemy
import argparse
from glob import glob
from sqlalchemy.orm import sessionmaker

import model
from model import Rom, Location, Flag, Item

def main():
    parser = argparse.ArgumentParser(description='LADXR log consumer')
    parser.add_argument("--logPath", dest="logPath", type=str, required=True,
        help="Path to a directory that contains json log files from LADXR")
    parser.add_argument("--dbPath", dest="dbPath", default="ladxr_stats.sqlite", type=str, required=False,
        help="Path to the SQLite database file")
    args = parser.parse_args()

    engine = sqlalchemy.create_engine(f'sqlite:///{args.dbPath}')
    model.Base.metadata.create_all(engine)

    startTime = datetime.datetime.now()

    Session = sessionmaker(bind=engine)
    session = Session()

    seenLocations = {}
    results = session.query(Location.name, Location).all()
    for row in results:
        seenLocations[row.name] = row.Location

    logGlob = glob(os.path.join(args.logPath, '*.json'))
    for path in logGlob:
        with open(path, 'r') as iFile:
            log = json.load(iFile)
        
        result = session.query(Rom.seed).filter(Rom.seed == path).first()

        if result:
            print(f"File {path} already exists in database, skipping")
            continue

        newRom = Rom(path)

        for arg in log['options']:
            Flag(arg, log['options'][arg], newRom)
        
        for item in log['accessibleItems']:
            if item['id'] not in seenLocations:
                loc = Location(item['id'], item['locationName'], item['area'])
                session.add(loc)

                seenLocations[item['id']] = loc
            
            Item(item['itemName'], item['sphere'], item['player'], seenLocations[item['id']], newRom)
        
        session.add(newRom)

    session.commit()

    print(f'Duration: {datetime.datetime.now() - startTime}')

if __name__ == "__main__":
    main()