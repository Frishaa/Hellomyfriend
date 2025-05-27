import streamlit as st

st.title("🎈🧡Hello Guys💝💖💣")
st.write("😻Thank you for🐯 click this web big love sasha, Xoxo💝")

st.image("pngtree-cute-funny-cat-illustration-png-image_16803570.png", width=300)
st.image("0974bdaa9f61a3afc1fb004984fb9a37.jpg", width=300)

st.title("Best App")
st.header("Best App cek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah angka:"),value=0, step=1

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
