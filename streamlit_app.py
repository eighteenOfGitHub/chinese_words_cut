import streamlit as st
import pandas as pd

from words_cut_func import *


names_to_funcs = {
    
    'FMM': FMM,
    'BMM': BMM,
    'Bi-MM': Bi_MM
}

data_names = [
    '1998版新闻',
    'THUOCL清华数据源',
    '词库融合'
]

def main():



    st.write("# 欢迎来到**分词系统**! 👋")

    st.markdown("-----------------------")

    fun_name = st.selectbox("选择算法", names_to_funcs.keys())
    data_name = st.selectbox("选择数据源", data_names)
    sentence = st.text_input("请输入中文句子：", "你好，世界！")

    is_exe = st.button("分词")

    st.markdown("-----------------------")

    words_dic = get_words_dic(data_name)
    if is_exe:
        st.write(f"**{fun_name}** 分词结果：")
        st.write('/'.join(names_to_funcs[fun_name](sentence, words_dic)))

if __name__ == "__main__":
    main()

# streamlit run ./streamlit_app.py