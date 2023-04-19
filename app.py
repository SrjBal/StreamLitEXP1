import streamlit as st

st.write("""
# Largest Number

This app calculates the largest of 3 given numbers
""")
n1 = st.number_input("First Number")
n2 = st.number_input("Second Number")
n3 = st.number_input("Third Number")

if ( n1 >= n2 ):
  if ( n1 >= n3 ):
    ans = n1
  else:
    ans = n3
else:
  if ( n2 >= n3 ):
    ans = n2
  else:
    ans = n3
 
st.write(ans)
    
