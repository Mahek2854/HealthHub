import streamlit as st
import joblib
import numpy as np


def authenticate_user(username, password):
    if username in user_database:
        if user_database[username]["password"] == password:
            return True
    return False

def predictDiseases(symptoms):
    final_svm_model = joblib.load('final_svm_model.pkl')
    encoder = joblib.load('encoder.pkl')
    data_dict = joblib.load('data_dict.pkl')

    symptoms = symptoms.split(",")
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        if symptom in data_dict["symptom_index"]:
            index = data_dict["symptom_index"][symptom]
            input_data[index] = 1
        else:
            st.warning(f"Warning: Symptom '{symptom}' not found in data dictionary.")

    input_data = np.array(input_data).reshape(1,-1)
    svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(input_data)[0]]

    return svm_prediction

def Preventive_measures_Arthritis():
    st.title("Preventive Measures and Resources for Arthritis")

    st.markdown("<h2 style='color: teal;'>Diet Recommendations for Joint Health</h2>", unsafe_allow_html=True)
    st.subheader("Anti-inflammatory Diet:")
    st.markdown(
        """
        Focus on consuming foods that help reduce inflammation in the body. 
        This includes foods rich in omega-3 fatty acids (such as salmon, walnuts, and flaxseeds), 
        fruits and vegetables high in antioxidants (such as berries, spinach, and kale), 
        and spices like turmeric and ginger known for their anti-inflammatory properties.
        """
    )

    st.subheader("Balanced Diet:")
    st.markdown(
        """
        Maintain a balanced diet that includes a variety of nutrients necessary for joint health. 
        This includes adequate protein intake to support muscle strength and repair, 
        as well as sufficient calcium and vitamin D for bone health. 
        Whole grains, lean proteins, healthy fats, and plenty of fruits and vegetables should be staples of your diet.
        """
    )

    st.subheader("Hydration:")
    st.markdown(
        """
        Stay hydrated by drinking plenty of water throughout the day. 
        Proper hydration helps lubricate the joints and supports overall joint health. 
        Limit consumption of sugary drinks and excessive caffeine, 
        as they may contribute to inflammation and dehydration.
        """
    )
    st.write("\n")
    st.markdown("---")

    st.markdown("<h2 style='color: teal;'>Workout Routines for Joint Health</h2>", unsafe_allow_html=True)
    st.subheader("Low-Impact Exercises:")
    st.markdown(
        """
        Engage in low-impact exercises that are gentle on the joints but still effective for improving flexibility,
        strength, and cardiovascular health. Examples include swimming, water aerobics, cycling, tai chi, and yoga. 
        These exercises help increase range of motion, reduce stiffness, and improve overall joint function without placing excessive stress on the joints.
        """
    )

    st.subheader("Strength Training:")
    st.markdown(
        """
        Incorporate strength training exercises into your routine to build muscle strength and support the joints.
        Focus on exercises that target the muscles around the affected joints, such as leg lifts, arm curls, and shoulder presses.
        Start with light weights and gradually increase resistance as tolerated.
        """
    )

    st.subheader("Stretching and Flexibility Exercises:")
    st.markdown(
        """
        Perform regular stretching and flexibility exercises to maintain joint mobility and prevent stiffness.
        Focus on gentle stretches for all major muscle groups, paying particular attention to areas affected by arthritis.
        Stretching can help improve joint range of motion, reduce pain, and enhance overall mobility.
        """
    )
    st.write("\n")
    st.markdown("---")

    st.markdown("<h2 style='color: teal;'>Website Recommendations to Know More</h2>", unsafe_allow_html=True)
    st.subheader("Arthritis Foundation:")
    st.markdown(
        """
        [Arthritis Foundation](https://www.arthritis.org/): The Arthritis Foundation offers a wealth of information on arthritis management, 
        including diet and exercise tips, resources for living with arthritis, and community support forums.
        """
    )

    st.subheader("Mayo Clinic - Arthritis:")
    st.markdown(
        """
        [Mayo Clinic - Arthritis](https://www.mayoclinic.org/diseases-conditions/arthritis): Mayo Clinic provides comprehensive information on arthritis,
        including diagnosis, treatment options, lifestyle recommendations, and expert insights.
        """
    )

    st.subheader("National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIAMS):")
    st.markdown(
        """
        [National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIAMS)](https://www.niams.nih.gov/): NIAMS offers research-based information on arthritis and related conditions, including dietary guidelines,
        exercise recommendations, and resources for patients and healthcare professionals.
        """
    )
    st.write("\n")
    st.markdown("---")

    st.markdown("<h2 style='color: teal;'>Medical Assistance</h2>", unsafe_allow_html=True)
    st.subheader("Arthritis.org - Understanding When Joint Pain Means It's Time:")
    st.markdown(
        """
        [Arthritis Medical Assistance](https://www.arthritis.org/health-wellness/about-arthritis/understanding-arthritis/when-joint-pain-means-its-time)
        """
    )
    
    
    
    
    
    



