from openpyxl import Workbook
import pandas as pd
import streamlit as st
from io import BytesIO


class DfDownloadComp:
    def __init__(self, download_file_name: str) -> None:
        self.download_file_name = download_file_name

    def show_wb_download_button(self, wb: Workbook) -> None:
        wb_bytes_io = BytesIO()  # BytesIOはファイルのように振る舞う。
        wb.save(wb_bytes_io)  # Excelデータを BytesIO に入れる。
        self._set_download_button_as_xlsx(wb_bytes_io)

    def show_df_download_button_as_xlsx(self, df: pd.DataFrame) -> None:
        xl_bytes_io = BytesIO()  # BytesIOはファイルのように振る舞う。
        df.to_excel(xl_bytes_io, index=False)  # Excelデータを BytesIO に入れる。
        self._set_download_button_as_xlsx(xl_bytes_io)

    def _set_download_button_as_xlsx(self, bytes_io: BytesIO) -> None:
        data = bytes_io.getvalue()
        st.download_button(
            label="Download data as EXCEL",
            data=data,
            file_name=f"{self.download_file_name}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

    def show_df_download_button_as_csv(
        self, df: pd.DataFrame, encoding="utf-8"
    ) -> None:
        csv_data = df.to_csv(index=False).encode(encoding)
        st.download_button(
            label="Download data as CSV",
            data=csv_data,
            file_name=f"{self.download_file_name}.csv",
            mime="text/csv",
        )
