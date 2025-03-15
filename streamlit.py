{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b9c18385",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (1.43.2)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (1.9.0)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (5.5.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: numpy<3,>=1.23 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (23.2)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (2.0.3)\n",
      "Requirement already satisfied: pillow<12,>=7.1.0 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (9.4.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (4.25.4)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (11.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (2.31.0)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.4.0 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (3.1.44)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (0.9.1)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from streamlit) (6.3.2)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.17.3)\n",
      "Requirement already satisfied: narwhals>=1.14.2 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (1.30.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (1.26.16)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2023.7.22)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (22.1.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\ltummala\\appdata\\local\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1818c203",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-03-15 11:11:47.926 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.144 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\ltummala\\AppData\\Local\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-03-15 11:11:48.144 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.145 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.145 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.145 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.146 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.146 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.146 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.147 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.147 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.147 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.148 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.148 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.149 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.150 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.150 Session state does not function when running a script without `streamlit run`\n",
      "2025-03-15 11:11:48.151 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-15 11:11:48.152 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "st.title(\"Hello, Streamlit! 👋\")\n",
    "st.write(\"This is a simple Streamlit app.\")\n",
    "\n",
    "# Add a button\n",
    "if st.button(\"Click Me!\"):\n",
    "    st.write(\"Button Clicked!\")\n",
    "\n",
    "# User Input\n",
    "name = st.text_input(\"Enter your name:\")\n",
    "if name:\n",
    "    st.write(f\"Hello, {name}!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e474ef2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
