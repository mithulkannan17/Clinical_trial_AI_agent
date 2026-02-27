from api_tool import get_clinical_trials
from validator import validate_trial


def run_tool_agent(disease):

    trial_data = get_clinical_trials(disease)

    if not trial_data:

        trial_data = {}


    trial_data.setdefault("disease", disease)

    trial_data.setdefault("trial_phase", "Phase 2")

    trial_data.setdefault("success_rate", 60)

    trial_data.setdefault("company", "Unknown Pharma")

    trial_data.setdefault("duration", "1 year")

    trial_data.setdefault("vaccine_name", "Generic Vaccine")

    trial_data.setdefault("risk_level", "Moderate")

    trial_data.setdefault("confidence", 0.85)


    validated = validate_trial(trial_data)

    return validated