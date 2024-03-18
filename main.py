import streamlit as st


def setting() -> None:
    # StreamlitのスタイリングTips より
    # https://qiita.com/papasim824/items/af2d18f3802e632ffa80
    SET_PAGE_CONFIG: dict = {
        "page_title": "File processor",
        "layout": "wide",
        "initial_sidebar_state": "expanded",
    }
    st.set_page_config(**SET_PAGE_CONFIG)

def main() -> None:
    st.header("左のバーから利用するアプリを選択してください。")
    st.write("file marger: ファイルを左外部結合するやつ")
    st.write("import to template: ←こっちは工事中")


if __name__ == "__main__":
    setting()
    main()
