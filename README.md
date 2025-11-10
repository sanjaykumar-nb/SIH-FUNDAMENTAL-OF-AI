# Intelligent Enterprise Assistant

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to the **Intelligent Enterprise Assistant** – your friendly AI-powered companion for navigating the complexities of public sector workplaces. Imagine having a knowledgeable colleague who can instantly answer questions about HR policies, IT troubleshooting, upcoming events, or even summarize lengthy documents. That's what we've built here: a robust, scalable chatbot leveraging natural language processing (NLP) to make your workday smoother and more efficient.

Whether you're an employee seeking quick information or an organization looking to streamline internal communications, this assistant is designed to handle it all with security, speed, and a touch of intelligence.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

Our assistant packs a punch with these key capabilities:

- **Conversational Chatbot**: Powered by advanced NLP, it understands and responds to queries on HR policies, IT support, company events, and more. Think of it as a tireless expert ready to chat 24/7.
- **Document Processing**: Upload PDF, DOCX, or TXT files for instant summarization and keyword extraction. Perfect for digesting reports or policies without the hassle.
- **Secure Authentication**: Implements email-based two-factor authentication (2FA) to ensure only authorized users access sensitive information.
- **Content Filtering**: Includes a bad language filter to maintain a professional and respectful environment.
- **High Performance**: Engineered for scalability, supporting multiple concurrent users with lightning-fast response times under 5 seconds.
- **User-Friendly Interface**: A clean, web-based frontend that feels intuitive and responsive.

## Architecture

At its core, the Intelligent Enterprise Assistant is a microservices-inspired web application built with:

- **Backend**: Python Flask framework handling API requests, authentication, and business logic.
- **Frontend**: Simple HTML5 with vanilla JavaScript for a lightweight, dependency-free UI.
- **Data Processing**: Utilizes libraries like PyPDF2 and docx2txt for document handling.
- **Security**: JWT tokens for session management and OTP for 2FA.
- **Scalability**: Modular design with separate routes, models, and utilities for easy extension.

The architecture ensures modularity, making it straightforward to integrate machine learning models or expand features as your needs grow.

## Prerequisites

Before diving in, ensure you have:
- Python 3.8 to 3.11 installed (we recommend the latest stable version for optimal compatibility).
- A basic understanding of web development and APIs – don't worry if you're new; we'll guide you through!

## Installation

Getting started is a breeze. Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/intelligent-enterprise-assistant.git
   cd intelligent-enterprise-assistant
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment** (if needed):
   - For real email 2FA, update SMTP settings in `backend/utils/auth_utils.py`.
   - Adjust any model paths or configurations as per your setup.

That's it! You're ready to launch.

## Usage

Launch the application and explore its capabilities:

1. **Start the Server**:
   ```bash
   python -m backend.app.main
   ```

2. **Access the App**:
   Open your browser and navigate to `http://localhost:5000`.

3. **Authenticate**:
   - Enter your email to receive an OTP (check the console for the code in development mode).
   - Verify the OTP to log in.

4. **Interact**:
   - Chat with the bot by typing queries like "What's the leave policy?" or "How do I reset my password?"
   - Upload documents for summarization and keyword extraction.
   - Experience seamless, secure interactions.

For testing, use the sample policy in `docs/sample_policy.pdf`.

## API Reference

Here's a quick overview of our RESTful API endpoints:

- `POST /auth/login`: Initiates login by sending an OTP to the provided email.
  - Body: `{ "email": "user@example.com" }`
- `POST /auth/verify`: Verifies the OTP and returns a JWT token.
  - Body: `{ "email": "user@example.com", "otp": "123456" }`
- `POST /chat/message`: Sends a message to the chatbot.
  - Headers: `Authorization: Bearer <token>`
  - Body: `{ "message": "Your query here" }`
- `POST /document/upload`: Uploads a document for processing.
  - Body: FormData with file.

All responses are in JSON format. Refer to the code for detailed schemas.

## Contributing

We believe in the power of community! If you'd like to contribute, here's how:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/amazing-enhancement`.
3. Make your changes and add tests.
4. Submit a pull request with a clear description.

Please follow our coding standards and ensure all tests pass. For major changes, open an issue first to discuss. We're excited to collaborate!

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details. Feel free to use, modify, and distribute as you see fit.

## Acknowledgments

A big thank you to the open-source community for tools like Flask and PyPDF2 that made this possible. Special shoutout to public sector innovators pushing the boundaries of AI for good.

If you have questions or feedback, reach out – let's build something amazing together!
