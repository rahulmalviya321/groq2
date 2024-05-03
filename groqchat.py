import streamlit as st
from groq import Groq

# Initialize the Groq client
client = Groq(api_key="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")

def get_chat_response(user_message):
    """
    Sends a message to the Groq API and returns the response.
    """
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="llama3-70b-8192",
    )
    return response.choices[0].message.content

def main():
    st.title("ask me")

    # User input for system role
    system_role = st.text_input("System Role (e.g., assistant):")
    # User input for user role
    user_role = st.text_input("User Role (e.g., customer):")
    # Submit button
    if st.button("Submit"):
        # Combine roles into a single message
        message = f"{system_role} says: {user_role}"
        # Get the chat response
        sarch_anything = get_chat_response(message)
        # Display the response
        st.write(f"Response: {sarch_anything}")

if __name__ == "__main__":
    main()