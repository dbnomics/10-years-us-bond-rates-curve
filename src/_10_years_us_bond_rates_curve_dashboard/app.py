import importlib

import plotly_express as px
import streamlit as st
from dbnomics import fetch_series
from streamlit_option_menu import option_menu

package_dir = importlib.resources.files("_10_years_us_bond_rates_curve_dashboard")
st.set_page_config(
    page_title="10 Years Bond Rates",
    page_icon=str(package_dir / "images/favicon.png"),
)
st.image(str(package_dir / "images/dbnomics.svg"), width=300)
st.title(":blue[10 Years Bond Rates]")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css(package_dir / "assets/styles.css")
st.markdown(
    """
    <style>
    hr {
        height: 1px;
        border: none;
        color: #333;
        background-color: #333;
        margin-top: 3px;
        margin-bottom: 3px;
    }
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("---")
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Explanations", "United-States", "Germany", "France", "Sources"],
        icons=["book", "bar-chart", "bar-chart", "bar-chart", "search"],
        menu_icon=":",
        default_index=0,
    )


if selected == "Explanations":
    st.subheader("**Definitions**")
    st.write(
        "**10 years bonds** are a type of **loan granted to a government** by an investor.\n"
        "In return, the bond issuer agrees to pay interest at regular intervals and to repay the principal borrowed at a future date, 10 years later.\n"
        "\n"
        "These 10-year bonds are a **key barometer of economic and financial health**. Their rate (known as yield) **fluctuates with monetary policies, inflation, and crises**.\n"
    )
    st.markdown("---")
    st.write(
        "**The interest rate on bonds (or \"yield\") is the percentage return on investment that the investor receives**. This rate varies based on several factors, including:\n"
        "- The duration of the bond.\n"
        "- The credit quality of the issuer.\n"
        "- Overall economic conditions.\n"
        "- Central bank monetary policies.\n"
    )
if selected == "United-States":
    # Plot data for US
    us_bond = fetch_series("FED/H15/RIFLGFCY10_N.B")
    trace_us = px.line(
        us_bond,
        x="original_period",
        y="original_value",
        title="10 Years Yield Bond for United-States",
        labels={"original_period": "Date", "original_value": "Bond rate (%)"},
        custom_data=["original_period", "original_value"],
    )

    st.write(
        "Some **significant periods** in Global Economy are easily identifiable through this curve: \n"
        "- The **1970s-80s** with the **highest recorded rates due to high volatility**. Rates were rising because of staglation and oil shocks. Restrictive monetary policies lead to a rate above 10%.In the 80s, Paul Volcker's significant fight against inflation in the US drives rates to 15%.\n"
        "- Following **the 2008 crisis**, interest rates remained very low, **ranging between 2% and 3%**. The slow recovery and accommodative policies from the Federal Reserve contributed to this prolonged period of low rates.\n "
        "- The historically **lowest rates after 2020**, rates plummet to record lows (0.5-1%) with **massive stimulus measures**.Then, rates rise (3-4%) in response to **re-emerging inflation between 2021 and 2023**.\n"
    )
    trace_us.update_traces(
        hovertemplate="<br>".join(
            [
                "Date: %{customdata[0]}",
                "10 years Bond rates (%): %{customdata[1]}",
            ]
        ),
        line=dict(color="gold"),
    )

    st.plotly_chart(trace_us)
    st.subheader("Dataset")
    st.write(us_bond)

if selected == "Germany":
    # Plot data for germany
    german_bond = fetch_series("BUBA/BBK01/WT1010")
    trace_ger = px.line(
        german_bond,
        x="original_period",
        y="original_value",
        title="10 Years Yield Bond for Germany",
        labels={"original_period": "Date", "original_value": "Bond rate (%)"},
        custom_data=["original_period", "original_value"],
    )
    trace_ger.update_traces(
        hovertemplate="<br>".join(
            [
                "Date: %{customdata[0]}",
                "10 years Bond rates (%): %{customdata[1]}",
            ]
        ),
        line=dict(color="deeppink"),
    )
    st.plotly_chart(trace_ger)
    st.subheader("Dataset")
    st.write(german_bond)

if selected == "France":
    # Plot data for France
    french_bond = fetch_series("BDF/FM/M.FR.EUR.FR2.BB.FR10YT_RR.YLD")
    trace_fr = px.line(
        french_bond,
        x="original_period",
        y="original_value",
        title="10 Years Yield Bond for France",
        labels={"original_period": "Date", "original_value": "Bond rate (%)"},
        custom_data=["original_period", "original_value"],
    )
    trace_fr.update_traces(
        hovertemplate="<br>".join(
            [
                "Date: %{customdata[0]}",
                " 10 years Bond rates (%): %{customdata[1]}",
            ]
        ),
        line=dict(color="green"),
    )
    st.plotly_chart(trace_fr)
    st.subheader("Dataset")
    st.write(french_bond)

if selected == "Sources":
    st.subheader("**Data**\n")
    st.write(
        "**United States**:\n"
        "- [10 Years Bond Rates](https://db.nomics.world/FED/H15/RIFLGFCY10_N.B)\n"
        "\n"
        "**Germany**:\n"
        "- [10 Years Bond Rates](https://db.nomics.world/BUBA/BBK01/WT1010)\n"
        "\n"
        "**France**:\n"
        "- [10 Years Bond Rates](https://db.nomics.world/BDF/FM/M.FR.EUR.FR2.BB.FR10YT_RR.YLD)\n"
    )
