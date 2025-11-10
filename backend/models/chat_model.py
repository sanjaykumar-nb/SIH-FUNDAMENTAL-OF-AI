# Simple rule-based chatbot for demo

def answer_question(question: str) -> str:
    question_lower = question.lower()
    if "leave" in question_lower or "vacation" in question_lower:
        return "Employees are entitled to 20 days annual leave, 10 days sick leave."
    elif "salary" in question_lower or "pay" in question_lower:
        return "Salaries are paid monthly. Benefits include health insurance and provident fund."
    elif "password" in question_lower or "reset" in question_lower:
        return "Contact IT desk or use self-service portal for password reset."
    elif "software" in question_lower or "install" in question_lower:
        return "Request software installation via IT ticket system."
    elif "network" in question_lower or "internet" in question_lower:
        return "Report network issues to IT support."
    elif "meeting" in question_lower or "event" in question_lower:
        return "Annual Meeting is held every December. Team Building quarterly."
    else:
        return "I'm sorry, I don't have information on that. Please contact HR or IT for more details."
