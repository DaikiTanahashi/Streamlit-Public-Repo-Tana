import streamlit as st


def show_options_with_filter(options: list, options_name: str):
    filter_text = st.text_input(f"Filter options for {options_name}", "")

    # 絞り込まれた項目を保持するリスト
    filtered_options = []
    for option in options:
        if filter_text.lower() in option.lower():
            filtered_options.append(option)

    selected_option = st.selectbox(
        f"Select option for {options_name}", filtered_options
    )
    return selected_option
