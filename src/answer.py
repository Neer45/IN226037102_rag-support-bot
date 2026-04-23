def generate_answer(context, query):
    if "contact" in query.lower():
        return "Customers can contact support via toll-free number, email, or website."
    
    elif "grievance" in query.lower():
        return "Customers can raise complaints through grievance redressal mechanism."
    
    elif "claims" in query.lower():
        return "Claims are processed in a fair and transparent manner."
    
    else:
        return "I don't know based on the document"