# from flask import Flask, render_template, request, jsonify, redirect, url_for
# from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

# app = Flask(__name__)

# # بارگذاری مدل
# print("در حال بارگذاری مدل هوش مصنوعی...")
# model_name = "deepset/roberta-base-squad2"
# try:
#     model = AutoModelForQuestionAnswering.from_pretrained(model_name)
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
#     nlp = pipeline('question-answering', model=model, tokenizer=tokenizer, device='cpu')
#     print("مدل با موفقیت بارگذاری شد!")
# except Exception as e:
#     print(f"خطا در بارگذاری مدل: {e}")
#     exit()

# # متن زمینه درباره شما
# context = "Ali Moharamzadeh is an innovative researcher in digital health, specializing in applying deep learning algorithms to medical applications." \
#             "As a rising star at the intersection of artificial intelligence and medical engineering, this 23-year-old Master's student in Mechatronics Engineering at the University of Tehran is developing intelligent solutions to transform healthcare systems." \
#             "Born in Tabriz in 2001 and now based in Tehran for his graduate studies, Ali combines his engineering expertise with computational insight to advance medical diagnostics and healthcare technologies." \
#             "His work focuses on implementing cutting-edge neural networks and advanced data processing techniques for medical applications." \
#             "While his professional world revolves around medical AI, neural networks, and advanced diagnostic technologies, in his personal life, Ali remains passionate about football and is an ardent supporter of Tractor FC." \
#             "His rapid progress in mechatronics engineering and medical AI promises to push the boundaries of technology in service of humanity." \


# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/ask', methods=['POST'])
# def ask():
#     try:
#         data = request.get_json()
#         question = data['question']
        
#         result = nlp({
#             'question': question,
#             'context': context
#         })
        
#         return jsonify({
#             'answer': result['answer'],
#             'confidence': f"{result['score']:.2%}",
#             'status': 'success'
#         })
    
#     except Exception as e:
#         return jsonify({
#             'error': str(e),
#             'status': 'failed'
#         }), 400

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# پایگاه داده جامع سوالات و پاسخ‌ها
qa_database = {
    "رشته": "کارشناسی ارشد مهندسی مکاترونیک از دانشگاه تهران",
    "تخصص": "یادگیری عمیق در کاربردهای پزشکی",
    "متولد": "متولد ۱۳۸۰ در تبریز",
    "تیم فوتبال": "هوادار تیم تراکتور",
    "تحقیقات": "تمرکز بر هوش مصنوعی پزشکی و شبکه‌های عصبی",
    "سن": "۲۳ ساله",
    "دانشگاه": "دانشگاه تهران",
    "شهر": "ساکن تهران",
    "علاقه": "علاقه‌مند به ریاضیات و هوش مصنوعی"
}

def find_best_answer(question):
    """پیدا کردن بهترین پاسخ با تطبیق کلیدواژه"""
    question = question.lower()
    
    # جستجوی هوشمند در پایگاه داده
    for keyword, answer in qa_database.items():
        if keyword in question:
            return answer, 0.95  # 95% اطمینان برای پاسخ‌های مستقیم
    
    # پاسخ پیش‌فرض برای سوالات ناشناخته
    return "متأسفانه اطلاعات دقیقی در این مورد ندارم. لطفاً سوال دیگری بپرسید.", 0.3

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        question = request.json['question']
        answer, confidence = find_best_answer(question)
        
        return jsonify({
            'question': question,
            'answer': answer,
            'confidence': f"{confidence*100:.1f}%",
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': "خطا در پردازش سوال",
            'status': 'failed'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)