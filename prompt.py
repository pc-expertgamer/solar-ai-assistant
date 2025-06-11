# prompt.py

def get_solar_analysis_prompt(location, electricity_cost_kwh):
    # We use an f-string to inject context (location, cost) into the prompt.
    # This addresses the "Context Management: Multi-source data handling" requirement.
    
    return f"""
    You are an expert solar installation analyst. Your task is to analyze the provided satellite image of a rooftop and provide a detailed solar potential assessment.

    **Context:**
    - Property Location: {location}
    - Average Electricity Cost: ${electricity_cost_kwh:.2f}/kWh

    **Analysis Requirements:**
    Based *only* on the visual information in the image and the context provided, perform the following analysis.

    1.  **Rooftop Analysis:**
        - Identify the total usable rooftop area for solar panels, excluding obstructions like vents, chimneys, and skylights.
        - Analyze the primary orientation (e.g., South-facing, South-West facing) of the usable roof planes.
        - Assess potential shading from nearby trees, buildings, or other structures visible in the image.

    2.  **System Recommendation:**
        - Recommend the type of solar panel (e.g., Monocrystalline, Polycrystalline) suitable for this roof. Assume standard modern panels.
        - Estimate the maximum number of standard-sized panels (approx. 1.7m x 1.0m) that could fit on the usable area.
        - Calculate the estimated system size in kilowatts (kW), assuming an average panel wattage of 400W.

    3.  **Financial & ROI Estimate:**
        - Provide a rough estimate of the total installation cost. Assume a cost of $2.50 per watt.
        - Estimate the annual energy production in kWh. Assume 1,300 peak sun hours per year for the estimated system size.
        - Calculate the estimated annual savings based on the provided electricity cost.
        - Estimate the simple payback period in years. Mention that local incentives and tax credits could shorten this period but are not included in this calculation.

    4.  **Confidence Score:**
        - Provide a confidence score (0-100) for your analysis, based on the clarity of the image and the visibility of the rooftop.

    **Output Format:**
    Provide your entire response as a single, valid JSON object. Do not include any text or explanations outside of the JSON structure. The JSON object must have the following keys:

    {{
      "rooftop_analysis": {{
        "usable_area_sq_meters": "...",
        "main_orientation": "...",
        "shading_analysis": "..."
      }},
      "system_recommendation": {{
        "panel_type_recommendation": "...",
        "max_panel_count": "...",
        "estimated_system_size_kw": "..."
      }},
      "financial_estimate": {{
        "estimated_installation_cost_usd": "...",
        "estimated_annual_production_kwh": "...",
        "estimated_annual_savings_usd": "...",
        "simple_payback_period_years": "..."
      }},
      "confidence_score": "...",
      "summary": "A brief, one-paragraph summary of the findings."
    }}
    """