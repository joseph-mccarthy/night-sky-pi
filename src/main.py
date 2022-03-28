import time_functions as time
import sun_functions as sun

def main() -> None:
    coordinates = (51.7678, 0.0878)
    while True:
        yesterday = time.get_yesterday()
        today = time.get_today()
        tomorrow = time.get_tomorrow()
        previous_sunrise,previous_sunset = sun.get_rise_and_set(yesterday,coordinates)
        today_sunrise,today_sunset = sun.get_rise_and_set(today,coordinates)
        next_sunrise,next_sunset = sun.get_rise_and_set(tomorrow,coordinates)
        if today > today_sunset and today < next_sunrise:
            print('take pictures')
        elif today < today_sunrise and today > previous_sunset:
            print('take pictures after midnight')      
        else:
            print('process images')      

if __name__ == "__main__":
    main()