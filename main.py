import streamlit as st

from app.df_component import df_component


def main():
    col1, col2 = st.columns(2)

    with col1:
        df_component1 = df_component("df1")
        df_component1.show_df()
        df_component1.show_options_with_filter()

    with col2:
        df_component2 = df_component("df2")
        df_component2.show_df()
        df_component2.show_options_with_filter()
        
    # df_component1.df
    # df_component1.selected_option


if __name__ == "__main__":
    main()
