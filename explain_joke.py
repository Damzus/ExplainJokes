import streamlit as st
import openai
import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

                          
# Creating the Streamlit web app
st.title("Joke Explainer")

# Text input for the user to enter their joke
joke = st.text_area("Enter your joke here:")

# Button to submit the joke
if st.button("Submit"):
    if joke:
        # Call the OpenAI API to get an explanation of the joke
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Explain this joke: {joke}"}]
        )
        
        # Extract the explanation from the response
        explanation = response.choices[0].message.content
        # Display the explanation
        st.subheader("Explanation")
        st.write(explanation)
    else:
        st.warning("Please enter a joke before submitting.")