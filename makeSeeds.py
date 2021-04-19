import os
import sys
import time
import json
import argparse
import datetime

def loadLadxrFlags(path):
    with open(path, 'r') as iFile:
        flags = json.load(iFile)

    return flags

def makeSeeds(ladxrPath, flagsFile, seedCount):
    import multiprocessing
    sys.path.insert(0, ladxrPath)
    import main as ladxr

    processesStarted = 0
    activeProcesses = set()
    coreCount = multiprocessing.cpu_count()
    ladxrFlags = loadLadxrFlags(flagsFile)

    while processesStarted < seedCount or activeProcesses:
        if len(activeProcesses) < coreCount and processesStarted < seedCount:
            process = multiprocessing.Process(target=ladxr.main, kwargs={"mainargs": ladxrFlags})
            process.start()
            processesStarted += 1
            activeProcesses.add(process)
        else:
            finishedProcesses = set(x for x in activeProcesses if not x.is_alive())
            activeProcesses = activeProcesses.difference(finishedProcesses)
            time.sleep(0.1)

def main():
    parser = argparse.ArgumentParser(description='LADXR bulk seed generator')
    parser.add_argument("--ladxrPath", dest="ladxrPath", type=str, required=True,
        help="Path to the directory that LADXR lives in")
    parser.add_argument("--ladxrFlagsFile", dest="ladxrFlagsFile", type=str, required=True,
        help="Path to a json file that contains a list of command line arguments to pass to LADXR when generating seeds")
    parser.add_argument("--seedCount", dest="seedCount", type=int, required=True,
        help="Number of seeds to generate")
    args = parser.parse_args()

    startTime = datetime.datetime.now()
    makeSeeds(args.ladxrPath, args.ladxrFlagsFile, args.seedCount)
    print(f"Duration: {datetime.datetime.now() - startTime}")

if __name__ == "__main__":
    main()