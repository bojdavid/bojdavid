<h1>Exploratory Data Analysis (EDA) on Global Terrorism Dataset</h1>
<p>
  This project explores the Global Terrorism Database from Kaggle, featuring 17 fields and 3,013 entries. The analysis was conducted using SQL to extract key insights and identify patterns in terrorist activities over time, regions, and attack types.<br>
</p>
<h2>SQL Analysis Tasks</h2> 

<h3>Primary Key Assignment:</h3>
<ul>
  <li>Added a new primary key as no suitable identifier was present in the dataset.</li>
  <li>Moved the primary key column to the first position for better organization.</li>
</ul>

<h3>Column Analysis:</h3>
<ul>
  <li>Counted the number of unique values in each column.</li>
  <li>Counted the number of empty (null) values in each column.</li>
</ul>

<h3>Data Cleaning:</h3>
<ul>
  <li>Removed records where "killed" and "wounded" fields had null values.</li>  
</ul>

<h3>Statistical Calculations:</h3>
<ul>
 <li> Computed the average, minimum, maximum, and total numbers for people killed and wounded.</li>
</ul>

<h3>Grouping and Aggregation:</h3>
Performed group-by analysis for the following fields:
<ul>
  <li> Attack Type </li>
  <li> Weapon Type </li>
  <li> Target Type </li>
  <li> Region </li>
  <li> Year </li>
</ul>

<h3>Tableau Visualization </h3>
The visualizations highlight crucial patterns, making it easy to identify the most targeted regions, common attack methods, and affected groups.<br>
<a href = "https://public.tableau.com/views/terrorismA_June2024Trial/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"> Tableau Visualization </a>

<h3>Dataset Source</h3>
The dataset was sourced from Kaggle and provides a comprehensive look into global terrorism incidents.<br>
<a href = "https://www.kaggle.com/datasets/adiagarwalrock/terrorism-data-1970to2017"><b>Terrorism Data</b></a>


