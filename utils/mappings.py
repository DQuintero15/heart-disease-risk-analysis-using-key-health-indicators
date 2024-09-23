mappings = {
    "Sex": {"Female": 0, "Male": 1},
    "GeneralHealth": {"Excellent": 0, "Very good": 1, "Good": 2, "Fair": 3, "Poor": 4},
    "LastCheckupTime": {
        "Within past year (anytime less than 12 months ago)": 1,
        "Within past 2 years (1 year but less than 2 years ago)": 2,
        "Within past 5 years (2 years but less than 5 years ago)": 3,
        "5 or more years ago": 4,
    },
    "HadDiabetes": {
        "Yes": 1,
        "Yes, but only during pregnancy (female)": 2,
        "No": 3,
        "No, pre-diabetes or borderline diabetes": 4,
    },
    "SmokerStatus": {
        "Current smoker - now smokes every day": 1,
        "Current smoker - now smokes some days": 2,
        "Former smoker": 3,
        "Never smoked": 4,
    },
    "ECigaretteUsage": {
        "Never used e-cigarettes in my entire life": 1,
        "Use them every day": 2,
        "Use them some days": 3,
        "Not at all (right now)": 4,
    },
    "AgeCategory": {
        "Age 18 to 24": 1,
        "Age 25 to 29": 2,
        "Age 30 to 34": 3,
        "Age 35 to 39": 4,
        "Age 40 to 44": 5,
        "Age 45 to 49": 6,
        "Age 50 to 54": 7,
        "Age 55 to 59": 8,
        "Age 60 to 64": 9,
        "Age 65 to 69": 10,
        "Age 70 to 74": 11,
        "Age 75 to 79": 12,
        "Age 80 or older": 13,
    },
    "CovidPos": {
        "Yes": 1,
        "No": 2,
        "Tested positive using home test without a health professional": 3,
    },
    "Boolean": {"Yes": 1, "No": 0},
}
