# ChatUX

A simple chat application using FastAPI backend and HTML frontend.

## Project Structure

```
chatux/
│
├── api.py
├── index.html
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.7+ or Miniconda
- pip (Python package installer)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/gavi/chatux.git
   cd chatux
   ```

2. Set up the environment:

   Option A: Using Python's built-in venv (virtual environment):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

   Option B: Using Miniconda:
   ```
   conda create -n chatux python=3.9
   conda activate chatux
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a `.env` file in the project root directory
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Running the Application

1. Start the FastAPI server:
   ```
   python api.py
   ```
   The API will be available at `http://localhost:8000`.

2. In a separate terminal, serve the HTML file using Python's built-in HTTP server:
   ```
   python -m http.server 8080
   ```
   The frontend will be available at `http://localhost:8080`.

3. Open your web browser and navigate to `http://localhost:8080` to use the chat application.

## API Endpoints

- POST `/chat`: Send chat messages to the OpenAI API and receive streamed responses.

## Notes

- Make sure both the API server and the HTTP server are running simultaneously.
- The frontend is a simple HTML file. You may want to enhance it with CSS and JavaScript for a better user experience.
- Remember to keep your OpenAI API key confidential and never commit it to version control.
- If using Miniconda, ensure you activate the `chatux` environment before running the application.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/gavi/chatux/issues) if you want to contribute.