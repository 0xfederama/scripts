import json, pathlib, time

def serialize(dictionary):
	path = pathlib.Path(str(pathlib.Path.home())+"/.config/study-timer")
	path.mkdir(parents=True, exist_ok=True)
	with open(str(pathlib.Path.home())+"/.config/study-timer/timers.json", "w") as outfile:
		json.dump(dictionary, outfile, indent=4)

try:
	with open(str(pathlib.Path.home())+"/.config/study-timer/timers.json") as f:
		timers = json.load(f)
except FileNotFoundError:
	timers = {}

print("Commands:\n   ls -> list all timers\n   start \'timername\' -> start the timer timername\n   stop -> stop the last timer\n   rm \'timername\' -> delete the timer timername\n   quit")
started = False

while True:
	command = str(input("\033[1m$> \033[0m"))
	if command=="":
		continue
	elif command=="ls":
		if not timers:
			print("No timers created")
		else:
			for x in timers:
				print(f"{x}: {timers[x]} minutes")
	elif command=="quit":
		if started is True:
			print("You have to stop the timer before quitting")
		else:
			break
	else:
		splitted_command = command.split()
		if splitted_command[0]=="start":
			if started is True:
				print("You already started a timer")
				continue
			start = time.time()
			started = True
			timer_name = splitted_command[1]
			timers[timer_name] = timers.get(timer_name, 0)
			print(f"Timer {timer_name} started")
		elif splitted_command[0]=="stop":
			if started is False:
				print("Timer was not started")
				continue
			end = time.time()
			interval = int((end-start)/60)
			print(f"You studied for {interval} minutes")
			started = False
			timers[timer_name] = timers.get(timer_name, 0)+interval
			serialize(timers)
		elif splitted_command[0]=="rm":
			if splitted_command[1]==timer_name:
				print("You cannot remove the timer that is running right now")
			else:
				timers.pop(splitted_command[1], None)
				serialize(timers)
				print("Timer deleted")
		else:
			print("This command does not exist")
