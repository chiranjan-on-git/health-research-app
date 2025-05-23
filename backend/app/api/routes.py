'''
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test_route():
    return {"msg": "test works"}
'''
from fastapi import APIRouter, HTTPException
from app.models.schemas import ResearchFormPayload
from app.utils.prompt_builder import build_sonar_prompt
# from app.utils.response_parser import parse_sonar_response # We'll use this later
# from app.core.config import SONAR_API_KEY, SONAR_API_URL # For actual Sonar call
# import httpx # For making HTTP requests to Sonar API, install with: pip install httpx

router = APIRouter()

@router.post("/generate-research-prompt", response_model=str)
async def generate_research_prompt_endpoint(payload: ResearchFormPayload):
    """
    Receives research form data, builds a prompt for Sonar,
    (later will call Sonar API and parse response).
    For now, just returns the generated prompt.
    """
    try:
        prompt = build_sonar_prompt(payload)
        
        # Placeholder for future Sonar API call:
        # async with httpx.AsyncClient() as client:
        #     sonar_payload = {"engine": "sonar-small-chat", "query": prompt} # Example
        #     headers = {"Authorization": f"Bearer {SONAR_API_KEY}"}
        #     response = await client.post(SONAR_API_URL, json=sonar_payload, headers=headers)
        #     response.raise_for_status() # Raise an exception for bad status codes
        #     sonar_response_text = response.json().get("answer", "No answer from Sonar.") # Adjust based on actual Sonar API response structure

        # Placeholder for future parsing:
        # parsed_data = parse_sonar_response(sonar_response_text)
        # return parsed_data # This would return a dict, so response_model would change

        return prompt # For now, just return the prompt string
    except Exception as e:
        # Log the error e
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# Example response model if returning parsed data later:
# class ResearchResult(BaseModel):
#     summary: str
#     data: Optional[List[Dict]] = None
#     citations: Optional[List[str]] = None

# @router.post("/research", response_model=ResearchResult)
# ...
