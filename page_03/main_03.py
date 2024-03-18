import streamlit as st


def calc_unit_value() -> None:
    st.title("数量当たりの価格計算アプリ")

    col1, col2 = st.columns(2)

    with col1:
        result1 = None
        price1 = st.number_input("比較対象１の価格（円）:", min_value=0, step=1)
        quantity1 = st.number_input("比較対象１の数量:", min_value=0, step=1)

    with col2:
        result2 = None
        price2 = st.number_input("比較対象２の価格（円）:", min_value=0, step=1)
        quantity2 = st.number_input("比較対象２の数量:", min_value=0, step=1)

    if st.button("計算する"):
        result1 = calculate_price_per_unit(price1, quantity1)
        result2 = calculate_price_per_unit(price2, quantity2)
        with col1:
            st.write(f"比較対象１の数量当たりの価格: {result1:.2f}")
        with col2:
            st.write(f"比較対象２の数量当たりの価格: {result2:.2f}")

        # result1とresult2の大小を比較して、小さいほうを表示
        if result1 is not None and result2 is not None:
            if result1 < result2:
                st.write("比較対象１の方が安いです")
            elif result1 > result2:
                st.write("比較対象２の方が安いです")
            else:
                st.write("比較対象１と比較対象２の数量当たりの価格は同じです")


def calculate_price_per_unit(price, quantity):
    if quantity == 0:
        st.write("数量は0では割れません")
        return None
    price_per_unit = price / quantity
    return price_per_unit
