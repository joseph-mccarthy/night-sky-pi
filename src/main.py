import time_functions as time
import sun_functions as sun
from capture import capture
from data import Observation,Location,SunData
import logging
import argparse


def main(lat, lon) -> None:
    location = Location(lat,lon)

    run = True

    while run:
        yesterday, today, tomorrow = time.get_dates()

        yesterday_sun = sun.get_rise_and_set(yesterday, location)
        today_sun = sun.get_rise_and_set(today, location)
        tomorrow_sun = sun.get_rise_and_set(tomorrow, location)

        if today > today_sun.sunset and today < tomorrow_sun.sunrise:
            logging.info("After Sunset before Midnight")
            sundata = SunData(today_sun.sunset,tomorrow_sun.sunrise)
            capture(Observation(today,location,sundata))
        elif today < today_sun.sunrise and today > yesterday_sun.sunset:
            logging.info("Between Midnight and Sunrise")
            sundata = SunData(yesterday_sun.sunset,today_sun.sunrise)
            capture(Observation(yesterday,location,sundata))
        else:
            logging.info(f"Waiting for sunset at {today_sun.sunset}")
            print("process images")

        run = False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lat", type=float, required=True,
                        help="Latitude position of the camera")
    parser.add_argument("--lon", type=float, required=True,
                        help="Longitude position of the camera")
    parser.add_argument("--log", type=str, required=False, help="Log Level", default=logging.WARNING
                        )
    args = parser.parse_args()

    logging.basicConfig(level=args.log)

    main(args.lat, args.lon)
