import streamlit as st

st.title("📦 Story Card Stock Teller")

st.write("Enter your stock counts below:")

# Input fields
stock_a = st.slider("3 Story Cards A", min_value=0, value=12)
stock_b = st.slider("3 Story Cards B", min_value=0, value=13)
stock_c = st.slider("2 Story Cards", min_value=0, value=4)

# Buffer selection
buffer = st.slider("Safety Buffer (units to keep aside)", min_value=0,max_value=10, value=3)

# Calculate available packs
pack_3 = stock_a
pack_6 = min(stock_a, stock_b)
pack_8 = min(stock_a, stock_b, stock_c)

st.subheader("📊 Stock Availability")
st.write(f"3 Card Packs: **{pack_3}**")
st.write(f"6 Card Packs: **{pack_6}**")
st.write(f"8 Card Packs: **{pack_8}**")

# Safe recommendation
safe_3 = max(0, pack_3 - buffer)
safe_6 = max(0, pack_6 - buffer)
safe_8 = max(0, pack_8 - buffer)

st.subheader("✅ Safe Stock Recommendation for Amazon")
st.write(f"3 Card Packs: **{safe_3}**")
st.write(f"6 Card Packs: **{safe_6}**")
st.write(f"8 Card Packs: **{safe_8}**")

st.info("Tip: Adjust the buffer if you expect bulk orders, then copy the safe stock values to Amazon.")