def Preventive_measures_Diabetes():
    st.title("Preventive Measures and Resources for Diabetes")

    st.markdown("<h2 style='color: teal;'>Diet Recommendations for Diabetes:</h2>", unsafe_allow_html=True)
    st.subheader("Balanced Macronutrient Intake:")
    st.markdown(
        """
        Encourage a balanced diet that includes carbohydrates, proteins,
          and healthy fats in appropriate proportions. Emphasize whole grains, lean proteins, fruits, vegetables,
            and healthy fats such as those found in nuts, seeds, and olive oil.

        """
    )

    st.subheader("Portion Control: ")
    st.markdown(
        """
        Educate individuals about portion sizes and encourage them to monitor their food intake to avoid overeating.
          Portion control can help regulate blood sugar levels and support weight management.

        """
    )

    st.subheader("Regular Meal Timing: ")
    st.markdown(
        """
        Encourage consistent meal timing with regular intervals between meals to help stabilize blood sugar levels throughout the day.
          Consistency in meal timing can also support insulin sensitivity.
        """
    )
    st.write("\n")
    st.markdown("---")

    st.markdown("<h2 style='color: teal;'>Workout Routines for Diabetes</h2>", unsafe_allow_html=True)
    st.subheader("Aerobic Exercise: ")
    st.markdown(
        """
        Include aerobic exercises such as brisk walking, cycling, swimming, or dancing in the workout routine.
          Aerobic exercises help improve cardiovascular health, increase insulin sensitivity, and manage blood sugar levels.
        """
    )

    st.subheader("Strength Training:")
    st.markdown(
        """
        Incorporate resistance training or strength training exercises using weights, resistance bands,
          or bodyweight exercises. Strength training builds muscle mass, which can enhance glucose metabolism and improve insulin sensitivity.
        """
    )

    st.subheader("Stretching and Flexibility Exercises:")
    st.markdown(
        """
        Include activities that improve flexibility, balance, and mobility, such as yoga, tai chi, or Pilates.
          These exercises can help reduce stress, improve circulation, and support overall well-being.
        """
    )
    st.write("\n")
    st.markdown("---")

    st.markdown("<h2 style='color: teal;'>Website Recommendations to Know More</h2>", unsafe_allow_html=True)
    st.subheader("American Diabetes Association (ADA):")
    st.markdown(
        """
        [ADA Website](https://www.diabetes.org/): The ADA website provides comprehensive information on diabetes management,
          including diet, exercise, medication, and lifestyle tips. It offers resources, recipes, and educational materials for individuals with diabetes.

        """
    )

    st.subheader("Joslin Diabetes Center:")
    st.markdown(
        """
        [Joslin Diabetes Center Website](https://www.joslin.org/):The Joslin Diabetes Center is a renowned institution specializing in diabetes research, education, and clinical care.
           Their website offers valuable resources, articles, and tools for diabetes management, including diet and exercise guidelines.

        """
    )

    st.subheader("Diabetes.co.uk:")
    st.markdown(
        """
        [Diabetes.co.uk Website](https://www.diabetes.co.uk/): This website provides a wealth of information on diabetes,
          including diet plans, exercise tips, forums, and community support. It offers practical advice and resources for people living with diabetes to improve their health and well-being.
        """
    )
    st.write("\n")
    st.markdown("---")

    st.markdown("<h2 style='color: teal;'>Medical Assistance</h2>", unsafe_allow_html=True)
    st.subheader("MediBuddy - Online Diabetologist Consultation:")
    st.markdown(
        """
        [Diabetes Medical Assistance](https://www.medibuddy.in/doctors/online-consultation/diabetologist)
        """
    )
