import streamlit as st
import pandas as pd
import re

def parse_log_line(line):
    # This is a basic parser; a real one would be more robust
    match = re.search(r'Latency: ([\d.]+)ms.*PII: (True|False).*Error: (True|False)', line)
    if match:
        latency = float(match.group(1))
        pii = match.group(2) == 'True'
        error = match.group(3) == 'True'
        return {'latency': latency, 'pii_detected': pii, 'error_detected': error}
    return None

st.title('Chatbot Live Monitor Dashboard')
st.markdown('### Key Metrics')

# Read logs and parse data
log_data = []
try:
    with open('chatbot.log', 'r') as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                log_data.append(parsed)
except FileNotFoundError:
    st.warning("`chatbot.log` not found. Please run the monitoring script first.")

if log_data:
    df = pd.DataFrame(log_data)
    
    # Display key metrics
    total_logs = len(df)
    error_count = df['error_detected'].sum()
    pii_count = df['pii_detected'].sum()
    avg_latency = df['latency'].mean()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Logs", total_logs)
    col2.metric("Error Rate", f"{error_count / total_logs:.2%}")
    col3.metric("PII Detections", pii_count)
    col4.metric("Avg. Latency", f"{avg_latency:.2f}ms")

    st.markdown('### Latency Distribution')
    st.line_chart(df['latency'])
    
    st.markdown('### PII and Error Breakdown')
    st.dataframe(df)