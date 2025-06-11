# app.py
import streamlit as st
import json
from solar_analyzer import analyze_rooftop_image

def main():
    st.set_page_config(page_title="Solar AI Assistant", layout="wide")
    st.title("☀️ Solar Industry AI Assistant")
    st.write("Upload a satellite image of a rooftop to analyze its solar potential.")

    # Create two columns for a cleaner layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("1. Input Data")
        uploaded_file = st.file_uploader("Choose a satellite image...", type=["jpg", "jpeg", "png"])
        location = st.text_input("Property Location (e.g., 'San Diego, CA')", "San Diego, CA")
        electricity_cost = st.number_input("Your Current Electricity Cost ($/kWh)", min_value=0.01, max_value=1.00, value=0.15, step=0.01)
        
        analyze_button = st.button("Analyze Rooftop Potential", type="primary")

    with col2:
        st.subheader("2. Analysis Results")
        if uploaded_file is not None:
            st.image(uploaded_file, caption="Uploaded Rooftop Image.", use_column_width=True)
        else:
            st.info("Please upload an image to see the analysis here.")

    # Logic to run on button click
    if analyze_button and uploaded_file is not None:
        with st.spinner('AI is analyzing the rooftop... This may take a moment.'):
            # Read the image bytes from the uploaded file
            image_bytes = uploaded_file.getvalue()
            
            # Call the analysis function
            analysis_result = analyze_rooftop_image(image_bytes, location, electricity_cost)

        if "error" in analysis_result:
            st.error(f"An error occurred: {analysis_result['error']}")
        else:
            st.success("Analysis Complete!")
            with col2: # Display results in the second column
                st.subheader("2. Analysis Results")
                st.markdown(f"**Summary:** {analysis_result.get('summary', 'N/A')}")

                # Display metrics
                fin_est = analysis_result.get('financial_estimate', {})
                sys_rec = analysis_result.get('system_recommendation', {})
                st.metric("Estimated System Size", f"{sys_rec.get('estimated_system_size_kw', 'N/A')} kW")
                st.metric("Estimated Annual Savings", f"${fin_est.get('estimated_annual_savings_usd', 'N/A')}")
                st.metric("Payback Period", f"~{fin_est.get('simple_payback_period_years', 'N/A')} years")

                # Show the full JSON for transparency
                with st.expander("View Detailed JSON Response"):
                    st.json(analysis_result)

if __name__ == "__main__":
    main()