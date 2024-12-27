Local AI Chatbot by John O'Dell

Items Needed:

    - VSCode IDE - https://code.visualstudio.com/download
    - Postman API client - https://www.postman.com/
    - Ollama Language Models - https://ollama.com/

Setting Up the Ollama Language Model(s)

    - Open Command Prompt/Terminal
    - Type the command below to make sure it has downloaded correctley
        ollama
    - Type the command below to Download the llama3 model (the model used in the example)
        ollama pull llama3
            - Visit the ollama README to see every model available, a larger model may not be "better" due to the response time. There are general guidlines for the specifications needed and the model size.
    - The download will take some time

Testing the Llama3 Model

    - Type in the command below to start the llama3 model
        ollama run llama3
    - if you downloaded a different model, replace "llama3" with your model
    - Type in the phrase
        hello world
    - You will get a response in the termal/command prompt window
    - Feel free to try other phrases
    - To exit, Type in the command below
        /bye

Setting up a virtual environment in VSCode

    - Create a new folder in VScode
    - Open the Terminal 
        - Type and run the following commands
            python -m venv chatbot
            source chatbot/bin/activate
    - Once the chatbot venv is activated install the following packages
        -Type and run the following commands
             pip install langchain
             pip install langchain-ollama
             pip install ollama
             pip install Flask

Command Line Chatbot (main.py)

    - Create a new file called main.py in the chatbot environment
    - Copy and paste the code from the example named "main.py"
    - Press the run arrow in the top right or in the termal type
        python main.py
    - Start having a Conversation in the terminal with the Chatbot
    - To end the chat type in the terminal
        exit

Local Host Chatbot 

    - Create a new file called app.py
    - Copy and paste the code from the example named "app.py"
        - Press the run arrow or in the terminal type
            python app.py
        - copy the IP addess 
            127.x.x.x:xxxx
    - Download and open the Postman App
        - In the top left click "New"
        - Paste the IP adress with ending /chat
            127.x.x.x:xxxx/chat
        - Click on "body" underneath 
        - Select "raw"
        - paste this into the space underneath
                
                {
                 "context": "",
                 "question": "Hello, how are you?"
                    }
        
        - Click send to make sure there is a response
        - Click save, above the send button if a response is recieved

    - Open the 127.x.x.x:xxxx in a broswer
    - if the chat does not appear here or redirected add the /chat to the end of the address

Troubleshooting:

    - Keywords can depend on Mac/Windows/Linux, if recieving a python error trying subsituting python3 as a keyword
    - Make sure all Libraries are downloaded and the kernal restarted
    - The Postman app call must be SAVED not just "send". This will result in a 404 or 403 error if not SAVED
    - End the "main.py" before you run the "app.py"

    