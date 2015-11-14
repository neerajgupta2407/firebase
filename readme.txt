#Steps:
1)download the file and cd to folder
2) Run: python api.py

# Now it will fetch all the runners data and 
the runner whose location was updated in last 60 sec(last_time_sync_limit) will be displayed
#######Dummy output
Current time is : 2015-11-10 13:12:03
Runner:865622026692355 {u'latitude': 28.5623088, u'longitude': 77.2027819} 2015-11-10 13:11:54

#To check for the old data
set Current_time some past epoc value
current_time = 1447085311
it will display the runners data aftr this time

o/p:
Current time is : 2015-11-09 21:38:31
Runner:867947020118877 {u'latitude': 28.5086557, u'longitude': 77.060771} 2015-11-10 03:19:23
Runner:865622026692355 {u'latitude': 28.5623088, u'longitude': 77.2027819} 2015-11-10 13:11:54