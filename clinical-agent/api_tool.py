import requests
from datetime import datetime


def calculate_duration(start, end):

    try:

        start_date = datetime.strptime(start, "%Y-%m-%d")

        end_date = datetime.strptime(end, "%Y-%m-%d")

        years = (end_date - start_date).days // 365

        return str(years) + " years"

    except:

        return None



def get_clinical_trials(disease):

    url = "https://clinicaltrials.gov/api/v2/studies"

    params = {
        "query.term": disease,
        "pageSize": 1
    }

    response = requests.get(url, params=params)

    data = response.json()

    studies = data.get("studies", [])

    if len(studies) == 0:

        return None


    study = studies[0]

    protocol = study.get("protocolSection", {})


    condition = protocol.get(
        "conditionsModule", {}
    ).get(
        "conditions", ["Unknown"]
    )[0]


    phase_list = protocol.get(
        "designModule", {}
    ).get(
        "phases", ["Unknown"]
    )


    sponsor = protocol.get(
        "sponsorCollaboratorsModule", {}
    ).get(
        "leadSponsor", {}
    ).get(
        "name", "Unknown"
    )


    # Dates

    status_module = protocol.get(
        "statusModule", {}
    )


    start_date = status_module.get(
        "startDateStruct", {}
    ).get(
        "date", None
    )


    completion_date = status_module.get(
        "completionDateStruct", {}
    ).get(
        "date", None
    )


    duration = calculate_duration(
        start_date,
        completion_date
    )


    return {

        "disease": condition,

        "trial_phase": phase_list[0],

        "company": sponsor,

        "duration": duration
    }