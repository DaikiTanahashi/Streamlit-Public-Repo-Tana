import pandas as pd
import streamlit as st
from io import BytesIO


class merge_component:
    def __init__(self, radio_xlsx_csv) -> None:
        self.df = None
        self.radio_xlsx_csv = radio_xlsx_csv

    def show_merge_button(self, df_component1, df_component2):
        if st.button("let's merge!"):
            df = pd.merge(
                df_component1.df,
                df_component2.df,
                left_on=df_component1.selected_option,
                right_on=df_component2.selected_option,
                how="left",
            )
            self.df = df
            st.write(df.head(n=3))

    def show_DL_button(self):
        if self.df is not None:
            if self.radio_xlsx_csv == "csv":
                data = self._convert_df_csv()

                st.download_button(
                    label="Download data as CSV",
                    data=data,
                    file_name="large_df.csv",
                    mime="text/csv",
                )
            else:
                data = self._convert_df_xlsx()
                st.download_button(
                    label="Download data as EXCEL",
                    data=data,
                    file_name="large_df.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )

    @st.cache  # 同じ入力値が関数に渡された場合、cacheを返すことで再計算がskipされる
    def _convert_df_csv(self):
        # 結果をキャッシュして、再実行ごとの余分な計算を防ぐ
        return self.df.to_csv(index=False).encode("utf-8")

    @st.cache
    def _convert_df_xlsx(self):
        output = BytesIO()  # BytesIOは、Excelデータを一時的に保持するためのもの
        self.df.to_excel(output, index=False)
        return output.getvalue()
