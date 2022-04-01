import argparse
import logging
from data import Observation, Location, SunData
import time_functions as time
import sun_functions as sun
import capture


class Main:

    location: Location

    RUNNING = True

    def __init__(self, lat, lon):
        self.location = Location(lat, lon)

    def run(self) -> None:

        while self.RUNNING:
            yesterday, today, tomorrow = time.get_dates()

            yesterday_sun = sun.get_rise_and_set(yesterday, self.location)
            today_sun = sun.get_rise_and_set(today, self.location)
            tomorrow_sun = sun.get_rise_and_set(tomorrow, self.location)

            if today > today_sun.sunset and today < tomorrow_sun.sunrise:
                logging.info("After Sunset before Midnight")
                sundata = SunData(today_sun.sunset, tomorrow_sun.sunrise)
                capture.run(Observation(today, self.location, sundata))
            elif today < today_sun.sunrise and today > yesterday_sun.sunset:
                logging.info("Between Midnight and Sunrise")
                sundata = SunData(yesterday_sun.sunset, today_sun.sunrise)
                capture.run(Observation(yesterday, self.location, sundata))
            else:
                logging.info(f"Waiting for sunset at {today_sun.sunset}")
                print("process images")


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

    application = Main(args.lat, args.lon)
    application.run()
