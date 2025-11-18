# A FastAPI Application

An application using FastAPI framework.

## Test Application

1. Open `Git Bash` shell.

2. Create a virtual environment.

   **RUN:**

   For Linux / MacOS:

   ```console
   python3 -m venv venv
   ```

   For Windows:

   ```console
   python -m venv venv
   ```

3. Activate the virtual environment.

   **RUN:**

   For Linux / MacOS:

   ```console
   source ./venv/bin/activate
   ```

   For Windows:

   ```console
   source ./venv/Scripts/activate
   ```

4. Install dependencies.

   **RUN:**

   ```console
   pip install -r requirements.txt
   ```

5. Change into subdirectory **`app`**.

   **RUN:**

   ```console
   cd app
   ```

6. Run the application.

   **RUN:**

   ```console
   uvicorn --host 0.0.0.0 --port 7000 --reload main:app
   ```

6. Open a browser using URL <http://localhost:7000/docs>.
   Try sending a request to test some endpoints.