def Preventive_measures_Migrane():
        st.title("Preventive Measures and Resources for Migrane")

        st.markdown("<h2 style='color: teal;'>Diet Recommendations for Migrane:</h2>", unsafe_allow_html=True)
        st.subheader("Hydration:")
        st.markdown(
            """
            Drink plenty of water throughout the day to stay hydrated. Dehydration can trigger migraines in some individuals,
            so maintaining adequate hydration levels is essential.
            """
        )
        st.subheader("Balanced Diet: ")
        st.markdown(
            """
            Follow a balanced diet rich in fruits, vegetables, whole grains, and lean proteins.
            Avoid skipping meals, as low blood sugar levels can also trigger migraines in some people.
            """
        )
        st.subheader("Identify Trigger Foods:")
        st.markdown(
            """
            Keep a food diary to identify any potential trigger foods that may exacerbate migraine symptoms.
            Common trigger foods include aged cheeses, processed meats, caffeine, alcohol, and artificial sweeteners.
            Avoiding or minimizing consumption of these trigger foods may help reduce migraine frequency.
            """
        )
        st.write("\n")
        st.markdown("---")

        st.markdown("<h2 style='color: teal;'>Workout Routines for Migrane</h2>", unsafe_allow_html=True)
        st.subheader("Low-Impact Cardio: ")
        st.markdown(
            """
            Engage in low-impact cardiovascular exercises such as walking, swimming, or cycling.
            These exercises help improve blood circulation and release endorphins, which can help alleviate migraine symptoms.
            """
        )

        st.subheader("Yoga and Stretching: ")
        st.markdown(
            """
            Practice yoga poses and stretching exercises that focus on relaxation and stress reduction.
            Yoga can help improve flexibility, reduce muscle tension, and promote relaxation, which may help prevent migraines triggered by stress.
            """
        )

        st.subheader("Breathing Exercises: ")
        st.markdown(
            """
            Incorporate deep breathing exercises and meditation into your daily routine. Deep breathing techniques can help calm the mind,
            reduce anxiety, and alleviate tension, which are common triggers for migraines.
            """
        )
        st.write("\n")
        st.markdown("---")

        st.markdown("<h2 style='color: teal;'>Website Recommendations to Know More</h2>", unsafe_allow_html=True)
        st.subheader("American Migraine Foundation:")
        st.markdown(
            """
            [American Migraine Foundation](https://americanmigrainefoundation.org/): The American Migraine Foundation offers comprehensive information on migraine prevention,
            treatment options, lifestyle management, and patient resources.
            """
        )

        st.subheader("Migraine.com:")
        st.markdown(
            """
            [Migraine.com](https://migraine.com/): Migraine.com provides a wealth of articles, forums, and community support for individuals living with migraines.
            It offers insights into managing migraine symptoms through lifestyle changes, diet, and exercise.
            """
        )

        st.subheader("National Headache Foundation: ")
        st.markdown(
            """
            [National Headache Foundation: ](https://headaches.org/): The National Headache Foundation is a non-profit organization dedicated to providing education,
            research, and support for individuals affected by headaches and migraines. Their website offers resources on migraine prevention, treatment, and lifestyle management.
            """
        )
        st.write("\n")
        st.markdown("---")

        st.markdown("<h2 style='color: teal;'>Medical Assistance</h2>", unsafe_allow_html=True)
        st.subheader("MediBuddy - Online Neurologist Consultation for Migraine:")
        st.markdown(
            """
            [Migrane Medical Assistance](https://www.medibuddy.in/doctors/online-consultation/neurologist/migraine)
            """
        )
           
        
        
        
