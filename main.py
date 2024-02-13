import streamlit as st

from app.df_component import df_component
from app.merge_component import merge_component


def main():
    st.title("File merger")
    st.write("２つのファイル（csv or excel）を指定列でvlookup的な感じでくっつけます。")

    col1, col2 = st.columns(2)

    with col1:
        df_component1 = df_component("df1")
        df_component1.show_df()
        df_component1.show_options_with_filter()

    with col2:
        df_component2 = df_component("df2")
        df_component2.show_df()
        df_component2.show_options_with_filter()

    st.divider()

    if df_component1.df is not None and df_component2.df is not None:
        m_component = merge_component()
        m_component.show_merge_button(df_component1, df_component2)
        m_component.show_DL_button()


if __name__ == "__main__":
    main()
