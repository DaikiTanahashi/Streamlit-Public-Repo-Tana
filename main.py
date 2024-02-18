import streamlit as st

from app.df_upload_comp import DfUploadComp
from app.df_download_comp import DfDownloadComp
from app.df_merge_comp import DfMergeComp


def main():
    st.title("File merger")
    st.write(
        "２つのファイル（csvまたはexcel）を取り込んで、指定された列でvlookup的なアレでくっつけます。 ※csvの中身に改行があるとダメです。"
    )

    col1, col2 = st.columns(2)

    with col1:
        df_comp1 = DfUploadComp("df1")
        df_comp1.show_upload_button()
        df_comp1.show_options_with_filter()

    with col2:
        df_comp2 = DfUploadComp("df2")
        df_comp2.show_upload_button()
        df_comp2.show_options_with_filter()

    st.divider()

    if df_comp1.df is not None and df_comp2.df is not None:
        m_comp = DfMergeComp(df_comp1, df_comp2)
        m_comp.show_merge_button()

        if m_comp.df is not None:
            DL_comp = DfDownloadComp(m_comp.merged_name)
            DL_comp.show_df_DL_button_as_xlsx(m_comp.df)
            DL_comp.show_df_DL_button_as_csv(m_comp.df)


if __name__ == "__main__":
    # StreamlitのスタイリングTips より
    # https://qiita.com/papasim824/items/af2d18f3802e632ffa80
    SET_PAGE_CONFIG = {
        "page_title": "File merger",
        "layout": "wide",
        "initial_sidebar_state": "collapsed",
    }
    st.set_page_config(**SET_PAGE_CONFIG)
    main()
