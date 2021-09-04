from pygame import mixer
def musiconloop(file,stopper):
	mixer.init()
	mixer.music.load(file)
	mixer.music.play()
	while True:
		a = input()
		if a == stopper:
			mixer.music.stop()
			break
musiconloop("mrbean.mp3","stop") 
 # the file name or yuo can also use the file path

