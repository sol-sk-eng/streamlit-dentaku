import streamlit as st
def calculator():
    st.title("電卓アプリ")

    # 入力フィールド
    num1 = st.number_input("数字を入力してください", value=0.0)
    num2 = st.number_input("もう一つの数字を入力してください", value=0.0)

    # 演算子の選択
    operation = st.selectbox("演算子を選択してください", ["+", "-", "*", "/"])

    # 計算ボタン
    if st.button("計算する"):
        result = perform_operation(num1, num2, operation)
        st.success(f"{num1} {operation} {num2} = {result}")

def perform_operation(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            st.error("0で割ることはできません")
            return None

# アプリの実行
if __name__ == "__main__":
    calculator()
