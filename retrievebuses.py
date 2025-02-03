import requests as requests

def retrieve_buses(address, boundingBox, api_key, relevant_routes):
    buses = {} #set up the buses dictionary. One entry per bus in area of interest. This will reset every update
    Timestamp = '' #Set up a string for the timestamp
    
    url = ("{}boundingBox={}&api_key={}").format(address, boundingBox, api_key)
    response = requests.get(url)
    bulkdata = xmltodict.parse(response.content)
    
    #Collect the timestamp
    Timestamp = bulkdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']['ResponseTimestamp']
    #Timestamp = str(datetime.now())
        
    #Pull out the only data we need. Using pop default value of None if there are no buses.
    filtereddata = bulkdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'].pop('VehicleActivity', None) 
    
    #Filtereddata is a list if there are several buses, a dictionary if there's one and "0" if there are none.
    #Check for number of buses and drop their data into a dictionary
    if len(filtereddata) == 0:
        print("No buses at the moment")
        exit()
    if type(filtereddata) is dict:
        buses[0] = (filtereddata['MonitoredVehicleJourney']) #Extract the only bus into the dictionary
    else:
        for bus in range(len(filtereddata)): #Extract all buses into a dictionary with an iterated key
            buses[bus] = (filtereddata[bus]['MonitoredVehicleJourney'])
    
    #Add irrelevant buses to a list and then remove them from buses
    pop_list = []
    for bus in buses:
        if buses[bus]['PublishedLineName'] not in relevant_routes: pop_list.append(bus) 
    for bus in pop_list: buses.pop(bus)
    
    #Remove unwanted data from each bus dictionary in buses. Not 'DestinationName',
    keys_to_remove = ('LineRef', 'FramedVehicleJourneyRef', 'OperatorRef','OriginRef', 'OriginName', 'DestinationRef', 
                      'OriginAimedDepartureTime', 'DestinationAimedArrivalTime', 'BlockRef', 'Bearing', 'DirectionRef','Occupancy')
    for bus in buses:
        for key in keys_to_remove: buses[bus].pop(key, None)

    
    #Add the timestamp to each bus.
    for bus in buses:
        buses[bus]['Timestamp'] = Timestamp
    
    
    #Bring the lat and long out of their sub-dictionary
    for bus in buses:
        buses[bus]['Longitude'] = buses[bus]['VehicleLocation']['Longitude']
        buses[bus]['Latitude'] = buses[bus]['VehicleLocation']['Latitude']
        buses[bus].pop('VehicleLocation', None)
    
    return buses
