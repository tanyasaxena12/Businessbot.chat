

#BEST TRAINED BOT | WORKS WELL | NO PDF
"""
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
#CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

openai.api_key = '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'  # replace 'your-openai-key' with your actual OpenAI key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])

@app.route('/ask', methods=['POST'])
def ask():
    message = request.json['message']

    # company's info
    company_info = [
        "Jun Cyber is a Service Disabled Veteran Owned Business and Florida Certified Veterans Business Enterprise and Minority Business Enterprise that provides full spectrum IT, cybersecurity, and digital services to small and medium businesses. Our team has been trusted by clients from many different industries. From data analytics, defense contractors, and law firms, Jun Cyber is your go-to source for “Service” and “Integrity” with all of our cybersecurity offerings.",
        "The CEO of Jun Cyber is Wilson Bautista.",
        "Some of the specific services offered include managed IT services, cybersecurity assessments and solutions, network infrastructure design and implementation, cloud services, data analytics, web development, digital marketing, and more. The company is committed to providing excellent service and maintaining the highest level of integrity in all of their offerings.",
        "You can contact Jun Cyber by visiting their website at juncyber.com and clicking on the 'Contact Us' tab. You can fill out the contact form on their website or send an email to info@juncyber.com. You can also call them at (561) 291-8333. Jun Cyber is located in Palm Beach Gardens, Florida and their address is 4440 PGA Blvd., Suite 600, Palm Beach Gardens, FL 33410. They are open Monday through Friday from 8:30 am to 5:30 pm Eastern Time.","In addition to managed IT services, cybersecurity assessments and solutions, network infrastructure design and implementation, cloud services, data analytics, web development, and digital marketing, Jun Cyber also offers services such as disaster recovery planning, compliance audits, risk assessments, penetration testing, vulnerability scanning, phishing simulations, employee cybersecurity training, and incident response planning and support. They tailor their services to meet the unique needs of each client and prioritize customer satisfaction and cybersecurity excellence.",
        "Specialties Cybersecurity, Project Management, NIST 800-171, ISO 27001, Risk Assessment, 3rd Party Risk Assessments, Vulnerability Assessments, Security Architecture, Automation, Secure Digital Workspace, Managed IT Services, Managed Security Services, and RPA"
        # Add more documents as needed
    ]

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that knows the following about Jun Cyber: " + ' '.join(company_info)
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    response_message = response['choices'][0]['message']['content']
    return jsonify({'message': response_message})

if __name__ == '__main__':
    app.run(debug=True)

"""
"""
#COMPANY INFO IN DICTIONARY
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import PyPDF2

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

openai.api_key = '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' 

# Define company info
company_info = {
    'company_name': 'Jun Cyber',
    'founder': 'Wilson Bautista',
    'founded_year': '2017',
    'product': 'Secure Digital Workspace Solutions',
    'location': 'Florida, USA'
}

# Read and extract content from PDF
def get_pdf_content(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    content = ""
    for page_num in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        content += page_obj.extractText()
    pdf_file_obj.close()
    return content

pdf_content = get_pdf_content('AccessControlPolicy.pdf')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    message = request.json['message']
    
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {
                "role": "system",
                "content": f"You are a helpful assistant. You have access to the following information:\n{company_info}\n\n{pdf_content}"
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    response_message = response['choices'][0]['message']['content']
    return jsonify({'message': response_message})

if __name__ == '__main__':
    app.run(debug=True)
"""
#BEST TRAINED BOT | WORKS WELL | READS PDF AND ARRAY

