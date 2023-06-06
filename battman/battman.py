import psutil

def get_battery_level():
    battery = psutil.sensors_battery()
    if battery is None:
        return "No battery detected"
    else:
        return f"Battery at {battery.percent}%"

print(get_battery_level())

