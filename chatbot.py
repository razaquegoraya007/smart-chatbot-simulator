from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Route to render the HTML page
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle chatbot messages
@app.route("/chat", methods=["POST"])
def chat():
    # Retrieve the user message from the POST request
    user_input = request.json.get("message")

    # Simulated responses for the demo
    demo_responses = {
    "Hello": "Hi there! How can I assist you today?",
    "How are you?": "I'm just a bot, but I'm here to help!",
    "Tell me about your services": "We offer AI-powered solutions tailored to your needs, including chatbots, data analysis, and automation.",
    "What can you do?": "I can assist with answering questions, generating content, or even performing data analysis tasks.",
    "Who are you?": "I'm an AI-powered chatbot designed to make your life easier!",
    "Goodbye": "Goodbye! Have a great day!",
    "How do I contact support?": "You can reach our support team via email at support@example.com or call us at (123) 456-7890.",
    "Where are you located?": "Our main office is located in New York City, but we operate globally.",
    "What are your hours of operation?": "We’re available 24/7 to assist you with any inquiries or support requests.",
    "How does this chatbot work?": "I use AI technology to understand your questions and provide relevant responses.",
    "What is your refund policy?": "We offer a 30-day money-back guarantee on all purchases.",
    "Can I schedule an appointment?": "Absolutely! Please provide your preferred date and time, and we'll set it up for you.",
    "What are your payment options?": "We accept credit cards, PayPal, and bank transfers.",
    "How secure is your platform?": "We use industry-standard encryption to ensure your data is safe and secure.",
    "Do you offer free trials?": "Yes, we offer a 14-day free trial for new users.",
    "How do I reset my password?": "Click on 'Forgot Password' on the login page, and follow the instructions to reset your password.",
    "Can you help me with my order?": "Of course! Please provide your order number so I can assist you further.",
    "What is the status of my order?": "Please share your order ID, and I'll check the status for you.",
    "Do you have a mobile app?": "Yes, our mobile app is available on both iOS and Android platforms.",
    "What languages do you support?": "Currently, we support English, Spanish, French, and German.",
    "How do I unsubscribe from emails?": "Click the 'Unsubscribe' link at the bottom of any of our emails to stop receiving communications.",
    "What is your privacy policy?": "You can read our full privacy policy on our website under the 'Privacy' section.",
    "How can I provide feedback?": "We'd love to hear your feedback! You can send it to feedback@example.com.",
    "Do you offer discounts for students?": "Yes, we offer a 10% discount for students with a valid student ID.",
    "What is your cancellation policy?": "You can cancel your subscription at any time from your account settings.",
    "How long does shipping take?": "Shipping usually takes 5-7 business days, depending on your location.",
    "Do you ship internationally?": "Yes, we ship to most countries worldwide.",
    "Can I change my order after placing it?": "Please contact our support team as soon as possible to make any changes to your order.",
    "What are your customer support hours?": "Our support team is available 24/7 to assist you.",
    "Do you have a loyalty program?": "Yes, you can earn points for every purchase and redeem them for discounts.",
    "How can I track my shipment?": "You will receive a tracking link via email once your order has been shipped.",
    "Can I upgrade my subscription plan?": "Yes, you can upgrade your plan at any time from your account settings.",
    "Do you offer custom solutions?": "Yes, we provide custom solutions tailored to your business needs. Contact us for more details.",
    "How do I delete my account?": "Please go to your account settings and select 'Delete Account' to permanently remove your account.",
    "Is there a minimum contract length?": "No, our services are month-to-month with no long-term contracts required.",
    "Can I request a demo of your services?": "Sure! We'd be happy to schedule a demo at your convenience.",
    "What is your uptime guarantee?": "We guarantee 99.9% uptime for our services.",
    "Do you offer support in multiple languages?": "Currently, we provide support in English, but we’re working on expanding to more languages.",
    "Can I share my account with others?": "Our accounts are meant for individual use only. Sharing your account is against our terms of service.",
    "How do I become a partner or affiliate?": "Visit our 'Affiliate Program' page for more details on how to join.",
    "Do you offer a money-back guarantee?": "Yes, we have a 30-day money-back guarantee if you're not satisfied with our service.",
    "How do I update my billing information?": "Go to your account settings and select 'Billing' to update your information.",
    "What is the best way to reach customer support?": "You can email us at support@example.com or use our live chat feature for immediate assistance.",
    "How do I report a bug or issue?": "Please report any issues to our support team at bugs@example.com.",
    "Can I use your services for personal projects?": "Yes, our services are available for both personal and professional projects.",
    "What happens if I miss a payment?": "If a payment is missed, you will receive a reminder and a grace period to make the payment before any service interruptions.",
    "Do you have tutorials or guides?": "Yes, our website features a section with tutorials and guides to help you get started.",
    "How can I stay updated on new features?": "Sign up for our newsletter or follow us on social media to stay informed about new features.",
    "Can I get a quote for a custom project?": "Absolutely! Please reach out to us with your project details, and we'll provide a quote."
}


    # Provide a default response if the user input is not in the demo responses
    reply = demo_responses.get(user_input, "This is a simulated response for the demo.")

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
