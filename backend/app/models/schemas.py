from pydantic import BaseModel
from typing import List, Optional, Dict

class AgeRange(BaseModel):
    from_age: Optional[int] = None # Renamed from 'from' as 'from' is a Python keyword
    to: Optional[int] = None

class ResearchFormPayload(BaseModel):
    language: Optional[str] = "English"
    primary_locations: List[str]
    comparison_locations: Optional[List[str]] = []
    disease: str
    metric: str # e.g., "Cases", "Deaths", "Risk"
    start_date: str # Consider using date type if validation is needed, e.g., date from datetime
    end_date: str   # Consider using date type
    predefined_range: Optional[str] = None # e.g., "Last 7 days", "Last Month" - we'll handle this later
    
    # Demographics
    population_scope: Optional[str] = "Entire" # "Entire" / "Filtered"
    gender: Optional[List[str]] = [] # Could be "Male", "Female", "Other", "All"
    age_range: Optional[AgeRange] = {}
    occupation_group: Optional[str] = None
    area_type: Optional[str] = None # "Urban" / "Rural" / "Both"

    # Output Preferences (Not directly used in prompt_builder based on your current spec, but good to have)
    output_components: Optional[List[str]] = ["Summary", "Graphs", "Tables"]
    chart_style: Optional[List[str]] = ["Line"]
    granularity_level: Optional[str] = "Country"

    # Advisories (Also not directly in current prompt_builder, but part of form)
    show_recent_advisories: Optional[bool] = False
    include_prevention_tips: Optional[bool] = False
    show_public_campaigns: Optional[bool] = False

    # Note: Citations are automatic, so not part of the input payload.