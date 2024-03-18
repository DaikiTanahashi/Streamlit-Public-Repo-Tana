import os
import streamlit as st
from pathlib import Path

from app.download_comp import *
from app.df_upload_comp import DfUploadComp
from app.template_processor import CustomError, ExcelTemplateProcessor
from main import setting


def import_to_template() -> None:
    setting()
    st.title("Import Data To Template Excel")
    st.write("ファイルを取り込んで、Excelのテンプレートファイルに落とし込むやつ")

    df_comp = DfUploadComp("df")
    df_comp.show_upload_button()

    st.divider()

    if df_comp.df is not None:
        try:
            template_file_path = Path(f"{os.curdir}/page_02/sampledata.xlsx")
            TemplateProcessor = ExcelTemplateProcessor(template_file_path)
            TemplateProcessor.dataframe_to_excel(df_comp.df, "&&data")
            DL_xlsx_comp: FileDownloadComp = Wb2ExcelDownload(TemplateProcessor.wb)
            DL_xlsx_comp.show_download_button("test")
        except CustomError as e:
            st.info(e)
