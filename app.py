import streamlit as st
import pandas as pd
import io, statistics, ast

PORTFOLIO_INFO = {
    "name": "Maryam Imdad",
    "from": "Gujranwala, Pakistan",
    "field": "BS Data Science & Data Analytics",
    "skills": ["Python", "Streamlit", "Data Analysis", "Pandas"],
}

def portfolio_info(): return PORTFOLIO_INFO

def analyze_csv_data(csv_text):
    df = pd.read_csv(io.StringIO(csv_text))
    return {"rows": df.shape[0], "columns": df.shape[1], "column_names": df.columns.tolist(), "preview": df.head().to_dict(orient="records")}

def python_code_explainer(python_code):
    try:
        tree = ast.parse(python_code)
        return f"Code mein {len(tree.body)} statements hain."
    except Exception as e: return f"Error: {e}"

def calculate_stats(numbers):
    return {"mean": statistics.mean(numbers), "median": statistics.median(numbers), "mode": statistics.mode(numbers)}

st.set_page_config(page_title="Maryam's MCP Tool Server", page_icon="✨", layout="wide")
st.markdown("""<style>.hero{padding:2rem;border-radius:20px;color:white;background:linear-gradient(115deg,#5b21b6,#0f766e);}</style><div class="hero"><h1>Maryam's MCP Tool Server</h1><p>Explore practical AI-ready tools</p></div>""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## ✨ Maryam Imdad\n📍 Gujranwala\n🎓 BS Data Science")

tab1, tab2, tab3, tab4 = st.tabs(["👩‍💻 Portfolio", "📁 CSV", "🐍 Code", "📈 Stats"])
with tab1:
    if st.button("Show Portfolio", type="primary"):
        st.json(portfolio_info()); st.balloons()
with tab2:
    f=st.file_uploader("Upload CSV", type=["csv"])
    if f: st.json(analyze_csv_data(f.getvalue().decode("utf-8-sig")))
with tab3:
    code=st.text_area("Paste Python code")
    if st.button("Explain Code"): st.info(python_code_explainer(code))
with tab4:
    nums=st.text_input("Numbers like: 10,20,20,30")
    if st.button("Calculate Stats"):
        if nums:
            n=[float(x.strip()) for x in nums.split(",")]
            st.json(calculate_stats(n))