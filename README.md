#  Book Recommendation System

This project is a simple **book recommendation system** built using Python. It suggests books that are similar to each other based on genres, and tags. The final app was made using **Streamlit** so you can see the recommendations in a nice dashboard.

---

## Table of Contents
- [What This Project Does](#what-this-project-does)
- [Project Folder Structure](#project-folder-structure)
- [Datasets Used](#datasets-used)
- [How to Run This Project on Your Computer](#how-to-run-this-project-on-your-computer)
- [Summary Report](#summary-report)
- [Histogram Insights](#histogram-insights)
- [Features of the App](#features-of-the-app)
- [Contact](#contact)

---

##  What This Project Does

- Loads book data from real-world datasets.
- Cleans and prepares the data.
- Uses **cosine similarity** to find books that are similar.
- Recommends books to users based on one they already like.
- Shows the results in an interactive web app (dashboard).

---

##  Project Folder Structure

Here is how the project is organized:

| Folder       | File / Subfolder                  | Description                                                  |
|--------------|---------------------------------|--------------------------------------------------------------|
| data         | `raw/`                          | Original datasets (Goodbooks-10k, Book-Crossing CSV files)   |
|              | `processed/`                    | Cleaned and preprocessed data ready for analysis             |
| notebooks    | `*.ipynb`                      | Jupyter Notebooks for EDA, feature engineering, and testing  |
| app          | `app.py`                       | Streamlit app script to launch the recommendation dashboard  |
| reports      | `histogram_report.md`          | Markdown report with histogram images and analysis           |
|              | `summary_report.pdf`           | Final 1-2 page project summary with findings                  |
| requirements.txt |                             | Python packages required to run the project                   |
| README.md    |                                | Project documentation and usage instructions                  |

---

##  Datasets Used

We used two datasets for books and ratings:

1. **Goodbooks-10k Dataset**  
   🔗 https://github.com/zygmuntz/goodbooks-10k

2. **Book-Crossing Dataset**  
   🔗 https://grouplens.org/datasets/book-crossing

These include book titles, authors, tags, and user ratings.

---

##  How to Run This Project on Your Computer

### Step 1: Download the project

You can download this project by:
- Cloning it from GitHub, or
- Downloading the ZIP file and unzipping it.

If you're using Git, run this in your terminal:

git clone https://github.com/Safvi/capstone8-recommender.git
>cd capstone8-recommender

### Step 2:Tools & Technologies

- Python 
(pip install -r requirements.txt)
- CSV datasets
- Streamlit

### Step 3: How to Use

- Load datasets
- Inside the terminal, run this: streamlit run app/app.py 

---

##  Summary Report

We also made a short 1–2 page report with graphs and explanations. You can find it in the `reports/` folder.

---

##  Histogram Insights

A separate Markdown report that contains histogram visualizations and insights about:

- Rating distribution
- Number of ratings per user
- Books with more than 500 ratings

[Click here to view the histogram insights](reports/histogram_insights.md)

---

##  Features of the App

- Recommends similar books based on what you select
- Uses content-based filtering with cosine similarity
- Simple and clean Streamlit dashboard to show results

---

## Contact
Syeda Rizvi 