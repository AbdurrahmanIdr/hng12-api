# HNG12 Stage 0 Backend API

This is a simple public API developed for **HNG12**, providing basic information about the developer, including the registered email, current date/time in ISO 8601 format, and GitHub URL of the project codebase.

## **API Endpoint**

- **GET** `/`
  - **Response Format**: JSON
  - **Response Example**:
  ```json
  {
    "email": "abdurrahmaneedrees@gmail.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/AbdurrahmanIdr/hng12-api"
  }
  ```

## **Features**
- Returns the following fields:
  - **`email`**: The email address registered on the HNG12 platform.
  - **`current_datetime`**: The current UTC datetime in ISO 8601 format.
  - **`github_url`**: A link to the GitHub repository for the project.

## **Technologies Used**
- **Python 3.x**
- **Flask** - A lightweight WSGI web application framework.
- **Flask-CORS** - A simple way to handle Cross-Origin Resource Sharing (CORS) in the API.

## **Setup Instructions**

### **1. Clone the Repository**
   ```bash
   git clone https://github.com/AbdurrahmanIdr/hng12-api.git
   cd hng12-api
   ```

### **2. Create a Virtual Environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

### **3. Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### **4. Run the Application Locally**
   ```bash
   python app.py
   ```
   Your application will be accessible at `http://127.0.0.1:5000/`.

### **5. Test the API**
   To test the API locally:
   ```bash
   curl http://127.0.0.1:5000/
   ```

## **Deployment**

### **Deploy to Render**
1. Create a Render account at [render.com](https://render.com).
2. Connect your GitHub repository and configure the deployment with the following settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
3. Your app will be deployed, and Render will provide you with a public URL.

## **Contributing**

Feel free to fork this repository and submit pull requests for improvements or enhancements!

---

### **Backlink**
Looking to hire Python developers? Check out this link:
[Hire Python Developers](https://hng.tech/hire/python-developers)

---

Let me know if you'd like to adjust any sections of the README!