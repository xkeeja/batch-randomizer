import streamlit as st
import random


# inject CSS
m = st.markdown("""
<style>
div.stButton {display: flex; justify-content: center}
h1 {text-align: center;}
p {text-align: center; color: grey;}
</style>""",unsafe_allow_html=True)


st.markdown("<h1>Batch #1191</h1>", unsafe_allow_html=True)
st.markdown("<p>Neyla • Hippolyte • Justin • Clement • Andrii • Yusuke • Jack • Sarat • Rukun</p>", unsafe_allow_html=True)


st.markdown("![The Claw](https://media.tenor.com/8dflUTn1LGEAAAAC/better-place-claw-machine.gif)")


if 'batch' not in st.session_state:
    st.session_state['batch'] = ['Neyla', 'Sarat', 'Yusuke', 'Jack', 'Clement', 'Justin', 'Hippolyte', 'Rukun', 'Andrii']


current = "Up next..."

if st.button("The Claw"):
    if len(st.session_state['batch']) == 0:
        current = 'No more students! Reload the page.'
    else:
        random.shuffle(st.session_state['batch'])
        current = st.session_state['batch'].pop()

st.markdown(f"<h1 style='color: red;'>{current}</h1>", unsafe_allow_html=True)
