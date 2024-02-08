# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 01:30:41 2024

@author: Sreejit
"""

import streamlit as st

# Page title
st.title("Saraswati Puja date?")


st.write("""
Well, this marks the end of my very elongated, and possibly very late, proposal for you to be my date on the 14th. But I promise you, this is only the beginning of creating countless memories together. 

In just a few days, we'll be celebrating two whole years of being in love, and it feels like time has flown by faster than I finish food on my plate or you grab the opportunity to call me brainless! 😄

I look forward to being there for all those days where you shower me with so much love that it makes my heart melt and the days where you are so grumpy that i choose my words so carefully as if my life depended on it. I am going to be there always. We'll make the best old couple, and others will be so jealous of our love.

I love you, and I will always love you.

Forever Yours,
Yash
""")

st.header("SAY YES  :triumph:")

# Unique key for the selectbox
selectbox_key = "yes_or_no"
# Prompt for "Yes" or "No"
answer = st.selectbox(f"Will you be my valentine", ["", "Yes", "No"], key=selectbox_key, index = "Yes")

# Handle the response
while answer != "Yes":
    selectbox_key = selectbox_key + "i"    
    if answer == "No":
        answer = st.selectbox(":angry: AGAIN", ["", "Yes", "No"], key=selectbox_key)
    else:
        st.warning("select 'Yes' to continue.")
        answer = st.selectbox(f"SAY YES or NO", ["", "Yes", "No"], key=selectbox_key)
        

# If the answer is 'Yes'
if answer == "Yes":
    st.success("Okay! See you on the 14th! :heart:")
                
