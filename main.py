import pandas as pd
import streamlit as st
from chardet import detect

from app.test import show_options_with_filter


def get_df_from_uploaded_file(uploaded_file) -> pd.DataFrame:
    st.write(uploaded_file.name)
    file_name = uploaded_file.name
    file_extension = file_name.split(".")[-1]  # 拡張子を取得

    st.write(file_extension)

    if "xls" in file_extension:
        df = pd.read_excel(uploaded_file)
        return df
    elif file_extension == "csv":
        binary_data = uploaded_file.getvalue()
        encode_data = detect(binary_data)
        st.write(encode_data)
        encoding = encode_data["encoding"]
        df = pd.read_csv(uploaded_file, encoding=encoding)
        return df


def main():
    col1, col2 = st.columns(2)

    with col1:
        uploaded_file = st.file_uploader("Choose a left_file")
        if uploaded_file is not None:
            df1 = get_df_from_uploaded_file(uploaded_file)
            st.write(df1)
            options = df1.columns.tolist()
            df1_key = show_options_with_filter(options, "df1")
            st.write(df1_key)

    with col2:
        uploaded_file = st.file_uploader("Choose a right_file")
        if uploaded_file is not None:
            df2 = get_df_from_uploaded_file(uploaded_file)
            st.write(df2)
            options = df2.columns.tolist()
            df2_key = show_options_with_filter(options, "df2")
            st.write(df2_key)


if __name__ == "__main__":
    main()