"""
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import PyPDF2
from PyPDF2 import PdfReader

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

openai.api_key = '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'

# Define company info
company_info = [
    "Jun Cyber is a Service Disabled Veteran Owned Business and Florida Certified Veterans Business Enterprise and Minority Business Enterprise that provides full spectrum IT, cybersecurity, and digital services to small and medium businesses. Our team has been trusted by clients from many different industries. From data analytics, defense contractors, and law firms, Jun Cyber is your go-to source for “Service” and “Integrity” with all of our cybersecurity offerings.",
        "The CEO of Jun Cyber is Wilson Bautista.",
        "Some of the specific services offered include managed IT services, cybersecurity assessments and solutions, network infrastructure design and implementation, cloud services, data analytics, web development, digital marketing, and more. The company is committed to providing excellent service and maintaining the highest level of integrity in all of their offerings.",
        "You can contact Jun Cyber by visiting their website at juncyber.com and clicking on the 'Contact Us' tab. You can fill out the contact form on their website or send an email to info@juncyber.com. You can also call them at (561) 291-8333. Jun Cyber is located in Palm Beach Gardens, Florida and their address is 4440 PGA Blvd., Suite 600, Palm Beach Gardens, FL 33410. They are open Monday through Friday from 8:30 am to 5:30 pm Eastern Time.","In addition to managed IT services, cybersecurity assessments and solutions, network infrastructure design and implementation, cloud services, data analytics, web development, and digital marketing, Jun Cyber also offers services such as disaster recovery planning, compliance audits, risk assessments, penetration testing, vulnerability scanning, phishing simulations, employee cybersecurity training, and incident response planning and support. They tailor their services to meet the unique needs of each client and prioritize customer satisfaction and cybersecurity excellence.",
        "Specialties Cybersecurity, Project Management, NIST 800-171, ISO 27001, Risk Assessment, 3rd Party Risk Assessments, Vulnerability Assessments, Security Architecture, Automation, Secure Digital Workspace, Managed IT Services, Managed Security Services, and RPA"   
]

#WORKS WELL DATA = ARRAY + PDF
documents = company_info

with open('AccessControlPolicy.pdf', 'rb') as file:
    pdf_reader = PdfReader(file)
    for page in pdf_reader.pages:
        documents.append(page.extract_text())


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    message = request.json['message']  # get the message from frontend

    # Create an array of messages. Each message has a 'role' and 'content'.
    # The 'system' role is used to set the behavior of the assistant.
    # The 'user' role is used to give instructions to the assistant.
    # The 'documents' variable is included in the system message to provide information to the assistant.
    messages = [
        {
            "role": "system",
            "content": f"You are a helpful assistant that knows the following information: {' '.join(documents)}"
        },
        {
            "role": "user",
            "content": message
        }
    ]

    # Send a chat model request to OpenAI
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    response_message = response['choices'][0]['message']['content']  # get the response message from OpenAI
    return jsonify({'message': response_message})  # send the response message back to the frontend

if __name__ == '__main__':
    app.run(debug=True)

"""
#BEST TILL 5-05-23 WORKS WITH MULTIPLE PDFS
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import PyPDF2
import glob

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

openai.api_key = ''

# Define company info
company_info = [
    "Jun Cyber is a Service Disabled Veteran Owned Business and Florida Certified Veterans Business Enterprise and Minority Business Enterprise that provides full spectrum IT, cybersecurity, and digital services to small and medium businesses. Our team has been trusted by clients from many different industries. From data analytics, defense contractors, and law firms, Jun Cyber is your go-to source for “Service” and “Integrity” with all of our cybersecurity offerings.",
        "The CEO of Jun Cyber is Wilson Bautista.",
        "Some of the specific services offered include managed IT services, cybersecurity assessments and solutions, network infrastructure design and implementation, cloud services, data analytics, web development, digital marketing, and more. The company is committed to providing excellent service and maintaining the highest level of integrity in all of their offerings.",
        "You can contact Jun Cyber by visiting their website at juncyber.com and clicking on the 'Contact Us' tab. You can fill out the contact form on their website or send an email to info@juncyber.com. You can also call them at (561) 291-8333. Jun Cyber is located in Palm Beach Gardens, Florida and their address is 4440 PGA Blvd., Suite 600, Palm Beach Gardens, FL 33410. They are open Monday through Friday from 8:30 am to 5:30 pm Eastern Time.","In addition to managed IT services, cybersecurity assessments and solutions, network infrastructure design and implementation, cloud services, data analytics, web development, and digital marketing, Jun Cyber also offers services such as disaster recovery planning, compliance audits, risk assessments, penetration testing, vulnerability scanning, phishing simulations, employee cybersecurity training, and incident response planning and support. They tailor their services to meet the unique needs of each client and prioritize customer satisfaction and cybersecurity excellence.",
        "Specialties Cybersecurity, Project Management, NIST 800-171, ISO 27001, Risk Assessment, 3rd Party Risk Assessments, Vulnerability Assessments, Security Architecture, Automation, Secure Digital Workspace, Managed IT Services, Managed Security Services, and RPA"   
]

# Load PDF data
pdf_files = glob.glob('*.pdf')
documents = company_info

# Load PDF data
# Load PDF data
"""
#For prinitng all pdfs
for pdf_file in pdf_files:
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text = page.extract_text()
            print(f"Extracted text from {pdf_file}:\n{text}\n")  # add this line
            documents.append(text)
"""

# Load PDF data
import pdfplumber

# Load PDF data
for pdf_file in pdf_files:
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            # preprocess the text: remove newlines, extra spaces, etc.
            text = text.replace('\n', ' ').replace('\r', '')  # remove newlines and carriage returns
            text = ' '.join(text.split())  # remove extra spaces

            print(f"Preprocessed text from {pdf_file}:\n{text}\n")  # print preprocessed text
            documents.append(text)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    message = request.json['message']  # get the message from frontend

    # Create an array of messages.
    # The 'system' role is used to set the behavior of the assistant.
    # The 'user' role is used to give instructions to the assistant.
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        }
    ]

    # Add documents as user messages
    for document in documents:
        messages.append({
            "role": "user",
            "content": document
        })

    # Add actual user message
    messages.append({
        "role": "user",
        "content": message
    })

    # Send a chat model request to OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    response_message = response['choices'][0]['message']['content']  # get the response message from OpenAI
    return jsonify({'message': response_message})  # send the response message back to the frontend

if __name__ == '__main__':
    app.run(debug=True)
