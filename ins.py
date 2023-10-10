import streamlit as st
st.write("#")
st.markdown("###### A California Real Estate Case Study")
st.title("Burning Money: Why California is Over Homeowner's Insurance")
st.subheader(":red[With increasingly severe and unpredictable fire seasons, costly claims payouts have insurers spooked]")
st.markdown("""
#
###### *Last updated October 10, 2023, WIP*
#### AIG was the first to leave. Exiting the California admitted homeowner's insurance market in January 2022<sup style='font-size:.8em;'>1</sup>, the New York-based company now only offers insurance through their surplus lines. Surplus lines, an unregulated type of insurance<sup style='font-size:.8em;'>2</sup>, allow carriers to take on higher risk customers without guaranteeing a standard set of coverage conditions... and set whatever premiums they want.
##### Now, other insurers have followed suit: All State, Farmers, and State Farm have also pulled out of the new homeowner insurance market in California, citing a variety of factors including inflation and higher wildfire risk. It doesn't take a coterie of actuaries armed with calculators to realize that for insurers, the numbers just aren't adding up.
##### But what effect does this have on people trying to eke out a living in the Golden State? For one homeowner in Auburn, this meant :red[insurance premiums went up from \$2,500 to \$10,000].<sup style='font-size:.8em;'>3</sup>. Ultimately, they settled for the state's fire-only insurance for \$7,000 under the "FAIR Plan."<sup style='font-size:.8em;'>4</sup>
""",
    unsafe_allow_html=True,
)

# Climate change is resulting in longer and more extreme fire seasons, especially in areas where decades of fire suppression efforts have resulted in excess fuel build-up. The idea of ":blue[wildland urban interface]" (WUI)--where wild areas meet manmade ones--has been

# window = st.slider("Forecast window")

st.divider()
st.caption("""
Sources:

1. AID to exit California homeowners insurance https://www.spglobal.com/marketintelligence/en/news-insights/latest-news-headlines/aig-to-exit-california-homeowners-insurance-market-at-january-end-68512476
2. Surplus lines, Investopedia https://www.investopedia.com/terms/s/surplus-lines-insurance.asp#:~:text=Regular%20insurance%20carriers%2C%20also%20called,to%20take%20on%20higher%20risks.
3. Impact on California insurance claims https://www.insurancebusinessmag.com/us/news/breaking-news/californias-insurance-carrier-exits--whats-the-impact-on-claims-451619.aspx
4. FAIR Plan insurance https://www.insurance.ca.gov/01-consumers/200-wrr/California-FAIR-Plan.cfm
""")