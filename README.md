# Mutual Fund Transaction Dashboard

**[Live Project Link](https://github.com/your-username/mutualfund_dashboard)**

![Dashboard Screenshot]-----[(https://drive.google.com/file/d/1ByPYpRv_Tq2iChquRH1ynUNQ7IuqsQXM/view?usp=sharing)]

A full-stack web application designed to summarize mutual fund transaction activity within a selected date range. 

This project consists of:
1. **Frontend**: A pure HTML/CSS/Vanilla JavaScript application with a simple, clean UI.
2. **Backend**: A FastAPI Python backend connecting to a PostgreSQL database.

---

## Requirements Met

The dashboard precisely implements the following features:

1. **Investor-wise Purchase Summary per Mutual Fund**
   - Total purchase amount per mutual fund
   - Total NAV units purchased per mutual fund
   - Filterable by selected date range

2. **Mutual Fund-wise Summary per Investor**
   - Amount and NAV units purchased by each investor for each mutual fund
   - Filterable by selected date range

3. **Investor List with Purchase Details**
   - Investor PAN number
   - Total amount invested within the selected date range

4. **Mutual Fund Summary**
   - Total amount invested across all investors
   - Total NAV units purchased
   - Average NAV price per mutual fund

---

## 1. Prerequisites and Tools Required

To run this project locally, ensure you have the following installed on your system:
- **Python 3.8+**: Required for the backend.
- **pip**: Python package manager.
- **A Modern Web Browser**: Google Chrome, Firefox, Safari, or Edge to view the frontend.

### Backend Dependencies
The backend requires the following Python libraries (typically found in `Backend/requirements.txt`):
- `fastapi`
- `uvicorn`
- `sqlalchemy`

---

## 2. How to Setup

### Backend Setup
1. Open your terminal or command prompt.
2. Navigate to the backend directory:
   ```bash
   cd c:\mutualfund_dashboard\Backend
   ```
3. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate

   ```
4. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy
   # OR if a requirements.txt exists:
   pip install -r requirements.txt
   ```

### Frontend Setup
The frontend uses pure Vanilla JS and HTML, so **no Node.js, npm, or build steps are required.**
You simply need to know where your `Frontend/index.html` file is located.

---

## 3. How to Run the Code

### Start the Backend Server
From within the `Backend` directory, start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```
You should see output indicating that the server is running on `http://127.0.0.1:8000`. Leave this terminal window open.

### Open the Frontend
1. Navigate to the `Frontend` folder on your computer.
2. Double-click the `index.html` file to open it in your default web browser.
3. *Alternatively*, you can use a simple local server if preferred (e.g., VS Code Live Server, or running `python -m http.server 3000` in the Frontend folder).

---

## 4. How to See the Output Details

Once the backend is running and you have opened `index.html` in your browser:

1. **Viewing Data:** The dashboard will immediately fetch all transactions from the backend and populate the four required tables.
2. **Filtering by Date:** 
   - Use the "From Date" and "To Date" input fields in the top header.
   - Click **"Apply Filter"**.
   - The frontend will send the date range to the backend API, which will recalculate and return the exact summaries for that specific period.
   - The 4 tables will instantly update to reflect the filtered data.
3. **Resetting:** Click the **"Reset"** button to clear the dates and view the all-time summaries again.

---

## API Contracts

The backend exposes the following four REST API endpoints to power the dashboard components. 

*Base URL: `http://localhost:8000/api/v1`*

### 1. Investor-wise Purchase Summary
* **Endpoint:** `GET /investor-purchase-summary`
* **Query Parameters:** `from_date` (YYYY-MM-DD), `to_date` (YYYY-MM-DD)
* **Response (JSON):**
  ```json
  [
    {
      "inv_name": "string",
      "pan": "string",
      "scheme": "string",
      "total_amount": "number",
      "total_units": "number"
    }
  ]
  ```

### 2. Mutual Fund-wise Summary per Investor
* **Endpoint:** `GET /mutualfund-investor-summary`
* **Query Parameters:** `from_date` (YYYY-MM-DD), `to_date` (YYYY-MM-DD)
* **Response (JSON):**
  ```json
  [
    {
      "scheme": "string",
      "inv_name": "string",
      "pan": "string",
      "total_amount": "number",
      "total_units": "number"
    }
  ]
  ```

### 3. Investor List with Purchase Details
* **Endpoint:** `GET /investors`
* **Query Parameters:** `from_date` (YYYY-MM-DD), `to_date` (YYYY-MM-DD)
* **Response (JSON):**
  ```json
  [
    {
      "inv_name": "string",
      "pan": "string",
      "total_investment": "number"
    }
  ]
  ```

### 4. Mutual Fund Summary
* **Endpoint:** `GET /mutualfund-summary`
* **Query Parameters:** `from_date` (YYYY-MM-DD), `to_date` (YYYY-MM-DD)
* **Response (JSON):**
  ```json
  [
    {
      "scheme": "string",
      "total_amount": "number",
      "total_units": "number",
      "avg_nav": "number"
    }
  ]
  ```

---
*Time Estimate for Implementation: ~5 hours.*
Task	Time
Requirement Analysis & API Contract Design   ----	30 mins
Backend API Development (4 endpoints)	       ---- 2 hrs
Frontend Dashboard UI Development	           ---- 1.5 hrs
API Integration & Filters                    ----	30 mins
Testing & Bug Fixes                          ----	30 mins
Total                                        
