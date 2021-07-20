import streamlit as st
from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt

def plot_dist(alpha_value: float, beta_value: float, data: np.ndarray = None):
    beta_dist = beta(alpha_value, beta_value)

    xs = np.linspace(0, 1, 1000)
    ys = beta_dist.pdf(xs)

    fig, ax = plt.subplots(figsize=(7, 3))
    ax.plot(xs, ys)
    ax.set_xlim(0, 1)
    ax.set_xlabel("x")
    ax.set_ylabel("P(x)")

    if data is not None:
        likelihoods = beta_dist.pdf(data)
        sum_log_likelihoods = np.sum(beta_dist.logpdf(data))
        ax.vlines(data, ymin=0, ymax=likelihoods)
        ax.scatter(data, likelihoods, color="black")
        st.write(
            f"""
_Under your alpha={alpha_slider:.2f} and beta={beta_slider:.2f},
the sum of log likelihoods is {sum_log_likelihoods:.2f}_
"""
        )
    st.pyplot(fig) 