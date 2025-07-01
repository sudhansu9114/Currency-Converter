import streamlit as st
import requests
st.title("Currency Converter")

amount=st.number_input("Enter amount in INR",min_value=0.0,value=0.0)
target_currency=st.selectbox("Convert to :",["USD","EUR","JPY","GBP","AUD","CAD","CNY"])

if st.button("Convert"):
    if amount == 0.0:
        st.warning("Please enter a value greater than 0")
    else:
        url="https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/inr.json"
        response=requests.get(url)
    
        if response.status_code==200 :
            data=response.json()
            try:
                conversion_rate=data["inr"][target_currency.lower()]
                converted_amount=amount*conversion_rate
                st.success("Conversion Successful")
                st.success(f"{amount} INR = {converted_amount:.2f} {target_currency.upper()}")
            except KeyError:
                st.error(f"Conversion rate for '{target_currency}' not found.")
            
        else:
            st.error(f"Failed to fetch currency data. Status code : {response.status_code}")

