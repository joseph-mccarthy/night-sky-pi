from time import sleep
import time_functions as time
import sun_functions as sun
from capture import capture
import logging

logging.basicConfig(level=logging.DEBUG)

def main() -> None:
    coordinates = (51.7678, 0.0878)
    while True:
        yesterday, today, tomorrow = time.get_dates()
        
        yesterday_sunrise,yesterday_sunset = sun.get_rise_and_set(yesterday,coordinates)
        today_sunrise,today_sunset = sun.get_rise_and_set(today,coordinates)
        tomorrow_sunrise,tomorrow_sunset = sun.get_rise_and_set(tomorrow,coordinates)
        
        if today > today_sunset and today < tomorrow_sunrise:
            logging.info("After Sunset before Midnight")
            capture(today,coordinates,(today_sunset,tomorrow_sunrise))
        elif today < today_sunrise and today > yesterday_sunset:
            logging.info("Between Midnight and Sunrise")
            capture(yesterday,coordinates,(yesterday_sunset,today_sunrise))
        else:
            if today < today_sunset:
                logging.info(f"Waiting for sunset at {today_sunset}")
                print('process images')    
        
        s = 60
        logging.debug(f'Debug sleep for {s}s')
        sleep(s)  

if __name__ == "__main__":
    main()