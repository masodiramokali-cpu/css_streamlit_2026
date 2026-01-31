# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 07:48:14 2026

@author: Masodi Ramokali
"""

import streamlit as st

st.markdown(
    "<style>.stApp { background-color: lightpink; }</style>",
    unsafe_allow_html=True
)


st.title("MCR Sneakers")


st.image(
    "https://img.ltwebstatic.com/images3_pi/2024/03/15/06/171051719158542ebaa75e435460ad9bb499efd184_thumbnail_405x.webp"
    ,width=250
)

st.title("MCR Sneakers")

category = st.selectbox("Select Category", ["Children","Adults"])

gender = st.selectbox("Select Gender", ["Female","Male"])

size = st.selectbox("Select Size", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if category == "Children":
    price = 600
else: 
    price = 1000
    
quantity = st.number_input("Quantity", min_value=1, value=1)

total = price * quantity 

st.write("### Order Details")
st.write("Sneaker: The Swegg")
st.write("Category:", category)
st.write("Gender:", gender)
st.write("Size:", size)
st.write("Price per pair: R", price)
st.write("Total price: R", total)

if st.button("Buy Now"):
    st.success("Purchase successful!")
