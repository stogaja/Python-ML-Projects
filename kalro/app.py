import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt

st.title("Group V Week V Covid-19 Final Project")
data = pd.read_csv("owid-covid-data.csv")


selected = st.sidebar.selectbox("Select the section", [
                                'Dataset', 'Mortality Rates', 'Vaccine Coverage', 'Effect of COVID on Continents', 'Overall Population Change', 'Stringency Index', 'life expectancy'])

st.markdown('The table above is the general outlook of our dataset.')

if selected == 'Dataset':
    st.write(data)
elif selected == 'Mortality Rates':
    # QUESTION 1: FINDING THE CHANGES IN MORTALITY RATE FROM WHEN
    # THERE WERE NO VACCINES TO WHEN THERE WAS AN ABUNDANCE IN VACCINES
    vacc_death = pd.DataFrame(data[:3000], columns=[
                              'total_deaths', 'total_vaccinations'])
    st.line_chart(vacc_death)
    st.markdown(
        'The tabulated bar graph above shows the changes in mortality rates with vaccinations.')
elif selected == 'Vaccine Coverage':
    # QUESTION 2: FINDING THE AREAS WITH LOW VACCINE COVERAGE
    # let's find the areas with low vaccine supply and print the first 10 rows
    low_vaccine_areas = pd.DataFrame(
        data['total_vaccinations'].groupby(data['location']).min().sort_values(axis=0, ascending=False).head(10))
    st.bar_chart(low_vaccine_areas)
    st.markdown(
        'The tabulated bar graph above shows the countries with no vaccine coverage.')
elif selected == 'Effect of COVID on Continents':
    # QUESTION 3: Lets find the continent most affected by COVID 19 and the least one and their number.
    # 1. South America was the most affected continent with total deaths of 341,631,554 people
    # 2. Australia / Oceania was the least affected continent with total deaths of 743,222 people.

    most_affected_continent = pd.DataFrame(
        data.groupby('continent').sum().sort_values(by="total_deaths", ascending=False).head(1))
    st.bar_chart(most_affected_continent)
    st.markdown(
        'The tabulated bar graph above shows the continent most affected by COVID-19.')
elif selected == 'Overall Population Change':
    # QUESTION 4: Let’s find the overall change in population from the COVID-19 pandemic in
    population_difference_distribution = pd.DataFrame(
        data['population_diff'].value_counts()).head(5)
    st.bar_chart(population_difference_distribution)
    st.markdown('The tabulated bar graph above shows the population difference.')
elif selected == 'Stringency Index':
    # QUESTION 6: Let’s investigate the changes in stringency index
    # as a result of COVID deaths in Kenya, Malaysia, Spain, Venezuela, Panama
    stringency = pd.DataFrame(
        data[['continent', 'stringency_index']].groupby('continent').mean())
    st.line_chart(stringency)
    st.markdown(
        'The tabulated line graph above shows the stringency index fluctuations in different continents.')
else:
    # QUESTION 7: Let’s find the changes in life expectancy as a result of COVID-19
    life_expectancy = pd.DataFrame(
        data[['continent', 'life_expectancy']].groupby('continent').mean())
    st.line_chart(life_expectancy)
    st.markdown(
        'The tabulated line graph above shows the life expectancy changes in different continents.')