def Preventive_measures_Hypertension():
        st.title("Preventive Measures and Resources for Hypertension")

        st.markdown("<h2 style='color: teal;'>Diet Recommendations for Hypertension:</h2>", unsafe_allow_html=True)
        st.subheader(" DASH Diet (Dietary Approaches to Stop Hypertension):")
        st.markdown(
            """
            The DASH diet emphasizes fruits, vegetables, whole grains, lean proteins, and low-fat dairy products.
            It encourages reducing sodium intake and limiting foods high in saturated fats and cholesterol.
            Aim to include plenty of potassium-rich foods such as bananas, spinach, and sweet potatoes.
            """
        )
        st.subheader("Mediterranean Diet:")
        st.markdown(
            """
            The Mediterranean diet focuses on whole, unprocessed foods such as fruits, vegetables, fish, nuts, and olive oil.
            It promotes moderate consumption of red wine and limits intake of processed foods, red meat, and sweets.
            Incorporate foods rich in omega-3 fatty acids, such as salmon, flaxseeds, and walnuts.
            """
        )
        st.subheader("Low-Sodium Diet:")
        st.markdown(
            """
            Reduce the amount of salt in your diet by avoiding processed foods, canned soups, and salty snacks.
            Use herbs, spices, lemon juice, and vinegar to add flavor to meals instead of salt.
            Read food labels carefully and choose low-sodium or sodium-free options whenever possible.
            """
        )
        st.write("\n")
        st.markdown("---")

        st.markdown("<h2 style='color: teal;'>Workout Routines for Hypertension</h2>", unsafe_allow_html=True)
        st.subheader("Aerobic Exercise:")
        st.markdown(
            """
            Engage in moderate-intensity aerobic activities such as brisk walking, cycling, swimming, or dancing.
            Aim for at least 150 minutes of aerobic exercise per week, spread out over several days.
            Gradually increase the duration and intensity of your workouts as your fitness improves.

            """
        )

        st.subheader("Strength Training: ")
        st.markdown(
            """
            Incorporate resistance training exercises using weights, resistance bands, or bodyweight exercises.
            Focus on working major muscle groups, such as the chest, back, legs, and arms, with compound exercises like squats, lunges, push-ups, and rows.
            Perform strength training exercises 2-3 times per week, allowing for adequate rest between sessions.
            """
        )

        st.subheader("Yoga and Mindfulness Practices:")
        st.markdown(
            """
            Practice yoga, tai chi, or qigong to promote relaxation, reduce stress, and improve flexibility and balance.
            Incorporate deep breathing exercises, meditation, or mindfulness techniques into your daily routine to manage stress and promote overall well-being.
            Aim for consistency in your practice, gradually increasing the duration and intensity of your sessions.
            """
        )
        st.write("\n")
        st.markdown("---")

        st.markdown("<h2 style='color: teal;'>Website Recommendations to Know More</h2>", unsafe_allow_html=True)
        st.subheader("MedlinePlus - High Blood Pressure (Hypertension):")
        st.markdown(
            """
            [MedlinePlus: ](https://medlineplus.gov/ency/article/000468.htm):MedlinePlus is a trusted resource from the National Library of Medicine and the National Institutes of Health (NIH)
            that provides authoritative information on various health topics. This specific link leads to an article on high blood pressure (hypertension), offering comprehensive information
                on its causes, symptoms, diagnosis, treatment options, and preventive measures.
            """
        )

        st.subheader("Healthline- High Blood Pressure (Hypertension):")
        st.markdown(
            """
            [Healthline](https://www.healthline.com/health/high-blood-pressure-hypertension):Healthline is a reputable health information website that offers comprehensive resources on various medical conditions.
            This specific link leads to an article on high blood pressure (hypertension), providing valuable insights into its causes, symptoms, risk factors, diagnosis, treatment options, and lifestyle management strategies.
            """
        )

        st.subheader("NHS - High Blood Pressure (Hypertension):")
        st.markdown(
            """
            [The NHS (National Health Service)](https://www.nhs.uk/conditions/high-blood-pressure-hypertension/):The NHS (National Health Service) is the primary healthcare provider in the United Kingdom, offering comprehensive
            information and services to the public. This link leads to an NHS webpage dedicated to high blood pressure (hypertension), providing valuable information on its causes, symptoms, diagnosis, treatment options, and preventive measures.
            """
        )
        st.write("\n")
        st.markdown("---")

        st.markdown("<h2 style='color: teal;'>Medical Assistance</h2>", unsafe_allow_html=True)
        st.subheader("MediBuddy - Online General Physician Consultation for Blood Pressure:")
        st.markdown(
            """
            [Hypertension Medical Assistance](https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/diagnosis-treatment/drc-20373417)
            """
        )    
        
        
        
        
        
        
        
        
        
        
        
