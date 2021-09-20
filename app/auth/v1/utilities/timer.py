import time

class UserTimer():

    def pomodoro(t):
        print("Timer starts now!")
        for i in range(4):
            set_time = t*60
            while set_time:
                mins = t // 60
                secs = t % 60
                timer = '{:02d}:{:02d}'.format(mins,secs)
                print("" + timer, end ="\r")
                time.sleep(1)
                t -= 1
            print('its Break time!')
            t = 10*60
            while t:
                mins = t//60
                secs = t % 60
                timer = '{:02d}:{:02d}'.format(mins,secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
            print("Work Time!")

