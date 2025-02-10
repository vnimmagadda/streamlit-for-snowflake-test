import streamlit as st

st.title("Hierarchical Data Viewer")

st.header("this is header")

st.subheader("subheader")
st.caption("caption")
st.write("this is write")
st.text("fixed text")
st.code("v = variable()\nanother_call()","python")
st.markdown("**bold**")
st.divider()
st.latex("..")

st.error("this is error")
st.info("this is info")
st.warning("this is warning")
st.success("this is success")

st.balloons()
st.snow