def Preventive_measures_HeartDisease():
    st.title("Preventive Measures and Resources for HeartDisease")

    st.markdown("<h2 style='color: teal;'>Diet Recommendations for HeartDisease:</h2>", unsafe_allow_html=True)
    st.subheader("Mediterranean Diet:")
    st.markdown(
        """
        Focuses on fruits, vegetables, whole grains, nuts, seeds, and healthy fats like olive oil.
        Includes moderate consumption of fish, poultry, and dairy products.
        Limits red meat and processed foods.
        Emphasizes herbs and spices for flavor instead of salt.
        """
    )
    st.subheader("DASH Diet (Dietary Approaches to Stop Hypertension):")
    st.markdown(
        """
        High in fruits, vegetables, whole grains, and low-fat dairy products.
        Encourages lean protein sources such as poultry, fish, and legumes.
        Restricts sodium intake to help lower blood pressure.
        Promotes moderation in sugar-sweetened beverages and red meat consumption.
        """
    )
    st.subheader("Plant-Based Diet:")
    st.markdown(
        """
        Centers around foods derived from plants, such as fruits, vegetables, whole grains, nuts, seeds, and legumes.
        Includes minimal or no animal products, which may help lower cholesterol levels and reduce the risk of heart disease.
        Rich in fiber, antioxidants, and phytonutrients that support heart health.
        """
    )
    st.write("\n")
    st.markdown("---")

    st.markdown("<h2 style='color: teal;'>Workout Routines for HeartDisease</h2>", unsafe_allow_html=True)
    st.subheader("Aerobic Exercises:")
    st.markdown(
        """
        Engage in aerobic activities such as brisk walking, jogging, cycling, swimming, or dancing.
        Aim for at least 150 minutes of moderate-intensity aerobic exercise or 75 minutes of vigorous-intensity exercise per week.
        Aerobic exercises help improve cardiovascular fitness, lower blood pressure, and manage weight.
        """
    )

    st.subheader("Strength Training: ")
    st.markdown(
        """
        Incorporate strength training exercises using resistance bands, free weights, or weight machines.
        Focus on major muscle groups such as legs, chest, back, abdomen, arms, and shoulders.
        Perform strength training exercises 2-3 times per week to build muscle strength and endurance, which can improve overall heart health.
        """
    )

    st.subheader("Yoga and Mindfulness Practices:")
    st.markdown(
        """
        Practice yoga, tai chi, or qigong to reduce stress, improve flexibility, and promote relaxation.
        Include breathing exercises, meditation, and mindfulness techniques to manage stress and enhance mental well-being.
        Regular practice of mind-body exercises can help lower blood pressure, reduce inflammation, and support heart health.
        """
    )
    st.write("\n")
    st.markdown("---")

    st.markdown("<h2 style='color: teal;'>Website Recommendations to Know More</h2>", unsafe_allow_html=True)
    st.subheader("American Heart Association (AHA):")
    st.markdown(
        """
        [American Heart Association (AHA):](http://www.heart.org):Provides comprehensive information on heart diseases, prevention strategies,
          healthy lifestyle tips, and resources for patients and caregivers.
        """
    )

    st.subheader("Mayo Clinic - Heart Disease and Cardiovascular Health:")
    st.markdown(
        """
        [Mayo Clinic](http://www.mayoclinic.org/diseases-conditions/heart-disease):Offers expert advice, educational materials, and up-to-date
          articles on heart disease, risk factors, diagnosis, treatment options, and lifestyle recommendations.

        """
    )

    st.subheader("National Heart, Lung, and Blood Institute (NHLBI):")
    st.markdown(
        """
        [National Heart, Lung, and Blood Institute (NHLBI):](http://www.nhlbi.nih.gov/health-topics/heart-disease):Features evidence-based guidelines,
          research updates, patient education resources, and tools for heart disease prevention, management,and recovery.
        """
    )
    st.write("\n")
    st.markdown("---")

    st.markdown("<h2 style='color: teal;'>Medical Assistance</h2>", unsafe_allow_html=True)
    st.subheader("MediBuddy - Online Cardiologist Consultation: ")
    st.markdown(
        """
        [HeartDisease Medical Assistance](https://www.medibuddy.in/doctors/online-consultation/cardiologist)
        """
    )    
    
    
    
    
    
    
        
        
        
        
        
    




    
    
