import time

firebase_app_url = 'https://boiling-torch-3635.firebaseio.com/'
last_time_sync_limit = 60 # Suposed tto be the cron time




####Helping functions
def get_runner_last_loc(runner,current_time):
	# runner the dict of runners data
	# current_Time is the time at which cron started.
	# We don'a want any delay dats y using curren time specified by calling function
	# @return  two values: time and runner location 
	if 'datapoints' in runner:
		# reverse sorting the runner data by time
		runner_times = sorted(runner['datapoints'],reverse=True)
		for key in runner_times:	
			# will execute loop only once and i.e for the first element
			# since we already sorted out the dict by time desc
			i = int(key) / 1000.0 # converting milisec to secs
			if current_time - last_time_sync_limit <= i :

				# UPDATED location found
				#print key
				return key,runner['datapoints'][key]
			else:
				# runner's location is not updated
				# sending False
				return False,False
			break		
	return False,False

def epoc_to_time(epoc):
	import time
	# function to convert epoc time to display str
	i = int(epoc) / 1000.0 # converting milisec to secs
	return (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i)))

def dummy_fe_fun(runner, loc, last_time):
	# function which will use the fe's locatoion
	print runner, loc, epoc_to_time(last_time)


########################Executable functions

from firebase import firebase
firebase = firebase.FirebaseApplication(firebase_app_url, None)
current_time = time.time()
#current_time = 1447085311
# Getting all the runners
all_runner = firebase.get('/', None,  {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print 'Current time is :', epoc_to_time(current_time*1000)

for runner in all_runner:
	## getting the last sync data of runner
	last_time,runner_last_loc = get_runner_last_loc(all_runner[runner], current_time)

	if runner_last_loc:
		# If runner last loc is not false means we get its updated location.
		# So forwarding the location so FMS Server
		dummy_fe_fun(runner,runner_last_loc, last_time)

