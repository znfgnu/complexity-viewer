import neurokit2 as nk
import streamlit as st


def st_simulate_signal():
    colA, colB = st.columns(2)
    with colA:
        col1, col2 = st.columns(2)
        with col1:
            duration = st.slider("Duration [s]", min_value=1., max_value=10., value=10.)
            sampling_rate = st.slider("Sampling rate [Hz]", min_value=1, max_value=1000, value=100)
            noise = st.slider("Noise", min_value=0., max_value=1., value=0.02)
        with col2:
            frequency1 = st.slider("Frequency 1 [Hz]", min_value=10e-9, max_value=10., value=1.)
            frequency2 = st.slider("Frequency 2 [Hz]", min_value=10e-9, max_value=10., value=1.5)
            amplitude = st.slider("Amplitude", min_value=0.0, max_value=10.0, value=.5)
    with colB:
        signal = nk.signal_simulate(duration=duration, sampling_rate=sampling_rate, frequency=[frequency1, frequency2], noise=noise, amplitude=1., random_state=0) * amplitude
        st.line_chart(signal)
    return signal
