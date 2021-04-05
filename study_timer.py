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

print("Commands:\n   ls: list all timers\n   start timername: start the timer timername\n   stop: stop the last timer\n   rm timername: remove the timer timername\n   quit")
started = False

while True:
	command = str(input("\033[1m$> \033[0m"))
	if command=="ls":
		if not timers:
			print("No timers created")
		else:
			print(timers)
	elif command=="quit":
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
			timers.pop(splitted_command[1], None)
			serialize(timers)
