import streamlit as st
import neurokit2 as nk
from utils.context_timer import ContextTimer
from ui.streamlit import st_maximize_space
from ui.tau_meta import st_tau_meta
from ui.data.simulate_signal import st_simulate_signal

st_maximize_space()

# Get the data
st.header("Data")

signal = st_simulate_signal()

# Calculate and visualize tau values
st.header("Tau")
col1, col2, col3 = st.columns(3)

with col1:
    tau_methods = ["fraser1986", "theiler1990", "casdagli1991", "rosenstein1993", "rosenstein1994", "kim1999", "lyle2021"]
    tau_forbidden_methods = ["kim1999"]

    tau_values = {}
    tau_scores = {}
    tau_method_time = {}
    tau_params = {}

    for method in tau_methods:
        if method in tau_forbidden_methods:
            continue
        print(f"Method: {method}")

        with ContextTimer() as ct:
            tau, params = nk.complexity_delay(signal, method=method)
        print(f"Done in {ct.get_elapsed():.4f}s")

        if params["Method"] != method:
            params["Method"] += f" ({method})"
        tau_values[method], tau_params[method] = tau, params
        tau_method_time[method] = ct.get_elapsed()
        if 'Scores' in params:
            tau_scores[method] = params.get('Scores')

    st_tau_meta(tau_params, tau_values)

with col2:
    st.write("Tau")
    st.bar_chart(tau_values)

with col3:
    st.write("Time spent")
    st.bar_chart(tau_method_time)

st.write("Scores")
st.line_chart(tau_scores)
