# Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/joelk9895/loopey-backend.git
   cd loopey-backend
   ```

2. **Install dependencies:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**

   - Copy `.env.example` to `.env` and update the values as needed.

4. **Run the development server:**

   ```bash
   fastapi dev app/main.py
   ```

5. **Access the API:**
   - The server will start on `http://localhost:8000` by default.
