import os
import pandas as pd
import streamlit as st
from io import BytesIO

from app.df_comp import df_comp


class merge_comp:
    def __init__(self, df_comp1: df_comp, df_comp2: df_comp) -> None:
        self.df = None
        self.df1 = df_comp1.df
        self.df2 = df_comp2.df
        self.select1 = df_comp1.selected_option
        self.select2 = df_comp2.selected_option
        self.file_name1 = self._shorten_name(df_comp1.uploaded_file.name, 20)
        self.file_name2 = self._shorten_name(df_comp2.uploaded_file.name, 20)

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

    def show_DL_button(self):
        if self.df is not None:
            self._convert_df_xlsx()
            self._convert_df_csv()

    def _convert_df_xlsx(self):
        output = BytesIO()  # BytesIOは、Excelデータを一時的に保持するためのもの
        self.df.to_excel(output, index=False)
        xlsx_data = output.getvalue()
        st.download_button(
            label="Download data as EXCEL",
            data=xlsx_data,
            file_name=f"{self.file_name1}_{self.file_name2}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

    def _convert_df_csv(self):
        csv_data = self.df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download data as CSV",
            data=csv_data,
            file_name=f"{self.file_name1}_{self.file_name2}.csv",
            mime="text/csv",
        )

    def _shorten_name(self, file_name: str, max_length: int):
        base_name, extension = os.path.splitext(file_name)  # 名前と拡張子を分割
        if len(base_name) > max_length:
            return base_name[:max_length]
        else:
            return base_name
