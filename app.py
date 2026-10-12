import os
import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정 (와이드 모드 적용)
st.set_page_config(
    page_title="KIA Tigers 3D Baseball Game",
    page_icon="⚾",
    layout="wide",
)

st.title("⚾ KIA Tigers 3D Baseball Game")
st.markdown(
    "KIA 타이거즈 원정 유니폼과 ABS 존, 진루/득점 시스템이 반영된 고해상도 3D"
    " 야구 게임입니다."
)

# htmls 폴더 내의 index.html 파일 경로 설정
html_file_path = os.path.join("htmls", "index.html")

if os.path.exists(html_file_path):
  try:
    # 파일 읽기
    with open(html_file_path, "r", encoding="utf-8") as f:
      html_content = f.read()

    # 스림릿 컴포넌트를 이용해 HTML/JS/CSS 렌더링
    # height 값을 조절하여 게임 화면 영역을 최적화할 수 있습니다.
    components.html(html_content, height=850, scrolling=True)

  except Exception as e:
    st.error(f"HTML 파일을 불러오는 중 오류가 발생했습니다: {e}")
else:
  st.error(
      f"'{html_file_path}' 경로에서 파일을 찾을 수 없습니다. 깃허브"
      " 'htmls' 폴더 안에 'index.html' 파일이 정확히 업로드되었는지"
      " 확인해주세요."
  )