user_database = {
    "user1": {"password": "password1"},
    "user2": {"password": "password2"}
}

st.sidebar.title("Navigation")

selected_page = st.sidebar.selectbox("",
                                     ["🔒 Login", "📝 Sign Up", "🔍 Prediction", "🛡️ Preventive Measures"])

if selected_page == "🔒 Login":
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate_user(username, password):
            st.success("Login successful!")
            st.header("Let's diagnose together!")
        else:
            st.error("Invalid username or password")

elif selected_page == "📝 Sign Up":
    st.title("Sign Up")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    if st.button("Sign Up"):
        if new_username in user_database:
            st.error("Username already exists")
        else:
            user_database[new_username] = {"password": new_password}
            st.success("Sign up successful! You can now login.")

elif selected_page == "🔍 Prediction":
    st.markdown('<h1 style="color: Teal; font-family: Snell Roundhand, cursive;">🩺 Predict Your Disease 🩺</h1>', unsafe_allow_html=True)
    s1 = st.text_input('Symptom 1', value='')
    s2 = st.text_input('Symptom 2', value='')
    s3 = st.text_input('Symptom 3', value='')
    
    if st.button("Get your Prognosis", key="get_prognosis_button"):
        symptoms = f"{s1},{s2},{s3}"
        prediction = predictDiseases(symptoms)
        st.success(f"Predicted Disease: {prediction}")

elif selected_page == "🛡️ Preventive Measures":
    st.sidebar.title("🛡️ Preventive Measures")
    selected_prevention_page = st.sidebar.selectbox("",
                                     ["Select your Disease", "🦴 Arthritis", "🩺 Diabetes", "🧠 Migraine","💉 Hypertension","❤️ Heart Disease"])

    if selected_prevention_page == "🦴 Arthritis":
        Preventive_measures_Arthritis()

    elif selected_prevention_page == "🩺 Diabetes":
        Preventive_measures_Diabetes()

    elif selected_prevention_page == "🧠 Migraine":
        Preventive_measures_Migrane()
    elif selected_prevention_page == "💉 Hypertension":
        Preventive_measures_Hypertension()
    elif selected_prevention_page == "❤️ Heart Disease":
        Preventive_measures_HeartDisease()
    
    
        

