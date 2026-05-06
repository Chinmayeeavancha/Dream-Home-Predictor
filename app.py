import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# --- UI/UX CONFIGURATION ---
st.set_page_config(page_title="DreamHome Analytics", page_icon="🏡", layout="wide")

# Custom CSS to inject some clean UI/UX styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #2c3e50; font-family: 'Inter', sans-serif; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #0e75b6; color: white; }
    .stButton>button:hover { background-color: #0b5e92; }
    .metric-card { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD DATA & MODEL ---
@st.cache_data
def load_data():
    return pd.read_csv('real_estate_data.csv')

@st.cache_resource
def load_model():
    return joblib.load('house_price_model.pkl')

try:
    df = load_data()
    model = load_model()
except FileNotFoundError:
    st.error("⚠️ Data or Model not found. Please run generate_data.py and train_model.py first!")
    st.stop()

# --- APP LAYOUT ---
st.title("🏡 DreamHome Analytics & Price Predictor")
st.markdown("A data-driven approach to real estate. Explore market trends and predict property values instantly.")

# Create tabs for better UX navigation
tab1, tab2 = st.tabs(["📊 Market Insights (EDA)", "🔮 Price Predictor"])

# --- TAB 1: DATA ANALYSIS ---
with tab1:
    st.header("Real Estate Market Overview")
    
    # Top Level Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Average Home Price", f"${df['Price'].mean():,.0f}")
    col2.metric("Average Sq. Footage", f"{df['Square_Feet'].mean():,.0f} sqft")
    col3.metric("Total Properties Analyzed", f"{len(df)}")
    
    st.markdown("---")
    
    # Visualizations
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("Price vs. Square Footage")
        fig1 = px.scatter(df, x="Square_Feet", y="Price", color="Location_Score", 
                          color_continuous_scale="Viridis", opacity=0.7)
        fig1.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig1, use_container_width=True)
        
    with col_chart2:
        st.subheader("Price Distribution by Bedrooms")
        fig2 = px.box(df, x="Bedrooms", y="Price", color="Bedrooms")
        fig2.update_layout(plot_bgcolor="rgba(0,0,0,0)", showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)

# --- TAB 2: PRICE PREDICTOR ---
with tab2:
    st.header("Predict Your Property's Value")
    st.markdown("Enter property details below to get an AI-powered price estimate.")
    
    col_input, col_result = st.columns([1, 1.5])
    
    with col_input:
        st.markdown("### Property Details")
        sqft = st.number_input("Square Footage", min_value=500, max_value=10000, value=2000, step=100)
        beds = st.slider("Bedrooms", min_value=1, max_value=10, value=3)
        baths = st.slider("Bathrooms", min_value=1, max_value=6, value=2)
        age = st.number_input("Property Age (Years)", min_value=0, max_value=100, value=10)
        location = st.slider("Location Score (1=Poor, 10=Excellent)", min_value=1, max_value=10, value=7)
        
        predict_btn = st.button("Calculate Value 🚀")
        
    with col_result:
        if predict_btn:
            # Create input dataframe
            input_data = pd.DataFrame({
                'Square_Feet': [sqft],
                'Bedrooms': [beds],
                'Bathrooms': [baths],
                'Age_Years': [age],
                'Location_Score': [location]
            })
            
            # Predict
            prediction = model.predict(input_data)[0]
            
            # Display result with nice UI
            st.markdown(f"""
            <div style="background-color: #e8f4f8; padding: 30px; border-radius: 15px; text-align: center; border: 2px solid #0e75b6;">
                <h3 style="color: #2c3e50; margin-bottom: 0;">Estimated Property Value</h3>
                <h1 style="color: #0e75b6; font-size: 48px; margin-top: 10px;">${prediction:,.2f}</h1>
                <p style="color: #666; font-size: 14px;">Based on our machine learning algorithm analyzing local market trends.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("👈 Adjust the sliders on the left and click 'Calculate Value' to see the prediction.")
