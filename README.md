# Learning Plus Plus

This program analyzes lecture videos or typed notes to detect important keywords the user may need to refer. It also provides top web sources linked to each keyword for more information.

### Inspiration
Due to YouTube's increasing prevalence, students are using YouTube for academic purposes, namely, viewing online lectures. But lectures become confusing if the audience lacks some previous knowledge of certain key terms.

### What it does
A program that analyzes lecture videos to find important terms and concepts and search the web for additional resources.

### How we built it
1. We download YouTube video and generate its corresponding .flac audio file using pytube
2. We analyze the audio file and generate a transcript using Google Cloud's SpeechRecognition API
3. We analyze the transcript using a database of relevant jargons the user may have difficulty understanding
4. We generate an output message consists of the terms, their definitions, and their corresponding information on the web
5. We use an electron module to allow the user to input a YouTube link or a text file (.doc .docx .txt), and to view the output
6. The backend of this program was entirely coded using python-37 and its dependencies as stated
7. For the GUI aspect, ElectronJS was used in conjunction with HTML and CSS to create dynamic and stunning pages.
8. "python-shell" was used as a client between the frontend and backend

### What's next for L++
1. Provide an interface that allows real-time video/audio streaming
2. Allow the user to view results at real-time
3. Refine the database of jargon to be recognized
4. Experiment with translating the given text into other languages
