from pydantic import BaseModel
from typing import Optional


class ClinicalTrial(BaseModel):

    disease: str

    trial_phase: Optional[str]

    success_rate: Optional[float]

    company: Optional[str]

    vaccine_name: Optional[str]

    duration: Optional[str]

    risk_level: Optional[str]

    confidence: Optional[float]