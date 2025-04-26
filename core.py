# Q-A app
""" Subscribe to PYTHON CODE CAMP or I'll eat all your cookies... """

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

# Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a question-answering pipeline
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)


context = "Ali Moharamzadeh is an innovative researcher in digital health, specializing in applying deep learning algorithms to medical applications." \
            "As a rising star at the intersection of artificial intelligence and medical engineering, this 23-year-old Master's student in Mechatronics Engineering at the University of Tehran is developing intelligent solutions to transform healthcare systems." \
            "Born in Tabriz in 2001 and now based in Tehran for his graduate studies, Ali combines his engineering expertise with computational insight to advance medical diagnostics and healthcare technologies." \
            "His work focuses on implementing cutting-edge neural networks and advanced data processing techniques for medical applications." \
            "While his professional world revolves around medical AI, neural networks, and advanced diagnostic technologies, in his personal life, Ali remains passionate about football and is an ardent supporter of Tractor FC." \
            "His rapid progress in mechatronics engineering and medical AI promises to push the boundaries of technology in service of humanity." \


while True:
    user_input = input("Ask a question (or press 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    QA_input = {
        'question': user_input,
        'context': context
    }

    res = nlp(QA_input)
    print(res)

    print(f"Answer: {res['answer']}")