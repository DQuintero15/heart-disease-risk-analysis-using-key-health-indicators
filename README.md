# Heart Disease Risk Analysis Using Key Health Indicators: A Comprehensive Study with CDC 2022 Data

![Heart Disease](/images/heart-attack.png)

## Dataset

Data Source: [Indicators of Heart Disease (2022 UPDATE)](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease/data)

### Description

The Key Indicators of Heart Disease dataset is a 2022 CDC (Centers for Disease Control and Prevention) survey of over 400,000 U.S. adults, capturing various health-related factors tied to heart disease. The dataset focuses on major risk factors like high blood pressure, high cholesterol, and smoking, as well as other indicators such as diabetes, obesity, physical inactivity, and alcohol consumption. It comes from the CDC's Behavioral Risk Factor Surveillance System (BRFSS), a long-running health survey covering all U.S. states and territories.

## Variables

| **Variable**               | **Description**                                                                                                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **State**                   | State FIPS Code                                                                                                                      |
| **Sex**                     | Sex of Respondent                                                                                                                    |
| **GeneralHealth**           | Would you say that in general your health is:                                                                                         |
| **PhysicalHealthDays**      | For how many days during the past 30 days was your physical health not good?                                                          |
| **MentalHealthDays**        | For how many days during the past 30 days was your mental health not good?                                                            |
| **LastCheckupTime**         | About how long has it been since you last visited a doctor for a routine checkup?                                                     |
| **PhysicalActivities**      | During the past month, did you participate in any physical activities or exercises?                                                   |
| **SleepHours**              | On average, how many hours of sleep do you get in a 24-hour period?                                                                   |
| **RemovedTeeth**            | How many of your permanent teeth have been removed due to tooth decay or gum disease?                                                 |
| **HadHeartAttack**          | (Ever told) you had a heart attack (myocardial infarction)?                                                                           |
| **HadAngina**               | (Ever told) you had angina or coronary heart disease?                                                                                 |
| **HadStroke**               | (Ever told) you had a stroke?                                                                                                         |
| **HadAsthma**               | (Ever told) you had asthma?                                                                                                           |
| **HadSkinCancer**           | (Ever told) you had skin cancer that is not melanoma?                                                                                 |
| **HadCOPD**                 | (Ever told) you had C.O.P.D., emphysema, or chronic bronchitis?                                                                       |
| **HadDepressiveDisorder**   | (Ever told) you had a depressive disorder?                                                                                           |
| **HadKidneyDisease**        | (Ever told) you had kidney disease (excluding kidney stones, bladder infection, or incontinence)?                                     |
| **HadArthritis**            | (Ever told) you had arthritis, rheumatoid arthritis, gout, lupus, or fibromyalgia?                                                    |
| **HadDiabetes**             | (Ever told) you had diabetes?                                                                                                         |
| **DeafOrHardOfHearing**     | Are you deaf or do you have serious difficulty hearing?                                                                               |
| **BlindOrVisionDifficulty** | Are you blind or do you have serious difficulty seeing, even when wearing glasses?                                                    |
| **DifficultyConcentrating** | Do you have serious difficulty concentrating, remembering, or making decisions due to a physical, mental, or emotional condition?     |
| **DifficultyWalking**       | Do you have serious difficulty walking or climbing stairs?                                                                            |
| **DifficultyDressingBathing**| Do you have difficulty dressing or bathing?                                                                                          |
| **DifficultyErrands**       | Do you have difficulty doing errands alone due to a physical, mental, or emotional condition?                                         |
| **SmokerStatus**            | Four-level smoker status: Everyday smoker, Someday smoker, Former smoker, Non-smoker                                                  |
| **ECigaretteUsage**         | Have you ever used e-cigarettes or other electronic vaping products?                                                                  |
| **ChestScan**               | Have you ever had a CT or CAT scan of your chest area?                                                                                |
| **RaceEthnicityCategory**   | Five-level race/ethnicity category                                                                                                    |
| **AgeCategory**             | Fourteen-level age category                                                                                                           |
| **HeightInMeters**          | Reported height in meters                                                                                                            |
| **WeightInKilograms**       | Reported weight in kilograms                                                                                                         |
| **BMI**                     | Body Mass Index (BMI)                                                                                                                |
| **AlcoholDrinkers**         | Adults who reported having had at least one drink of alcohol in the past 30 days.                                                    |
| **HIVTesting**              | Adults who have ever been tested for HIV                                                                                              |
| **FluVaxLast12**            | Have you had a flu vaccine in the past 12 months?                                                                                     |
| **PneumoVaxEver**           | Have you ever had a pneumonia shot (pneumococcal vaccine)?                                                                            |
| **TetanusLast10Tdap**       | Have you received a tetanus shot in the past 10 years?                                                                                |
| **HighRiskLastYear**        | Have you engaged in high-risk behaviors in the past year?                                                                             |
| **CovidPos**                | Have you ever tested positive for COVID-19?                                                                                           |
