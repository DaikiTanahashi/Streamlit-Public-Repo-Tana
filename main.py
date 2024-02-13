import streamlit as st

from app.df_comp import df_comp
from app.merge_comp import merge_comp


def main():
    st.title("File merger")
    st.write("２つのファイル（csv or excel）を指定列でvlookup的な感じでくっつけます。")

    col1, col2 = st.columns(2)

    with col1:
        df_comp1 = df_comp("df1")
        df_comp1.show_df()
        df_comp1.show_options_with_filter()

    with col2:
        df_comp2 = df_comp("df2")
        df_comp2.show_df()
        df_comp2.show_options_with_filter()

    st.divider()

    if df_comp1.df is not None and df_comp2.df is not None:
        m_comp = merge_comp()
        m_comp.show_merge_button(df_comp1, df_comp2)
        m_comp.show_DL_button()


if __name__ == "__main__":
    main()
