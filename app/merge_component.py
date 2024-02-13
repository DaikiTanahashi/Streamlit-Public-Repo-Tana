import pandas as pd
import streamlit as st
from io import BytesIO

from app.df_component import df_component


class merge_component:
    def __init__(self) -> None:
        self.df = None

    def show_merge_button(
        self, df_component1: df_component, df_component2: df_component
    ):
        if st.button("let's merge!"):
            df = pd.merge(
                df_component1.df,
                df_component2.df,
                left_on=df_component1.selected_option,
                right_on=df_component2.selected_option,
                how="left",
            )
            self.df = df
            st.caption("Sample (first 3 rows)")
            st.write(df.head(n=3))

    def show_DL_button(self):
        if self.df is not None:
            self._convert_df_csv()
            self._convert_df_xlsx()

    def _convert_df_csv(self):
        csv_data=self.df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download data as CSV",
            data=csv_data,
            file_name="large_df.csv",
            mime="text/csv",
        )

    def _convert_df_xlsx(self):
        output = BytesIO()  # BytesIOは、Excelデータを一時的に保持するためのもの
        self.df.to_excel(output, index=False)
        xlsx_data =output.getvalue()
        st.download_button(
            label="Download data as EXCEL",
            data=xlsx_data,
            file_name="large_df.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
