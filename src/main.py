import time_functions as time
import sun_functions as sun
from capture import capture
import logging
import argparse


def main(lat,lon) -> None:
    coordinates = (lat,lon)
    
    run = True
    while run:
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
        
        run = False 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lat",type=float,required=True,help="Latitude position of the camera")
    parser.add_argument("--lon",type=float,required=True,help="Longitude position of the camera")
    parser.add_argument("--log",type=str,required=False,help="Log Level",default=logging.WARNING)

    args = parser.parse_args()
    
    logging.basicConfig(level=args.log)
    main(args.lat,args.lon)