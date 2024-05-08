import streamlit as st

# Electron configuration for atoms
electron_config = {
    "Hidrogen": "1s^1",
    "Helium": "1s^2",
    "Lithium": "1s^2 2s^1",
    "Berilium": "1s^2 2s^2",
    "Boron": "1s^2 2s^2 2p^1",
    "Karbon": "1s^2 2s^2 2p^2",
    "Nitrogen": "1s^2 2s^2 2p^3",
    "Oksigen": "1s^2 2s^2 2p^4",
    "Fluorin": "1s^2 2s^2 2p^5",
    "Neon":"1s^2 2s^2 2p^6",
    "Natrium":"1s^2 2s^2 2p^6 3s^1",
    "Magnesium":"1s^2 2s^2 2p^6 3s^2",
}

st.title("Electron Configuration")
st.write("Select an atomic number:")

atomic_number = st.selectbox("Atomic Name", list(electron_config.keys()))

st.write("Electron Configuration:")
st.write(electron_config[atomic_number])