from pydantic import BaseModel


class ClinicalTrial(BaseModel):

    disease: str
    trial_phase: str
    success_rate: float
    company: str
    duration: str
    vaccine_name: str
    risk_level: str
    confidence: float


APPROVED_MEDICATIONS = [
    "Pfizer",
    "Moderna",
    "Covaxin",
    "Generic Vaccine",
    "Clinical Trial Drug"
]


def validate_trial(data):


    data.setdefault("success_rate", 50.0)
    data.setdefault("vaccine_name", "Generic Vaccine")
    data.setdefault("risk_level", "Moderate")
    data.setdefault("confidence", 0.8)
    data.setdefault("trial_phase", "Phase 2")
    data.setdefault("company", "Unknown")
    data.setdefault("duration", "1 year")
    data.setdefault("disease", "Unknown")



    data["success_rate"] = float(data["success_rate"])
    data["confidence"] = float(data["confidence"])



    if data["vaccine_name"] not in APPROVED_MEDICATIONS:

        data["vaccine_name"] = "Generic Vaccine"


    trial = ClinicalTrial(**data)

    return trial.dict()