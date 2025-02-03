# BODS
Routines for adventures with bus open data service. This lot is all in Python 3.

Retrieve buses is a routine for interacting with Bus Open Data Services which gives GPS locations and various other data for buses in a given bounding box. It is a government run service and the data is updated every ten seconds.
Buslogger takes that data and drops it into csv files for later use.

Learner is my first attempt at using machine learning on the dataset. Results on around 10,000 data points are:
Score 1.0
The coefficient for VehicleRef is -0.0015208793658823229
The coefficient for PublishedLineName is -0.006847318499563902
The coefficient for DestinationName is 0.01007110100594977
The coefficient for Longitude is -1.7644682438867791
The coefficient for Latitude is 0.5664663578969962
Intercept -31.857782714389565

Plan is to use this to augment the bustracker, which draws data from a webpage of live departures that's not entirely reliable. For example, it measures due time by the bus crossing time-gates on its route. If there is variable traffic the time gates remain the same and a bus can get stuck at "due in 5 minutes" for ages. I would like to use ML to allow me to predict where, given current bus coordinates, the bus will be in 2 minutes time. That's how long it takes to get to the stop. I would also like to know how long it will take that bus to get to work, roughly.
My idea is to use current bus coordinates to map onto a "modelled bus timeline", then a) look forwards in that modelled timeline by 2 minutes and output corresponding coordinates and b)look forward in that timeline by X minutes until coordinates = work. I have no idea how, yet.

