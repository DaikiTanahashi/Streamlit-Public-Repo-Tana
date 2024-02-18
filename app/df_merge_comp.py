import os
import pandas as pd
import streamlit as st

from app.df_upload_comp import DfUploadComp


class DfMergeComp:
    def __init__(self, df_comp1: DfUploadComp, df_comp2: DfUploadComp) -> None:
        self.df = None
        self.df1 = df_comp1.df
        self.df2 = df_comp2.df
        self.select1 = df_comp1.selected_option
        self.select2 = df_comp2.selected_option
        self.file_name1 = self._shorten_name(df_comp1.uploaded_file.name, 20)
        self.file_name2 = self._shorten_name(df_comp2.uploaded_file.name, 20)
        self.merged_name = f"{self.file_name1}_{self.file_name2}"

    def _shorten_name(self, file_name: str, max_length: int):
        base_name, extension = os.path.splitext(file_name)  # 名前と拡張子を分割
        if len(base_name) > max_length:
            return base_name[:max_length]
        else:
            return base_name

    def show_merge_button(self):
        if st.button("let's merge!"):
            self.df1[self.select1] = self.df1[self.select1].astype(str)
            self.df2[self.select2] = self.df2[self.select2].astype(str)
            df = pd.merge(
                self.df1,
                self.df2,
                left_on=self.select1,
                right_on=self.select2,
                how="left",
            )
            self.df = df
            st.caption("Sample (first 3 rows)")
            st.write(df.head(n=3))
