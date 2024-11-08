class MedicalExpertSystem:
    def __init__(self):
        
        self.knowledge_base = {
            'Flu': ['fever', 'chills', 'fatigue', 'cough', 'body aches', 'headache'],
            'Cold': ['runny nose', 'sore throat', 'sneezing', 'cough', 'fatigue'],
            'COVID-19': ['fever', 'cough', 'shortness of breath', 'fatigue', 'loss of taste', 'loss of smell'],
            'Malaria': ['fever', 'chills', 'sweating', 'headache', 'fatigue', 'nausea'],
            'Stomach Flu': ['nausea', 'vomiting', 'diarrhea', 'fatigue', 'abdominal pain'],
        }
        self.possible_diseases = list(self.knowledge_base.keys())

    def get_user_input(self):
        """Get symptoms from the user."""
        symptoms = []
        print("Please answer the following questions (yes or no):")
        for symptom in ['fever', 'chills', 'fatigue', 'cough', 'body aches', 'headache', 'runny nose', 
                        'sore throat', 'sneezing', 'shortness of breath', 'loss of taste', 'loss of smell', 
                        'nausea', 'vomiting', 'diarrhea', 'abdominal pain']:
            answer = input(f"Do you have {symptom}? (yes/no): ").lower()
            if answer == 'yes':
                symptoms.append(symptom)
        return symptoms

    def diagnose(self, symptoms):
        """Diagnose based on the symptoms provided by the user."""
        if not symptoms:
            return "No symptoms provided, unable to diagnose."

        possible_diagnoses = []
        for disease in self.possible_diseases:
            matching_symptoms = set(symptoms) & set(self.knowledge_base[disease])
            if len(matching_symptoms) > 0:
                possible_diagnoses.append((disease, len(matching_symptoms)))

        if not possible_diagnoses:
            return "No matching diseases found. You may need to consult a doctor for further diagnosis."

        possible_diagnoses.sort(key=lambda x: x[1], reverse=True)

        best_match = possible_diagnoses[0]
        return f"Based on the symptoms, the most likely diagnosis is {best_match[0]}."
        
        possible_diagnoses.sort(key=lambda x: x[1], reverse=True)

        best_match = possible_diagnoses[0]
        return f"Based on the symptoms, the most likely diagnosis is {best_match[0]}."

   

   
    def run(self):
        """Run the expert system."""
        symptoms = self.get_user_input()
        diagnosis = self.diagnose(symptoms)
        print(diagnosis)



if __name__ == "__main__":
    system = MedicalExpertSystem()
    system.run()
    def run(self):
        """Run the expert system."""
        symptoms = self.get_user_input()
        diagnosis = self.diagnose(symptoms)
        print(diagnosis)

if __name__ == "__main__":
    system = MedicalExpertSystem()
    system.run()
