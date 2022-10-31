import streamlit as st
import pandas as pd
import numpy as np

# Load plotting packages.
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import altair as alt  # Import altair package to display graphs.
import plotly .express as px  # Import plotly package.

# If a backend gui is necessary to configure. By default, this setting is not necessary.
# matplotlib.use('Agg')


def main():

    st.title('Plotting with st.pyplot.')

    a_df = pd.read_csv('data/iris.csv')  # Load csv file.

    st.dataframe(a_df.head())

    species_count_ds = a_df['species'].value_counts()
    st.dataframe(species_count_ds)
    st.write(type(species_count_ds))

    # Use PYPLOT method to plot in Stramlit.
    a_figure, a_ax = plt.subplots()
    a_df['species'].value_counts().plot(kind='bar')
    st.pyplot(a_figure)

    # ALternative in Seaborn.
    b_figure = plt.figure()
    sns.countplot(x='species', data=a_df)
    st.pyplot(b_figure)

    # Using st.bar_chart.
    st.bar_chart(a_df['sepal_length'])
    st.bar_chart(a_df[['sepal_length', 'petal_length']])

    # Usign line chart with a different dataset.
    b_df = pd.read_csv('data/lang_data.csv')
    lang_list = b_df.columns.tolist()
    lang_choices = st.multiselect('Choose Languages', lang_list, default='Python')
    selected_languages_df = b_df[lang_choices]
    st.dataframe(selected_languages_df.head())
    st.line_chart(selected_languages_df)

    # Using area chart.
    # st.area_chart(selected_languages_df, use_container_width=True)
    st.area_chart(selected_languages_df)

    # Using altair chart.
    c_df = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
    st.dataframe(c_df)
    c = alt.Chart(c_df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.write(c)

    # or,
    st.altair_chart(c, use_container_width=True)

    # Using plotly package.
    d_df = pd.read_csv('data/prog_languages_data.csv')
    st.dataframe(d_df)

    c_figure = px.pie(d_df, values='Sum', names='lang', title='Pie chart for prog language.')
    st.plotly_chart(c_figure)

    d_figure = px.bar(d_df, x='lang', y='Sum')
    st.plotly_chart(d_figure)


    return


if __name__ == '__main__':

    main()
