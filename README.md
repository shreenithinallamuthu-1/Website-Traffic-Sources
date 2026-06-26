# Website Traffic Sources


##  Internship Details

| Field | Details |
|-------|---------|
| **Intern ID** | CITS2445 |
| **Full Name** | Shreenithi Nallamuthu |
| **No. of Weeks** | 4 Weeks |
| **Project Name** | website traffic sources |
| **Project Scope** | A project scope for website traffic sources defines the deliverables, timelines, and technical requirements for analyzing where your visitors originate. Using Python, this typically involves connecting to APIs, processing channel data (organic, direct, social, paid), and generating actionable visualizations to improve marketing ROI. |

---


##  Features

- Collects website traffic information through a user-friendly CLI.
- Automatically stores data in a CSV file.
- Assigns serial numbers automatically.
- Supports multiple traffic source categories:
  - Organic Search
  - Social Media
  - Paid Ads
  - Direct / Referral / Other
- Validates user inputs.
- Generates interactive charts:
  -  Monthly Visitors Bar Chart
  -  Monthly Visitors Pie Chart
  -  Bounce Rate Bar Chart
- Automatically summarizes data using Pandas.

---

##  Project Structure

```
project/
│
├── main.py
├── website_traffic_data.csv
└── README.md
```

---

##  Requirements

Install the required libraries before running the project.

```bash
pip install pandas matplotlib
```

---

##  How to Run

Run the Python file using:

```bash
python main.py
```

---

##  Data Collection

The application asks for:

- Source Type
- Source Name
- Monthly Visitors
- Bounce Rate (%)

Example:

```
Source Type:
1. Organic Search
2. Social Media
3. Paid Ads
4. Direct / Referral / Other

Source Name:
Google

Monthly Visitors:
12000

Bounce Rate:
35.7
```

---

##  CSV Output

The data is saved in:

```
website_traffic_data.csv
```

Example:

| S.No | Source Type | Source Name | Monthly Visitors | Bounce Rate (%) |
|------|-------------|------------|-----------------:|----------------:|
| 1 | Organic Search | Google | 15000 | 35.2 |
| 2 | Social Media | Instagram | 8500 | 52.4 |
| 3 | Paid Ads | Facebook Ads | 4200 | 48.1 |

---

##  Charts Generated

After data entry is complete, the application automatically displays:

### 1. Monthly Visitors Bar Chart

Shows total visitors received from each traffic source.

---

### 2. Monthly Visitors Pie Chart

Displays the percentage contribution of each traffic source.

---

### 3. Bounce Rate Bar Chart

Shows the average bounce rate for every traffic source.

---

##  Technologies Used

- Python 3
- Pandas
- Matplotlib
- CSV Module
- OS Module

---

##  Input Validation

The program validates:

- Monthly visitors must be a positive integer.
- Bounce rate must be between **0–100%**.
- Empty source names are replaced with **"Not Specified"**.

---

##  Workflow

```
Start Program
      │
      ▼
Enter Traffic Source
      │
      ▼
Validate Input
      │
      ▼
Save Data to CSV
      │
      ▼
Add Another Source?
      │
 ┌────┴─────┐
 │          │
Yes         No
 │          │
 ▼          ▼
Repeat   Generate Charts
              │
              ▼
           End Program
```

---

##  Sample Output

The application generates:

-  Total Monthly Visitors by Traffic Source
-  Percentage Share of Monthly Visitors
-  Average Bounce Rate by Traffic Source

---

##  Future Improvements

- Export charts as PNG images.
- Generate PDF reports.
- Build a graphical user interface (GUI) using Tkinter.
- Add database support (SQLite/MySQL).
- Create an interactive dashboard using Plotly or Dash.
- Filter data by date.
- Support importing existing datasets.

---
