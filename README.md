# Mail Application in Python

This project aims to create a mail application in Python that allows users to send and receive email messages. The application supports various file types, including text files, word documents, presentations, and images in formats such as JPEG and PNG. It involves interacting with mail servers to handle sending and receiving of messages.

## Key Features

The mail application in Python offers the following key features:

- Support for multiple protocols: The application supports protocols like SMTP (Simple Mail Transfer Protocol) for sending emails and IMAP (Internet Message Access Protocol) for receiving emails.
- Attachments and rich media: Users can attach various types of files to their emails, including text files, documents, presentations, and images.
- Multiple recipients: The application allows sending emails to multiple users simultaneously.
- Receiver side: The application provides a user interface to view received mails, including the time of receipt.
- Mail bot: An automated mail bot feature allows users to send pre-written text messages automatically.
- Voice recognition bot: The application includes a voice recognition bot that enables users to interact with the mail system using voice commands.
- Mail statistics: The project displays a bar graph using the matplotlib library, showing the number of mails received per day.

## Dependencies

The mail application relies on the following libraries and modules:

- `smtplib`: Used for interacting with SMTP servers to send emails.
- `imaplib`: Used for interacting with IMAP servers to receive emails.
- `matplotlib`: Used for generating the bar graph displaying mail statistics.

## Getting Started

To run the mail application, follow these steps:

1. Clone the project repository from GitHub:

   ```shell
   git clone https://github.com/barath-sk17/Mail_working_py
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Open the project in your Python IDE or text editor.

4. Configure the mail server settings, including the SMTP and IMAP server addresses, ports, and login credentials.

5. Explore the project files to understand the different components, including sending emails, receiving emails, mail bot, voice recognition bot, and mail statistics.

6. Interact with the mail application through the user interface and explore its various features.


## Acknowledgements

- The mail application in Python is built upon the functionalities provided by the `smtplib` and `imaplib` libraries.
- The bar graph for mail statistics is generated using the `matplotlib` library.
- Special thanks to the contributors and maintainers of the above libraries for their invaluable work.
