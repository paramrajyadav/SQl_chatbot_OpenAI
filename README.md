# SQL Chatbot

This project implements a chatbot capable of interacting with a SQL database to answer user queries. The chatbot leverages the OpenAI API for natural language understanding and response generation.

## Features

- Connects to a PostgreSQL database to execute SQL queries.
- Utilizes the OpenAI API to process natural language input and generate responses.
- Provides a conversational interface for users to interact with the database.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your_username/sql-chatbot.git
cd sql-chatbot
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your environment variables by creating a `.env` file in the project directory and adding the following variables:

```dotenv
db_name="your_database_name"
db_user="your_database_user"
db_password="your_database_password"
db_host="your_database_host"
db_port="your_database_port"
OPENAI_API_KEY="your_openai_api_key"
```

Replace the placeholders with your actual database connection details and OpenAI API key.

## Usage

1. Start the chatbot by running the following command:

```bash
python app.py
```

2. Interact with the chatbot by entering queries or questions about the database.

3. The chatbot will process your input, execute SQL queries if necessary, and provide responses accordingly.

4. To exit the chatbot, simply type "exit" and press Enter.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
