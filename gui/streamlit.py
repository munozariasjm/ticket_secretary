import streamlit as st
import pymongo
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def fetch_data(username, db_url, db_name):
    client = pymongo.MongoClient(db_url)
    db = client[db_name]
    collection = db["user_flights"]
    data = collection.find({"username": username})
    return pd.DataFrame(data)


def plot_data(df):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    sns.histplot(df["price"], kde=True, ax=ax[0])
    ax[0].set_title("Price Distribution")

    sns.histplot(df["flight_duration"], kde=True, ax=ax[1])
    ax[1].set_title("Flight Duration Distribution")

    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    sns.scatterplot(x="price", y="flight_duration", data=df, ax=ax2)
    ax2.set_title("Price vs. Flight Duration")
    st.pyplot(fig2)


def main():
    st.title("Flight Price History and Analysis")

    db_url = "mongodb://localhost:27017/"  # Replace with your MongoDB URL
    db_name = "flight_data"  # Replace with your database name

    username = st.text_input("Enter your username:")
    if st.button("Fetch History"):
        if username:
            df = fetch_data(username, db_url, db_name)
            if not df.empty:
                st.write("Historical Flight Data:")
                st.dataframe(df[["date", "route", "price", "flight_duration"]])
                plot_data(df)
            else:
                st.write("No data found for the user.")


if __name__ == "__main__":
    main()
