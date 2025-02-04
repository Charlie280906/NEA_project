# IMPORTS
from groq import Groq

# Function to improve a given password
def improve_password(password):
    try:
        client = Groq(
            api_key="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"
        )

        # Chat request to Groq API
        completion = client.chat.completions.create(
            model="llama3-70b-8192",  # Model to use
            messages=[
                {
                    # Prompt to the AI
                    "role": "user",
                    "content": f"Improve the password \"{password}\" whilst all the improved versions still resemble the original, giving me 5 improved versions. Also please don't add the ** to the beginning and end of the improved suggestions. If an empty password is given, please return nothing."
                },
                {
                    "role": "assistant",
                    "content": ""
                }
            ],
            temperature=1, 
            max_tokens=1024,
            top_p=1,  
            stream=True,  
            stop=None,  
        )

        response = []
        for chunk in completion:
            # Append actual words from each chunks to the response list
            response.append(chunk.choices[0].delta.content or "")

        improved_passwords = []
        for element_index in range(0, len(response)-1):
            # Check for a structure of a number followed by a .
            if response[element_index] in ["1", "2", "3", "4", "5"] and response[element_index+1] == ".":
                # Flag to find index of the end of suggestion
                flag = element_index + 1
                while True:
                    # Looking for - to show end of suggestion
                    if response[flag] == " -":
                        password_endpoint = flag
                        break
                    else:
                        flag += 1

                # Storing parts of the improved password
                improved_version = []
                # Removes leading space
                start_element = response[element_index+2].replace(" ", "")
                improved_version.append(start_element)
                # Appends remaining elements of the password
                for i in range(element_index+3, password_endpoint):
                    improved_version.append(response[i])
                # Combines all elements into a single string
                improved_passwords.append("".join(improved_version))
    
    except:
        improved_passwords = improve_password(password)

    # Return the list of improved password suggestions
    return improved_passwords
