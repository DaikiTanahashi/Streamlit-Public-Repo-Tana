import streamlit as st

from app.ErrorHandler import CustomError
from app.df_upload_comp import DfUploadComp
from app.download_comp import *
from app.df_merge_comp import DfMergeComp
from main import setting


def file_merger() -> None:
    setting()
    st.title("File merger")
    st.write(
        "２つのファイル（csvまたはexcel）を取り込んで、指定された列でvlookup的なアレでくっつけます。 ※csvの中身に改行があるとダメです。"
    )

    col1, col2 = st.columns(2)

    with col1:
        try:
            df_comp1 = DfUploadComp("df1")
            df_comp1.show_upload_button()
            df_comp1.show_options_with_filter()
        except CustomError as e:
            st.info(e)

    with col2:
        try:
            df_comp2 = DfUploadComp("df2")
            df_comp2.show_upload_button()
            df_comp2.show_options_with_filter()
        except CustomError as e:
            st.info(e)

    st.divider()

    if df_comp1.df is not None and df_comp2.df is not None:
        m_comp = DfMergeComp(df_comp1, df_comp2)
        m_comp.show_merge_button()

        if m_comp.df is not None:
            DL_xlsx_comp:FileDownloadComp = Df2ExcelDownload(m_comp.df)
            DL_xlsx_comp.show_download_button(m_comp.merged_name)
            DL_csv_comp:FileDownloadComp = Df2CsvDownload(m_comp.df)
            DL_csv_comp.show_download_button(m_comp.merged_name)
