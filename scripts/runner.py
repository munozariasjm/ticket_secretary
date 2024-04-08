import schedule
import time
from datetime import datetime, timedelta
from secretary_solver import SecretarySolver


def setup_user_interaction():
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    route = input("Enter your desired route (e.g., 'NYC-LAX'): ")
    flight_deadline = datetime.now() + timedelta(
        days=30
    )  # Assuming a 30-day window for purchasing tickets

    return username, email, route, flight_deadline


def daily_task(username, email, route, flight_deadline):
    db_url = "mongodb://localhost:27017/"  # Your MongoDB URL
    db_name = "flight_data"  # Your database name
    solver = SecretarySolver(flight_deadline, [route], email, db_url, db_name)
    solver.run_analysis()


if __name__ == "__main__":
    username, email, route, flight_deadline = setup_user_interaction()
    schedule.every().day.at("10:00").do(
        daily_task, username, email, route, flight_deadline
    )

    while True:
        schedule.run_pending()
        time.sleep(1)
