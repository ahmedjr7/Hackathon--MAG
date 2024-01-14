from flask import Flask, request, jsonify

app = Flask(__name__)
from openai import OpenAI
client = OpenAI(api_key="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")

@app.route('/submit', methods=['POST'])
def submit():
    # Extract data from JSON request
    data = request.json
    age = data.get('age')
    gender = data.get('gender')
    weight = data.get('weight')
    height = data.get('height')
    activityLevel = data.get('activityLevel')
    healthGoals = data.get('healthGoals')
    foodPreferences = data.get('foodPreferences')
    medicalHistory = data.get('medicalHistory')

    # Here you would implement your logic for recommendations
    # Placeholder for recommendation logic
    recommendations = (
    f" Act Like Personalized Health and Nutrition Recommendations:\n"
    f"1. Age and Gender: As a {age}-year-old {gender}, focus on nutrients important for your age and gender, such as calcium and possibly iron.\n"
    f"2. Weight and Height: With a weight of {weight} kg and height of {height} cm, maintaining a balanced diet and regular exercise is key to achieving a healthy BMI.\n"
    f"3. Activity Level: Your current activity level is '{activityLevel}'. Aim to incorporate both aerobic and strength-training exercises into your routine for optimal health.\n"
    f"4. Health Goals: To achieve your goals of {', '.join(healthGoals)}, consider a diet rich in {'' if 'weight loss' in healthGoals else 'whole grains, lean proteins, and a variety of fruits and vegetables'}.\n"
    f"5. Food Preferences: Given your preference for {', '.join(foodPreferences)}, include these in your meals in a balanced way. Consider exploring healthy recipes that align with these preferences.\n"
    f"6. Medical History: Taking into account your medical history of {', '.join(medicalHistory)}, it's important to tailor your diet and exercise to manage or mitigate these conditions. Consult with healthcare professionals for personalized advice.\n"
)
    
    
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
      ]
    )

    print(completion.choices[0].message)

    # Return recommendations as JSON
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
