# TechSoup-Bot
A demo prototype of FAQ AI Chatbot project by TechSoup team (Group 8) in Introduction of Information Technology course at RMIT University Vietnam 2023 Semester A using ChatGPT as language model, Whisper by OpenAI as speech-to-text model and ElevenLabs as text-to-speech model. This is just a demonstration on how we will use those technological approach if we have a chance to complete the project in the assignment with personal and customization trained model.

### Windows Installation
1. Clone repository:
`git clone https://github.com/khoi3975162/TechSoup-Bot.git`
`cd TechSoup-Bot`

2. Create virtual environment:
`pip install virtualenv`
`virtualenv venv`
`venv\Scripts\activate`

3. Install requirements:
`pip install -r requirements.txt`

4. (Optional) Reinstall pytorch to speed up Whisper:
`pip uninstall torch torchaudio torchvision -y`
`pip cache purge`
`pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`

5. Edit `config-example.json` and save as `config.json`:    
`chatgpt_token: ` (Required, see https://chat.openai.com/api/auth/session)\
`chatgpt_conversation_id: ` (Optional, leave blank will create a new conversation with start prompt instead of continue the existing one)\
`el_key: ElevenLabs key` (Optional, leave blank will use pyttsx3 instead)