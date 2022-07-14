import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

# st.write('DataFrame')

# df = pd.DataFrame({
#     '1col':[1, 2, 3, 4],
#     '2col':[10, 11, 12, 13]
# })

# st.dataframe(df.style.highlight_max(axis=0),width=200)

# st.table(df.style.highlight_max(axis=0))

# df2 = pd.DataFrame(
#     np.random.rand(100,2) / 50 + [35.69, 139.70],
#     columns=['lat','lon']
# )
# st.dataframe(df2)
# st.map(df2)

st.write('Progress Bar')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.001)

'Done!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？',0 ,100, 50)

# st.write("あなたの趣味：{}".format(text))
# st.write("コンデジション{}".format(condition))


# option = st.selectbox(
#     '貴方が好きな数字を教えてください。',
#     list(range(1,11))
# )

# st.write("貴方が好きな数字は{}です".format(option))

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img,caption='Inazawa Ryuta',use_column_width=True)