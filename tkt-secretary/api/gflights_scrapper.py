from when2flight import FlightSearch
from datetime import datetime, timedelta


class GFlightsScrapper:
    def __init__(self):
        self.searcher = FlightSearch()

    def get_flight_info(self, route):
        # Assume route is a string like "NYC-LAX" for New York to Los Angeles
        origin, destination = route.split("-")
        # Perform the flight search for today's date or your preferred date
        today = datetime.now()
        flight_data = self.searcher.search_flights(
            origin=origin,
            destination=destination,
            departure_date=today.strftime("%Y-%m-%d"),
            return_date=(today + timedelta(days=7)).strftime(
                "%Y-%m-%d"
            ),  # Example return date
        )

        if flight_data.empty:
            return None, None  # Handle case where no data is found

        # Assuming we take the first result or find the best one based on some criteria
        best_flight = flight_data.iloc[0]
        price = best_flight["price"]
        flight_duration = best_flight[
            "duration"
        ]  # Check the actual key for flight duration in your data

        return price, flight_duration
