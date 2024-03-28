import speech_recognition as sr

def enroll_user(username="user123"):
    recognizer = sr.Recognizer()

    for i in range(3):
        with sr.Microphone() as source:
            print(f"Speak passphrase for sample {i + 1}:")
            #speak(f"Speak passphrase for sample {i + 1}")
            audio = recognizer.listen(source)

            with open(f"data/{username}_sample{i + 1}.wav", "wb") as file:
                file.write(audio.get_wav_data())

    print(f"{username} enrolled successfully.")


def authenticate_user(username="user123"):
    recognizer = sr.Recognizer()

    print("Speak passphrase for authentication:")
    #speak("Speak passphrase for authentication:")
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    stored_samples = [f"data/{username}_sample{i + 1}.wav" for i in range(3)]

    for sample in stored_samples:
        with sr.AudioFile(sample) as file:
            stored_audio = recognizer.record(file)
            try:
                user_input = recognizer.recognize_google(audio)
                stored_input = recognizer.recognize_google(stored_audio)

                similarity = user_input == stored_input

                if similarity:
                    print(f"Authenticated as {username}.")
                    #speak(f"Authenticated as {username}.")
                    return True
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                print(f"RequestError: {e}")

    print("Authentication failed.")
    return False

#
# if __name__ == "__main__":
#     username = "user123"
#
#     # Enroll user
#     enroll_user(username)
#
#     # Authenticate user
#     authenticated = authenticate_user(username)
#     if authenticated:
#         print("Access granted.")
#     else:
#         print("Access denied.")

