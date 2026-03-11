import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Bird observations", layout = "wide")

#Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title = "main menu",
        options = ["Homepage", "Data and sources", "Research Question 1", "Research Question 2", "Research Question 3", "Research Question 4", "Research Question 5", "Research Question 6", "Research Question 7", "Research Question 8", "Research Question 9"],
        icons = ["house", "database", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill", "pie-chart-fill"],
        menu_icon ="cast",
        styles={
            "container": {"padding": "5!important", "background-color": "#0e1117"},
            "icon": {"color": "green", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#000000"},
            "nav-link-selected": {"background-color": "#1d222c"},
        }
    )
#--------------------------
#        HOMEPAGE
#--------------------------
if selected == "Homepage":
    st.title("Bird observations Dashboard")
    st.subheader("Welcome to the website! Click the options to the left to explore the contents") 

    code = '''
                            ⠀⠀⠀⣀⣤⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⢀⣾⠛⠁⢰⣧⡈⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⢸⣇⣼⡀⠻⠟⠁⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⢀⡞⣹⠙⣧⡀⠀⠀⡀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⣀⡴⠋⠀⣀⣴⣿⡷⠴⠞⠁⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⢾⣁⣀⡤⠾⠛⠁⣸⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⢠⡟⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⣠⣿⠁⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⢿⣶⠶⠿⠟⠿⠿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⣼⠟⠀⠀⠀⠀⠀⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠈⠙⠛⠿⠶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢀⣀⣠⣤⣤⣤⣤⣤⣀⠀⠉⠙⠳⢦⣄⡀⣀⣤⣀⣀⡄⠀
                        ⠀⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠈⠉⠻⢶⣀⠀⠀⠈⠉⢁⠈⠏⣿⣁⠀
                        ⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣀⣀⡴⠁⠀⠀⢙⣿⡾
                        ⠀⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⣀⣠⡾⠟⠃
                        ⠀⠀⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡔⢊⣵⠞⠋⠁⠀⠀⠀
                        ⠀⠀⠀⠙⠿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠚⠉⠀⣠⣴⠟⠁⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠈⠙⠳⠶⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⢤⣤⣴⠊⣁⣤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⡷⢶⡶⠶⠤⠔⢺⠃⡟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⢰⡇⠀⡇⠀⠀⠀⢸⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠈⣹⣤⣭⠿⠟⣃⣾⠋⠀⠀⢠⡟⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠉⠙⠛⢋⣿⣙⣶⣾⡿⢷⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠻⠧⠶⠾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

    st.code(code, language=None)



#--------------------------
#      Data and sources
#--------------------------

if selected == "Data and sources":
    st.title("Data and Sources")

   
    RQ_1 = pd.read_csv("RQ_1/hamburg_birdCounts_pollution_2021-2025.csv")
    st.success("Data used for Research Question 1:")
    st.write(RQ_1)

   
    RQ_2 = pd.read_csv("RQ_2/rq_2_berlin_houspa_pollution_2023_2025_apr_jun.csv")
    st.success("Data used for Research Question 2:")
    st.write(RQ_2)

   
    RQ_3 = pd.read_csv("RQ_3/rq_3_richness_sh_data.csv")
    st.success("Data used for Research Question 3:")
    st.write(RQ_3)

   
    RQ_4 = pd.read_csv("RQ_4/berlin_pigeon_pullution_2020_2024.csv")
    st.success("Data used for Research Question 4:")
    st.write(RQ_4)


    RQ_5 = pd.read_csv("RQ_5/europe_ducks_march_2020_2024.csv")
    RQ_5_2 = pd.read_csv("RQ_5/europe_ducks_recent_daily.csv")
    st.success("Data used for Research Question 5:")
    st.write(RQ_5)
    st.write(RQ_5_2)

    RQ_6 = pd.read_csv("RQ_6/final_richness_vs_temp.csv")          
    st.success("Data used for Research Question 6:")
    st.write(RQ_6)

   
    RQ_7 = pd.read_csv("RQ_7/analyse_wind_enten_deutschland.csv")         
    st.success("Data used for Research Question 7:")
    st.write(RQ_7)

   
    RQ_8 = pd.read_csv("RQ_8/migratory_observations_SH_2021-2025.csv")
    st.success("Data used for Research Question 8:")
    st.write(RQ_8)

   
    RQ_9 = pd.read_csv("RQ_9/craneArrival_pollution_updated.csv")
    st.success("Data used for Research Question 9:")
    st.write(RQ_9)

#--------------------------
#    Research Questions
#--------------------------

if selected == "Research Question 1":
    st.title("Research Question 1")
    st.subheader("How does air Pollution affect bird observation frequency in Hamburg in the years 2021-2025 and which pollutant affects the birds the most?")


if selected == "Research Question 2":
    st.title("Research Question 2")
    st.subheader("How are hotspots of house sparrows in Berlin influenced by increased pollution in the years 2023-2025?")


if selected == "Research Question 3":
    st.title("Research Question 3")
    st.subheader("How does bird species richness differ between urban and rural locations in Schleswig-Holstein in the last 30 days?")


if selected == "Research Question 4":
    st.title("Research Question 4")
    st.subheader("How does O3 concentration influence the observation frequency of feral pigeons in Berlin in 2020-2024?")


if selected == "Research Question 5":
    st.title("Research Question 5")
    st.subheader("Which region of Europe has the highest density of Mallard ducks observations and how stable is the population over time in the years 2020-2024?")
    st.subheader("🌍Density vs. stability of Mallard Ducks (2020-2024)")

    try:
        df_hist = pd.read_csv("Streamlit/RQ_5/europe_ducks_march_2020_2024.csv")
        df_density = pd.read_csv("Streamlit/RQ_5/europe_ducks_recent_daily.csv")


        df_hist["Date"] = pd.to_datetime(df_hist["Date"])
        daily_ducks = df_hist.groupby(["Country","Date"])["DuckCount"].sum().reset_index()
        stability = daily_ducks.groupby("Country")["DuckCount"].agg(mean="mean", std="std").reset_index()
        stability["CV"] = stability["std"] / stability["mean"]

        density_country = df_density.groupby("Country").mean(numeric_only=True).reset_index()
        density_country["Density"] = density_country["DuckCount"] / density_country["LocationCount"]

        
        df_map = pd.merge(density_country, stability, on="Country", how="left")

        
        view_option = st.selectbox(
            "Choose the metric for the map:",
            ["Density", "Instability (CV)"]
        )

        target_col = "Density" if view_option == "Density" else "CV"
        color_scale = "Reds" if view_option == "Density" else "Blues"
        label_text = "Density" if view_option == "Density" else "Instability (Coefficient of Variation)"


        fig = px.choropleth(
            df_map,
            locations="Country",
            locationmode="country names",
            color=target_col,
            hover_name="Country",
            hover_data={"Density": ":.2f", "CV": ":.2f"},
            color_continuous_scale=color_scale,
            scope="europe"
        )

        fig.update_layout(
            geo=dict(
                showframe=False,
                showcoastlines=True,
                projection_type='equirectangular',
                landcolor="#0e1117",
                showland = True,
                bgcolor="#0e1117",         
                lakecolor="#0e1117"
            ),
            margin=dict(l=0, r=0, t=50, b=0),
            height = 500
        )

        st.plotly_chart(fig, use_container_width=True)

        if view_option == "Density":
            st.info("💡 **Density**: Shows where the average duck count per location for each European country.")
        else:
            st.info("💡 **Instability (CV, Coefficient of Variation)**: A high value indicates strong fluctuation over the years (for example: migration). A low value indicates a constant population.")

    except Exception as e:
        st.error(f"error: {e}")



if selected == "Research Question 6":
    st.title("Research Question 6")
    st.subheader("How does bird species richness during spring change in relation to temperature between 2020 and 2025 in northern and southern Germany")


if selected == "Research Question 7":
    st.title("Research Question 7")
    st.subheader("How does wind speed affect the observation frequency of Mallards in northern and southern Germany between 2020 and 2025, and does wind speed have a similar effect on other duck species?")


if selected == "Research Question 8":
    st.title("Research Question 8")
    st.subheader("How does the observation frequency of migratory bird species differ between spring and autumn in Schleswig-Holstein in the year 2021 and 2025 and can the potential offspring of those birds be determined?")


if selected == "Research Question 9":
    st.title("Research Question 9")
    st.subheader("Does Air pollution influence the arrival dates of cranes in Niedersachsen, Germany between 2021 and 2025?")






