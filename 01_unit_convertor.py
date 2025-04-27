import streamlit as st

def unit_converter():
    st.title("Unit Converter Program")
    st.write("1. Length (m to km, km to m)")
    st.write("2. Weight (kg to lbs, lbs to kg)")
    st.write("3. Temperature (C to F, F to C)")

    # Choice selection
    choice = st.radio("Choose a conversion", ["1", "2", "3"])

    if choice == "1":
        unit_type = st.selectbox("Convert from 'm to km' or 'km to m'", ['m to km', 'km to m'])
        value = st.number_input("Enter the value:", min_value=0.0)
        if unit_type == "m to km":
            st.write(f"{value} meters = {value / 1000} kilometers")
        elif unit_type == "km to m":
            st.write(f"{value} kilometers = {value * 1000} meters")

    elif choice == "2":
        unit_type = st.selectbox("Convert from 'kg to lbs' or 'lbs to kg'", ['kg to lbs', 'lbs to kg'])
        value = st.number_input("Enter the value:", min_value=0.0)
        if unit_type == "kg to lbs":
            st.write(f"{value} kilograms = {value * 2.20462:.2f} pounds")
        elif unit_type == "lbs to kg":
            st.write(f"{value} pounds = {value / 2.20462:.2f} kilograms")

    elif choice == "3":
        unit_type = st.selectbox("Convert from 'C to F' or 'F to C'", ['c to f', 'f to c'])
        value = st.number_input("Enter the value:", min_value=-100.0)
        if unit_type == "c to f":
            fahrenheit = (value * 9/5) + 32
            st.write(f"{value}°C = {fahrenheit:.2f}°F")
        elif unit_type == "f to c":
            celsius = (value - 32) * 5/9
            st.write(f"{value}°F = {celsius:.2f}°C")
        else:
            st.write("Invalid unit type.")

unit_converter()












