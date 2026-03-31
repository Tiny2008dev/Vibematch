import customtkinter as ctk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr


def build_voice(parent):

    recognizer = sr.Recognizer()
    sentiment_obj = SentimentIntensityAnalyzer()

    recorded_audio = None  # shared variable

    # ---------------- QUESTION ----------------
    question = ctk.CTkLabel(parent, text="How has your day been going so far?", font=("Arial", 20))
    question.pack(pady=30)

    # ---------------- MIC BUTTON ----------------
    mic_btn = ctk.CTkButton(
        parent,
        text="🎤",
        width=120,
        height=120,
        corner_radius=100,
        font=("Arial", 40),
        fg_color="#6C63FF"
    )
    mic_btn.pack(pady=20)

    # ---------------- STATUS ----------------
    status_label = ctk.CTkLabel(parent, text="Tap to Speak", text_color="gray")
    status_label.pack()

    # ---------------- ENTRY ----------------
    response_box = ctk.CTkEntry(parent, width=400, height=40, placeholder_text="Your response...")
    response_box.pack(pady=20)

    # ---------------- BUTTON FRAME ----------------
    btn_frame = ctk.CTkFrame(parent, fg_color="transparent")
    btn_frame.pack()

    start_btn = ctk.CTkButton(btn_frame, text="Start Recording")
    start_btn.grid(row=0, column=0, padx=10)

    # ---------------- NEXT BUTTON ----------------
    def next_button():
        question.configure(text="2nd question")
        response_box.delete(0, "end")

    next_btn = ctk.CTkButton(btn_frame, text="Next →", fg_color="#6C63FF", command=next_button)
    next_btn.grid(row=0, column=1, padx=10)

    # ---------------- RECORD FUNCTION ----------------
    def record_and_analyze():
        nonlocal recorded_audio

        try:
            mic_btn.configure(fg_color="#1DB954")
            status_label.configure(text="Calibrating...")

            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=2)

                status_label.configure(text="Speak now...")
                recorded_audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)

            status_label.configure(text="Recognizing...")

            text = recognizer.recognize_google(recorded_audio, language="en-US")

            # show in textbox
            response_box.delete(0, "end")
            response_box.insert(0, text)

            # sentiment
            sentiment = sentiment_obj.polarity_scores(text)

            if sentiment['compound'] >= 0.05:
                result = "Positive 😊"
            elif sentiment['compound'] <= -0.05:
                result = "Negative 😡"
            else:
                result = "Neutral 😐"

            status_label.configure(text=f"Sentiment: {result}")

        except sr.WaitTimeoutError:
            status_label.configure(text="You didn't speak in time.")
        except sr.UnknownValueError:
            status_label.configure(text="Couldn't understand.")
        except Exception as ex:
            status_label.configure(text=f"Error: {ex}")

        finally:
            mic_btn.configure(fg_color="#6C63FF")

    # ---------------- BUTTON BINDS ----------------
    mic_btn.configure(command=record_and_analyze)
    start_btn.configure(command=record_and_analyze)