import re

comorbidities_translations = {
    "затлъстяване": "obesity",
    "сърдечно": "cardiovascular disease",
    "белодробно": "lung disease",
    "пневмония": "pneumonia",
    "диабет": "diabetes",
    "неврологично": "neurological condition",
    "онкологично": "cancer",
    "хематологично": "hematological disease",
    "бъбречно": "kidney disease",
    "чернодробно": "liver disease",
    "астма": "asthma",
    "неуточнено към момента заболяване": "unknown disease",
    "множество придружаващи": "multiple diseases"
}


def parse_comorbidities(text):
    if "няма информация" in text or "липсва информация" in text or "не са въведени" in text:
        return None
    else:
        comorbidities = []
        for key in comorbidities_translations.keys():
            if key in text:
                comorbidities.append(comorbidities_translations[key])
        return comorbidities

def augment_deaths_stats(deaths, cases):
    deaths["sex"] = deaths["text"].apply(lambda text: "male" if "мъж" in text else "female" if "жена" in text else None)
    deaths["age"] =  deaths["text"].apply(lambda text: int(re.findall("^(мъж|жена) на (\d+)", text)[0][1]))
    deaths["comorbidities"] = deaths["text"].apply(parse_comorbidities)
    
    age_groups = list(cases["age_group"])
    age_group_map = lambda age: age_groups[0] if age < 20 else age_groups[-1] if age >= 90 else age_groups[int((age - 10)/10)]
    deaths["age_group"] = deaths["age"].apply(age_group_map)   
    return deaths