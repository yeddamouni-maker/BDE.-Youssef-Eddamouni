import streamlit as st
import random

st.set_page_config(page_title="Luftsicherheitsassistent Training")

st.title("Erstausbildung Luftsicherheitsassistent")
st.write("Kostenloses Multiple Choice Training (100 Fragen)")

# -------------------------
# Fragenkatalog
# -------------------------

questions = []

topics = [
    "LuftSiG",
    "ZÜP",
    "Röntgentechnik",
    "Handgepäckkontrolle",
    "Personenkontrolle",
    "Sprengstofferkennung",
    "Gefahrgut",
    "Zutrittskontrolle",
    "Dokumentenprüfung",
    "Notfallmaßnahmen"
]

for i in range(1, 101):
    topic = random.choice(topics)
    questions.append({
        "question": f"Frage {i}: Welche Aussage zu {topic} ist korrekt?",
        "options": [
            f"{topic} dient der Gefahrenabwehr.",
            f"{topic} ist freiwillig.",
            f"{topic} betrifft nur Flugpersonal.",
            f"{topic} ist nicht gesetzlich geregelt."
        ],
        "answer": f"{topic} dient der Gefahrenabwehr."
    })

# -------------------------
# Quiz Logik
# -------------------------

if "current" not in st.session_state:
    st.session_state.current = 0
    st.session_state.score = 0
    random.shuffle(questions)

if st.session_state.current < len(questions):

    q = questions[st.session_state.current]
    st.subheader(f"Frage {st.session_state.current + 1}")

    answer = st.radio(q["question"], q["options"])

    if st.button("Antwort bestätigen"):
        if answer == q["answer"]:
            st.success("Richtig")
            st.session_state.score += 1
        else:
            st.error("Falsch")

        st.session_state.current += 1
        st.rerun()

else:
    st.subheader("Prüfung abgeschlossen")
    st.write(f"Punkte: {st.session_state.score} von 100")

    if st.session_state.score >= 70:
        st.success("Bestanden")
    else:
        st.warning("Nicht bestanden")

    if st.button("Neu starten"):
        st.session_state.current = 0
        st.session_state.score = 0
        random.shuffle(questions)
        st.rerun()


    