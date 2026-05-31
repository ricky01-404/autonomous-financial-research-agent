import streamlit as st
import requests
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Autonomous Financial Research Agent",
    page_icon="📈",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stTextArea textarea {
    font-size: 16px;
}

.report-box {
    padding: 20px;
    border-radius: 10px;
    background-color: #1E1E1E;
    border: 1px solid #333;
}

.metric-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #1A1A1A;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER
# -----------------------------------

st.title("📈 Autonomous Financial Research Agent")

st.markdown("""
AI-powered investment research platform with:

✅ Autonomous Planning  
✅ ReAct Reasoning  
✅ SEC Filing RAG  
✅ Multi-Source Synthesis  
✅ Vector Memory  
✅ Financial Analysis  
""")

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("⚙️ Agent Controls")

selected_company = st.sidebar.selectbox(
    "Quick Company Selection",
    [
        "NVIDIA",
        "Tesla",
        "Apple",
        "Microsoft",
        "Amazon",
        "Meta",
        "Google"
    ]
)

show_chart = st.sidebar.checkbox(
    "Show Stock Chart",
    value=True
)

show_metrics = st.sidebar.checkbox(
    "Show Financial Metrics",
    value=True
)

# -----------------------------------
# QUERY INPUT
# -----------------------------------

default_query = (
    f"Analyze {selected_company} as a long-term investment "
    f"using SEC filings, news, and valuation metrics."
)

query = st.text_area(
    "Enter Research Query",
    value=default_query,
    height=150
)

# -----------------------------------
# STOCK CHART
# -----------------------------------

if show_chart:

    ticker_map = {
        "NVIDIA": "NVDA",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Meta": "META",
        "Google": "GOOGL"
    }

    ticker = ticker_map[selected_company]

    stock = yf.Ticker(ticker)

    hist = stock.history(period="6mo")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=hist.index,
            y=hist["Close"],
            mode="lines",
            name="Close Price"
        )
    )

    fig.update_layout(
        title=f"{selected_company} Stock Price",
        xaxis_title="Date",
        yaxis_title="Price",
        height=400
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------------
# GENERATE REPORT BUTTON
# -----------------------------------

if st.button("🚀 Generate Research Report"):

    if query:

        with st.spinner(
            "Autonomous agent researching..."
        ):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/research",
                    json={
                        "query": query
                    }
                )

                result = response.json()

                report = result.get(
                    "report",
                    "No report generated."
                )

                # -----------------------------------
                # SUCCESS MESSAGE
                # -----------------------------------

                st.success(
                    "Research report generated successfully."
                )

                # -----------------------------------
                # METRICS SECTION
                # -----------------------------------

                if show_metrics:

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric(
                            "Agent Status",
                            "Active"
                        )

                    with col2:
                        st.metric(
                            "Research Sources",
                            "SEC + News + Metrics"
                        )

                    with col3:
                        st.metric(
                            "Reasoning Engine",
                            "ReAct"
                        )

                # -----------------------------------
                # REPORT DISPLAY
                # -----------------------------------

                st.subheader(
                    "📑 Investment Research Report"
                )

                st.markdown(
                    f"""
                    <div class="report-box">
                    {report}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # -----------------------------------
                # DOWNLOAD BUTTON
                # -----------------------------------

                st.download_button(
                    label="⬇️ Download Report",
                    data=report,
                    file_name="research_report.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.error(
                    f"Error generating report: {str(e)}"
                )

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.caption(
    "Built with FastAPI, Streamlit, ChromaDB, "
    "Groq LLMs, SEC RAG, and Autonomous Agents."
)