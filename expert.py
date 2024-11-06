class MedicalExpertSystem:
    def __init__(self):
        self.symptoms = []
        self.diagnosis_rules = {
            'cold': ['cough', 'sore throat', 'runny nose', 'congestion', 'sneezing'],
            'flu': ['fever', 'chills', 'muscle aches', 'fatigue', 'sore throat', 'cough'],
            'covid-19': ['fever', 'cough', 'shortness of breath', 'fatigue', 'loss of taste', 'loss of smell'],
            'allergy': ['sneezing', 'itchy eyes', 'runny nose', 'congestion'],
            'migraine': ['headache', 'nausea', 'sensitivity to light', 'blurred vision'],
            'diabetes': ['frequent urination', 'excessive thirst', 'extreme fatigue', 'blurry vision', 'weight loss']
        }

    def get_symptoms(self):
        print("Please enter your symptoms (type 'done' when finished):")
        while True:
            symptom = input("Enter symptom: ").strip().lower()
            if symptom == 'done':
                break
            self.symptoms.append(symptom)

    def diagnose(self):
        potential_diagnosis = []
        for disease, disease_symptoms in self.diagnosis_rules.items():
            matching_symptoms = set(self.symptoms).intersection(set(disease_symptoms))
            match_percentage = (len(matching_symptoms) / len(disease_symptoms)) * 100
            if match_percentage > 0:
                potential_diagnosis.append((disease, match_percentage, matching_symptoms))
        if potential_diagnosis:
            potential_diagnosis.sort(key=lambda x: x[1], reverse=True)
            print("\nPotential Diagnoses (with matching symptoms):")
            for diagnosis, percentage, symptoms in potential_diagnosis:
                print(f"\nDisease: {diagnosis.capitalize()}")
                print(f"Match: {percentage:.2f}%")
                print(f"Matching symptoms: {', '.join(symptoms)}")
        else:
            print("No potential diagnosis found. Please consult a doctor.")

def main():
    system = MedicalExpertSystem()
    system.get_symptoms()
    system.diagnose()

if __name__ == "__main__":
    main()
