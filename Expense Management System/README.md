
---

# Expense Management System 💰  

Track, analyze, and manage your expenses efficiently with this streamlined Expense Management System. The application includes a FastAPI backend for database operations and a Streamlit frontend for interactive expense management and visualization.  

## Features 🚀  
1. **Add/Update Expenses** 📝  
   Record and modify your daily expenses with categories like Rent, Food, Shopping, and more.  
2. **Category Analysis** 📊  
   Visualize expense breakdown by categories over a specified date range.  
3. **Monthly Trends** 📅  
   Track monthly expense trends with an interactive bar chart and summary table.  

---

## Project Structure 🗂️  
- **frontend/**: Contains the Streamlit application code.  
- **backend/**: Contains the FastAPI backend server code.  
- **tests/**: Contains the test cases for both frontend and backend.  
- **requirements.txt**: Lists the required Python packages.  
- **README.md**: Provides an overview and instructions for the project.  

---

## Workflow Overview 🛠️  
1. User interacts with the Streamlit frontend.  
2. Streamlit communicates with the FastAPI backend.  
3. Backend performs CRUD operations and analytics using a MySQL database.  

**Workflow Diagram Placeholder**  
*(Insert your workflow image here)*  

---

## Application Architecture  

### **Frontend Layer - Streamlit**  
- **Main App**  
  - **Tab Navigation**  
    - **Add/Update Tab**  
      - GET/POST: `/expenses/{date}`  
    - **Category Analysis Tab**  
      - POST: `/analytics`  
    - **Monthly Trends Tab**  
      - GET: `/months`  

### **API Layer - FastAPI**  
- `/expenses/{date}` (GET/POST)  
- `/analytics` (POST)  
- `/months` (GET)  

### **Database Layer**  
- **MySQL Database**  

---

### **Data Flow**  
1. The **Main App** in Streamlit allows users to navigate between tabs.  
2. Each tab interacts with the API endpoints:  
   - Add/Update Tab → `/expenses/{date}` for retrieving or saving expenses.  
   - Category Analysis Tab → `/analytics` for analytics operations.  
   - Monthly Trends Tab → `/months` for fetching trend data.  
3. API endpoints communicate with the **MySQL Database** for data persistence.  

---


## Tabs in the Application 🖥️  
- **Add/Update Expenses:** Manage expenses by selecting a date, amount, category, and notes.  
  *(Insert image of Add/Update Expenses tab here)*  
- **Category Analysis:** View category-wise expense breakdown with percentages and bar charts.  
  *(Insert image of Category Analysis tab here)*  
- **Monthly Trends:** Explore expense trends over months with detailed insights.  
  *(Insert image of Monthly Trends tab here)*  

---

## Technical Stack 🛠️  

### Backend:  
- **FastAPI:** RESTful API for handling expense data.  
- **MySQL:** Database for storing expense records.  
- **Pydantic:** Validation of request and response models.  

### Frontend:  
- **Streamlit:** Interactive dashboards for user-friendly visualization.  

### Testing:  
- **Postman:** Used for testing API endpoints.  

### Logging:  
- **Custom Logger:** Tracks API requests and database interactions for debugging and monitoring.  

---

## API Endpoints  
1. **GET /expenses/{expense_date}**: Retrieve expenses for a specific date.  
2. **POST /expenses/{expense_date}**: Add or update expenses for a specific date.  
3. **POST /analytics/**: Get a summary of expenses by category for a date range.  
4. **GET /months/**: Fetch a summary of expenses grouped by months.  

---

## How to Run Locally 🖥️  
1. Clone this repository.  
2. Setup MySQL and configure the `db_helper.py` connection.  
3. Run the FastAPI server: `uvicorn server:app --reload`.  
4. Start the Streamlit frontend: `streamlit run app.py`.  

---

## Future Enhancements 🌟  
- Implement user authentication.  
- Add data export functionality.  

---
