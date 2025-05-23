from app.models.schemas import ResearchFormPayload # Import your schema

def build_sonar_prompt(payload: ResearchFormPayload) -> str:
    """
    Builds a structured natural language prompt from form data.
    """
    lang = payload.language or "English" # Use payload.language, default to English
    disease = payload.disease
    metric = payload.metric
    start_date = payload.start_date
    end_date = payload.end_date
    locations = payload.primary_locations
    
    compare_locations = payload.comparison_locations or []
    gender = payload.gender or []
    
    # Handle age_range carefully due to potential None or empty dict
    age_range_data = payload.age_range
    age_from = None
    age_to = None
    if age_range_data:
        age_from = age_range_data.from_age # Use from_age from schema
        age_to = age_range_data.to

    area_type = payload.area_type
    occupation = payload.occupation_group

    # Start base
    prompt = f"Give me the {metric.lower()} trends of {disease}"

    # Locations
    if compare_locations:
        prompt += f" in the following locations: {', '.join(locations)} and {', '.join(compare_locations)}"
    else:
        prompt += f" in {', '.join(locations)}"

    # Time
    prompt += f", from {start_date} to {end_date}"

    # Demographics
    if gender and "All" not in gender and "all" not in [g.lower() for g in gender]: # Case-insensitive "all" check
        prompt += f", for gender(s): {', '.join(gender)}"
    
    if age_from is not None and age_to is not None: # Check if age range values are set
        prompt += f", age between {age_from} and {age_to}"
    elif age_from is not None:
        prompt += f", age from {age_from}"
    elif age_to is not None:
        prompt += f", age up to {age_to}"

    if area_type and area_type.lower() != "both":
        prompt += f", living in {area_type.lower()} areas"
    
    if occupation:
        prompt += f", occupation group: {occupation}"

    # Language of results
    prompt += f". Present the results in {lang}." # Added language instruction

    prompt += " Please include any available charts or numbers, and cite your sources."

    return prompt