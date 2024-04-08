import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import List
from ..api.gflights_scrapper import GFlightsScrapper
from ..utils.email import send_email
from ..utils.mongo import MongoDataManager


class SecretarySolver:

    def __init__(
        self,
        flight_deadline: bool,
        routes: List[str],
        user_mail: str,
        use_duration_weight: bool = False,
    ):
        self.flight_deadline = flight_deadline
        self.routes = routes
        self.user_mail = user_mail

        self.scrapper = GFlightsScrapper()
        self.use_duration_weight = use_duration_weight

        db_url = "mongodb"
        db_name = "flights"
        self.db_manager = MongoDataManager(db_url, db_name)

    def setup(self):
        self.intialization_date = datetime.now()
        self.history = pd.DataFrame(
            columns=["date", "route", "price", "flight_duration"]
        )

    def estimate_possible_dates(self):
        """
        Returns a list of all the possible samples from now to the deadline
        (once a day)
        """
        today = datetime.now()
        delta = self.flight_deadline - today
        num_days = delta.days
        return [today + timedelta(days=i) for i in range(num_days)]

    def estimate_measuring_cutoff(self):
        """
        Returns the date up to the 37% of the possible dates
        """
        loc = 0.37 * len(self.estimate_possible_dates())
        date_loc = self.estimate_possible_dates()[int(loc)]
        return date_loc

    def normalizer(self, data):
        """
        Normalizes the data using the min-max normalization method
        """
        return (data - data.min()) / (data.max() - data.min())

    def run_analysis(self):
        """
        If the date is before the measuring cutoff, the secretary will
        take the price and the flight duration of the route and store it.

        Otherwise, the secretary will take the best price and flight duration
        and check if it is better than the previous ones. If it is, it will
        send a notification to the user via email.
        """
        today = datetime.now()
        if today < self.estimate_measuring_cutoff():
            for route in self.routes:
                price, flight_duration = self.scrapper.get_flight_info(route)
                self.history = self.history.append(
                    {
                        "date": today,
                        "route": route,
                        "price": price,
                        "flight_duration": flight_duration,
                    },
                    ignore_index=True,
                )
                self.db_manager.store_flight_data(
                    self.user_mail, route, price, flight_duration
                )

        else:
            # Take the best price and flight duration
            best_price = self.history["price"].min()
            best_flight_duration = self.history[self.history["price"] == best_price][
                "flight_duration"
            ].values[0]
            if self.use_duration_weight:
                scores = self.normalizer(best_price) + self.normalizer(
                    best_flight_duration
                )
            else:
                scores = self.normalizer(best_price)
            if scores.min() == scores.iloc[-1]:
                # Send email to user
                self.send_email()
            else:
                pass

    def send_email(self):
        send_email(
            self.user_mail,
            "Best flight found",
            "The secretary has found the best flight for you!",
        )
