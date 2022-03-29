import time_functions as time
import sun_functions as sun
from capture import capture
import logging
import argparse


def main(lat, lon) -> None:
    pos = (lat, lon)

    run = True

    while run:
        yesterday, today, tomorrow = time.get_dates()

        _, yesterday_ss = sun.get_rise_and_set(yesterday, pos)
        today_sr, today_ss = sun.get_rise_and_set(today, pos)
        tomorrow_sr, _ = sun.get_rise_and_set(tomorrow, pos)

        if today > today_ss and today < tomorrow_sr:
            logging.info("After Sunset before Midnight")
            capture(today, pos, (today_ss, tomorrow_sr))
        elif today < today_sr and today > yesterday_ss:
            logging.info("Between Midnight and Sunrise")
            capture(yesterday, pos, (yesterday_ss, today_sr))
        else:
            if today < today_ss:
                logging.info(f"Waiting for sunset at {today_ss}")
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
