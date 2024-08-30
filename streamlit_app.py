import streamlit as st
import yfinance as yf
import pandas as pd

# Streamlit app
def main():
    st.title("Stock Price Viewer")
    
    # Input from the user: Stock ticker
    ticker_symbol = st.text_input("Enter Stock Ticker", "AAPL")

    # Get the date range from the user
    start_date = st.date_input("Start Date", pd.to_datetime("2023-01-01"))
    end_date = st.date_input("End Date", pd.to_datetime("today"))

    if st.button("Show Stock Prices"):
        # Fetching stock data
        try:
            ticker_data = yf.download(ticker_symbol, start=start_date, end=end_date)

            if not ticker_data.empty:
                # Display the stock data
                st.subheader(f"Stock Prices for {ticker_symbol} from {start_date} to {end_date}")
                st.line_chart(ticker_data['Close'])
                st.dataframe(ticker_data)
            else:
                st.warning("No data available for the given date range.")
        except Exception as e:
            st.error(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()
