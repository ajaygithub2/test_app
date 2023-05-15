import streamlit as st
import datetime
from dateutil import relativedelta


DOB = st.date_input("Enter your DOB", min_value=datetime.datetime(1950,1,1))

today = datetime.datetime.today()

delta = relativedelta.relativedelta(today, DOB)

st.write(f"You have been on this earth for {delta.years} years, {delta.months} months, {delta.days} days.")
