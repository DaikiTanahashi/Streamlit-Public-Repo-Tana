import pandas as pd
import streamlit as st
from chardet import detect


class df_component:
    def __init__(self, df_name: str) -> None:
        self.df_name = df_name
        self.uploaded_file = st.file_uploader(f"Choose a file for {self.df_name}")

    def show_df(self):
        if self.uploaded_file is not None:
            self._get_df()

    def _get_df(self) -> pd.DataFrame:
        file_name = self.uploaded_file.name
        file_extension = file_name.split(".")[-1]  # 拡張子を取得
        if "xls" in file_extension:
            df = pd.read_excel(self.uploaded_file)
            self.df = df
        elif file_extension == "csv":
            binary_data = self.uploaded_file.getvalue()
            encode_data = detect(binary_data)
            encoding = encode_data["encoding"]
            df = pd.read_csv(self.uploaded_file, encoding=encoding)
            self.df = df
        else:
            st.write("拡張子が正しくありません。")
            self.uploaded_file = None

    def show_options_with_filter(self):
        if self.uploaded_file is not None:
            options = self.df.columns.tolist()
            filter_text = st.text_input(f"Filter options for {self.df_name}", "")
            selected_option = st.selectbox(
                f"Select option for {self.df_name}",
                self._filtered_options(options, filter_text),
                label_visibility="collapsed",
            )
            self.selected_option = selected_option

    def _filtered_options(self, options: list, filter_text: str) -> list:
        # フィルタされた項目だけをリストに保持
        filtered_options = []
        for option in options:
            if filter_text.lower() in option.lower():
                filtered_options.append(option)
        return filtered_options
