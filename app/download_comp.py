from abc import ABC, abstractmethod
from openpyxl import Workbook
import pandas as pd
import streamlit as st
from io import BytesIO


class FileDownloadComp(ABC):
    """ダウンロードのコンポーネント（抽象クラスの練習兼ねる）"""
    @abstractmethod
    def show_download_button(self, download_file_name: str) -> None:
        pass


class Wb2ExcelDownload(FileDownloadComp):
    """WBをexcelとしてダウンロード"""

    def __init__(self, wb: Workbook) -> None:
        self._wb = wb

    def show_download_button(self, download_file_name: str) -> None:
        bytes_io = BytesIO()  # BytesIOはファイルのように振る舞う。
        self._wb.save(bytes_io)  # Excelデータを BytesIO に入れる。
        data = bytes_io.getvalue()
        st.download_button(
            label="Download data as excel",
            data=data,
            file_name=f"{download_file_name}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )


class Df2ExcelDownload(FileDownloadComp):
    """DFをexcelとしてダウンロード"""
    def __init__(self, df: pd.DataFrame) -> None:
        self._df = df

    def show_download_button(self, download_file_name: str) -> None:
        bytes_io = BytesIO()  # BytesIOはファイルのように振る舞う。
        self._df.to_excel(bytes_io, index=False)  # Excelデータを BytesIO に入れる。
        data = bytes_io.getvalue()
        st.download_button(
            label="Download data as excel",
            data=data,
            file_name=f"{download_file_name}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )


class Df2CsvDownload(FileDownloadComp):
    """DFをcsvとしてダウンロード"""
    def __init__(self, df: pd.DataFrame, encoding="utf-8") -> None:
        self._df = df
        self._encoding = encoding

    def show_download_button(self, download_file_name: str) -> None:
        data = self._df.to_csv(index=False).encode(self._encoding)
        st.download_button(
            label="Download data as csv",
            data=data,
            file_name=f"{download_file_name}.csv",
            mime="text/csv",
        )
