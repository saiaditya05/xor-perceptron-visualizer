import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="XOR Visualizer",
    page_icon="🧠"
)

st.title("XOR & Perceptron Visualizer")
st.write("Explore the XOR truth table interactively.")

a = st.selectbox("Input A", [0, 1])
b = st.selectbox("Input B", [0, 1])

result = a ^ b

st.subheader("Prediction")
st.metric("XOR Output", result)

st.write("XOR returns 1 when inputs differ and 0 when they are the same.")

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

fig, ax = plt.subplots()

for i in range(4):
    color = "red" if y[i] == 1 else "blue"
    ax.scatter(X[i, 0], X[i, 1], color=color, s=150)
    ax.annotate(
        f"Output {y[i]}",
        (X[i, 0] + 0.03, X[i, 1] + 0.03)
    )

ax.set_xlabel("Input A")
ax.set_ylabel("Input B")
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.grid(True)

st.pyplot(fig)
