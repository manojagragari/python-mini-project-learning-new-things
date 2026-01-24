from unicodedata import name
import streamlit as st
st.title("VAK self test")
v,a,k=0,0,0
x=st.text_input("Enter your name")
if st.button("Submit"):
    st.write(f"Hello, {x}!")

# qs1=st.radio("Choose your learning style:", ("Visual", "Auditory", "Kinesthetic","None"),index=None)
# if qs1=="Visual":
#       v+=1
# elif qs1=="Auditory":
#         a+=1    
# elif qs1=="Kinesthetic":
#           k+=1
# else:
#     pass
# if st.button("get result"):
#       st.success(f"Your learning style is: {v/30*100}% Visual, {a/30*100}% Auditory, S{k/30*100}% Kinesthetic")
#streamlit run first.py
#pip install streamlit
questions = [
    {
        "q_no": 1,
        "question": "When you receive a new task at work, what helps you most to get started?",
        "options": [
            ("Reviewing an example that shows the final result", "V"),
            ("Talking it through step by step with someone", "A"),
            ("Trying it out and adjusting as you go", "K")
        ]
    },
    {
        "q_no": 2,
        "question": "In a training session, you remember information best when:",
        "options": [
            ("It is structured and clearly laid out", "V"),
            ("It is explained in detail", "A"),
            ("You actively participate", "K")
        ]
    },
    {
        "q_no": 3,
        "question": "While preparing for an exam, you usually:",
        "options": [
            ("Organize notes neatly", "V"),
            ("Read explanations aloud or repeat them", "A"),
            ("Practice by solving problems", "K")
        ]
    },
    {
        "q_no": 4,
        "question": "If instructions are unclear, you prefer to:",
        "options": [
            ("Look for a reference or sample", "V"),
            ("Ask someone to clarify", "A"),
            ("Experiment until it works", "K")
        ]
    },
    {
        "q_no": 5,
        "question": "You understand a new concept fastest when:",
        "options": [
            ("It is presented in an organized format", "V"),
            ("It is explained logically", "A"),
            ("You apply it immediately", "K")
        ]
    },
    {
        "q_no": 6,
        "question": "During a meeting, you focus most on:",
        "options": [
            ("The structure of the discussion", "V"),
            ("What people are saying", "A"),
            ("What actions need to be taken", "K")
        ]
    },
    {
        "q_no": 7,
        "question": "When learning a new software tool, you prefer:",
        "options": [
            ("Exploring the interface first", "V"),
            ("Listening to guidance", "A"),
            ("Using it directly", "K")
        ]
    },
    {
        "q_no": 8,
        "question": "If you forget something important, you try to remember by:",
        "options": [
            ("Recalling how it was written or arranged", "V"),
            ("Recalling how it was explained", "A"),
            ("Recalling what you were doing", "K")
        ]
    },
    {
        "q_no": 9,
        "question": "You feel most confident when:",
        "options": [
            ("You have reviewed material thoroughly", "V"),
            ("You have discussed it well", "A"),
            ("You have practiced it", "K")
        ]
    },
    {
        "q_no": 10,
        "question": "When solving a problem, your first step is usually:",
        "options": [
            ("Understanding the full structure", "V"),
            ("Thinking through the explanation", "A"),
            ("Jumping in and testing solutions", "K")
        ]
    },
    {
        "q_no": 11,
        "question": "In a classroom or training room, you prefer:",
        "options": [
            ("Clear organization of content", "V"),
            ("Detailed explanations", "A"),
            ("Interactive activities", "K")
        ]
    },
    {
        "q_no": 12,
        "question": "You remember people better by:",
        "options": [
            ("Their overall appearance or presence", "V"),
            ("Conversations you had with them", "A"),
            ("Experiences you shared", "K")
        ]
    },
    {
        "q_no": 13,
        "question": "When planning your day, you rely on:",
        "options": [
            ("A clear outline", "V"),
            ("Talking through priorities", "A"),
            ("Starting tasks and adjusting", "K")
        ]
    },
    {
        "q_no": 14,
        "question": "If you attend a workshop, you enjoy it most when:",
        "options": [
            ("Content is well structured", "V"),
            ("Discussions are engaging", "A"),
            ("Activities are hands-on", "K")
        ]
    },
    {
        "q_no": 15,
        "question": "When learning something difficult, you prefer to:",
        "options": [
            ("Break it into organized sections", "V"),
            ("Explain it to someone", "A"),
            ("Practice repeatedly", "K")
        ]
    },
    {
        "q_no": 16,
        "question": "If someone explains a complex idea, you prefer it to be:",
        "options": [
            ("Well-organized", "V"),
            ("Clearly spoken", "A"),
            ("Demonstrated through action", "K")
        ]
    },
    {
        "q_no": 17,
        "question": "You judge a learning resource as good when:",
        "options": [
            ("It is well-presented", "V"),
            ("It is easy to follow verbally", "A"),
            ("It allows practice", "K")
        ]
    },
    {
        "q_no": 18,
        "question": "When revising material, you often:",
        "options": [
            ("Rewrite or reorganize it", "V"),
            ("Recite or discuss it", "A"),
            ("Use it in exercises", "K")
        ]
    },
    {
        "q_no": 19,
        "question": "In group work, you naturally take the role of:",
        "options": [
            ("Organizer", "V"),
            ("Communicator", "A"),
            ("Doer", "K")
        ]
    },
    {
        "q_no": 20,
        "question": "You feel most engaged when:",
        "options": [
            ("Information is clearly arranged", "V"),
            ("There is active discussion", "A"),
            ("You are involved in the task", "K")
        ]
    },
    {
        "q_no": 21,
        "question": "When learning rules or procedures, you prefer:",
        "options": [
            ("Reviewing a clear format", "V"),
            ("Having them explained", "A"),
            ("Trying them out", "K")
        ]
    },
    {
        "q_no": 22,
        "question": "If you had to teach someone, you would:",
        "options": [
            ("Prepare structured material", "V"),
            ("Explain step by step", "A"),
            ("Let them practice", "K")
        ]
    },
    {
        "q_no": 23,
        "question": "You solve problems best when:",
        "options": [
            ("You see the full plan", "V"),
            ("You talk through the logic", "A"),
            ("You work through it", "K")
        ]
    },
    {
        "q_no": 24,
        "question": "You lose focus most easily when:",
        "options": [
            ("Content is poorly organized", "V"),
            ("Explanations are unclear", "A"),
            ("You cannot engage actively", "K")
        ]
    },
    {
        "q_no": 25,
        "question": "When remembering instructions, you rely on:",
        "options": [
            ("How they were arranged", "V"),
            ("How they were explained", "A"),
            ("What you did with them", "K")
        ]
    },
    {
        "q_no": 26,
        "question": "You feel learning is effective when:",
        "options": [
            ("Everything makes sense structurally", "V"),
            ("Concepts are clearly explained", "A"),
            ("You can apply it immediately", "K")
        ]
    },
    {
        "q_no": 27,
        "question": "In online learning, you prefer:",
        "options": [
            ("Well-structured material", "V"),
            ("Clear verbal guidance", "A"),
            ("Interactive tasks", "K")
        ]
    },
    {
        "q_no": 28,
        "question": "If you are confused, you usually:",
        "options": [
            ("Review reference material", "V"),
            ("Ask questions", "A"),
            ("Try again differently", "K")
        ]
    },
    {
        "q_no": 29,
        "question": "You stay motivated when:",
        "options": [
            ("Progress is clearly visible", "V"),
            ("Feedback is discussed", "A"),
            ("You are actively involved", "K")
        ]
    },
    {
        "q_no": 30,
        "question": "Overall, you learn best when:",
        "options": [
            ("Information is organized", "V"),
            ("Information is explained", "A"),
            ("Information is practiced", "K")
        ]
    }
]
st.divider()

answers = []

# Display all questions
for q in questions:
    option_texts = [opt[0] for opt in q["options"]]

    selected = st.radio(
        f"Q{q['q_no']}. {q['question']}",
        option_texts,
        key=f"q{q['q_no']}"
    )

    # Map selected option to hidden V/A/K
    for text, vak in q["options"]:
        if selected == text:
            answers.append(vak)

st.divider()

# Submit button
if st.button("📊 Get Result"):
    if not name:
        st.warning("Please enter your name before submitting.")
    elif len(answers) < len(questions):
        st.warning("Please answer all questions.")
    else:
        v = answers.count("V")
        a = answers.count("A")
        k = answers.count("K")

        total = len(questions)

        st.success(f"Hello {name} 👋 Here is your learning style result:")

        st.write(f"👀 **Visual:** {v/total*100:.2f}%")
        st.write(f"👂 **Auditory:** {a/total*100:.2f}%")
        st.write(f"🤸 **Kinesthetic:** {k/total*100:.2f}%")

        # Final dominant style
        if v > a and v > k:
            st.info(" Your dominant learning style is **Visual**")
        elif a > v and a > k:
            st.info(" Your dominant learning style is **Auditory**")
        else:
            st.info(" Your dominant learning style is **Kinesthetic**")
