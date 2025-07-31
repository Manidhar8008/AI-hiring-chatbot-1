import openai

def generate_questions(tech_stack):
    questions = {}
    for tech in tech_stack:
        prompt = f"Generate 3 intermediate technical interview questions for a candidate skilled in {tech}."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a technical interviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        generated = response['choices'][0]['message']['content']
        questions[tech] = [q.strip() for q in generated.split("\n") if q.strip()]
    return questions
