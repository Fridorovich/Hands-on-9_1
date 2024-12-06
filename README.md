# Pipes-and-filters system

## Description

The system consists of four services:
1. REST API server for receiving messages from users.
2. Filter is a service for filtering messages by stop words.
3. SCREAMING service for converting text to uppercase.
4. Publish service for sending emails.

## Project structure

```
project/
│
├── app/
│ ├── init.py
│ └── app.py
│
├── filters/
│ ├── init.py
│ ├── filter_service.py
│ ├── screaming_service.py
│ └── publish_service.py
│
├── pipe.py
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## Installation and launch

1. **Install dependencies**:
- Install dependencies using pip:
```bash
pip install -r requirements.txt
```

2. **Configure the `.env` file**:
- Create a `.env` file in the root directory of the project and add environment variables to it:
     ```env
     SMTP_SERVER=mail.innopolis.ru
     SMTP_PORT=587
     SMTP_USER=your_email
     SMTP_PASSWORD=your_password
     RECIPIENT_EMAIL=recipient_email1,recipient_email2,...
     ```

3. **Start the server**:
- Start the server using the command:
     ```bash
     python main.py
     ```

4. **Sending a message via the REST API**:
- Use `Invoke-WebRequest` in PowerShell to send a POST request to `/send`:
     ```powershell
     Invoke-WebRequest -Uri http://localhost:5000/send -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"user": "test_user", "message": "Hello, world!"}'
     ```

## Checking the result

1. **Check the recipient's email**:
- Open the email `recipient_email`.
   - Find a new email with the subject "New Message".
   - Check the text of the letter:
     ```
     From the user: test_user
     Message: HELLO, WORLD!
     ```

## Pipes-and-filters system

In this variant each filter operates in a separate process and data is transmitted through channels (queues).

#### Advantages:
- Ease of implementation.

- Ease of debugging and testing.

#### Disadvantages:
- Possible problems with synchronization and locks.

- Higher resource consumption due to the use of processes.
