from time import sleep
from pprint import pp
#import json
import csv

import retrievebuses as retrievebuses

#BODS login data
address = 'https://data.bus-data.dft.gov.uk/api/v1/datafeed?'
api_key = 'XXXX'

#Diagonal corners of box to get buses from
boundingBox = 'XXXX,XXXX,XXXX,XXXX'

relevant_routes = {'XX', 'XX', 'XX'} #Set of routes we're interested in

filelocation = "C:\\XXXX"
filetype = ".csv"
suffix = "a"
filename  = ""

log = {}
logcount = 0
filecount = 0

field_names = ['VehicleRef', 'PublishedLineName', 'DestinationName', 'Timestamp', 'Longitude', 'Latitude']

while True:
    
    try:        
        buses = retrievebuses.retrieve_buses(address, boundingBox, api_key, relevant_routes)
                    
        #Append the bus data to the log and increment the log count
        for bus in buses:
            log[logcount] = buses[bus]
            logcount = logcount + 1
    except:
        pass
    
    if logcount >1000:
        filename = filelocation + str(filecount) + suffix + filetype
        print (filename)
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            for entry in log:
                writer.writerow(log[entry])
        
        log.clear()
        logcount = 0
        filecount = filecount + 1
        
        
    print("Buses in this log: {} Files saved: {} Approx. total records: {}".format(logcount, filecount, ((filecount * 1000)+logcount)))
        
    if filecount > 2000: exit()
    
    sleep(15)
