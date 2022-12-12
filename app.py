import streamlit as st
from PIL import Image

st.title('サプーアプリンリン')
st.caption('これはサプーの動画用のテストアプリです')
st.subheader('自己紹介')
st.text('Pythonに関する情報をYouTube上で発信しているPython VTuber　サプーです。\n'
'よければチャンネル登録よろしくお願いします')

code = '''
import streamlit as st 
st.title('サプーアプリ')
'''

st.code(code, language='python')

#画像
image = Image.open('１.jpg')
st.image(image,width=280)
#動画
# video_file = open('1.mov','rb')
# video_bytes = video_file.read()
# st.video(video_bytes)

#フォーム画面作成
with st.form(key='profile_form'):
    #テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')
    # print(name)

    #セレクトボックス
    age_category = st.selectbox(
        '年齢層',
        ('子ども（18才未満)','大人(18才以上)')
    )

    #複数選択
    hobby = st.multiselect(
        '趣味',
        ('スポーツ','読書','プログラミング','アニメ・映画','釣り','料理')
    )

    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    
# print(f'submit_btn: {submit_btn}')
# print(f'cancel_btn: {cancel_btn}')
if submit_btn:
    st.text(f'ようこそ！{name}さん！{address}に書類を送りました！')
    st.text(f'年齢層：{age_category}')
    st.text(f'趣味：{",".join(hobby)}')