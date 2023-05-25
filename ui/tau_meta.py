import streamlit as st
import pandas as pd


def st_tau_meta(tau_params: dict, tau_values: dict):
    for method, params in tau_params.items():
        params.pop("Scores", None)
        params.pop("Values", None)
        params.update({'Tau': tau_values[method]})
    st.table(pd.DataFrame(tau_params.values()))
