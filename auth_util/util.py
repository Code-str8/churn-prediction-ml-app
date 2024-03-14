import streamlit as st
import pandas as pd
import numpy as np

# Transform TotalCharges using log1p
def log1p_transform(df):
    df['TotalCharges'] = np.log1p(df['TotalCharges'])
    return df