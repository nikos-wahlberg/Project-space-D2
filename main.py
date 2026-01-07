"""
The most popular functions when using Pandas:

1. Data Ingestion & Inspection
Before you can work, you have to see what you have.

pd.read_csv() / pd.read_excel(): The starting point for almost every project.

df.head(): Shows the first 5 rows. It's the first thing every coder types to verify the load worked.

df.info(): The most important "health check." It shows you missing values (nulls) and data types (integers vs. strings).

df.describe(): Provides a statistical summary (mean, max, min, standard deviation) for all numerical columns.

2. Selection & Filtering
Getting exactly the data you need from a large table.

df['column_name']: Selects a single column.

df.loc[]: Selects data by label (e.g., "Find the row where the ID is 'A101'").

df.iloc[]: Selects data by integer position (e.g., "Give me the first 10 rows and first 3 columns").

Boolean Indexing: Filtering rows based on conditions, like df[df['age'] > 25].

3. Data Cleaning (Crucial for AI)
AI models fail if the data is "dirty." These functions fix that.

df.dropna(): Removes rows with missing values.

df.fillna(value): Replaces missing values with a specific number or the average (mean).

df.drop_duplicates(): Ensures every row in your dataset is unique.

df.rename(): Changes column names (useful for fixing messy Excel headers).

4. Transformation & Aggregation
This is where the actual "Engineering" happens.

df.groupby(): The powerhouse function. It allows you to group data (like by "City") and calculate totals or averages for each group.


df.apply(): Runs a custom Python function on every single row in a column.

df.merge(): Similar to a SQL JOIN. It combines two different tables based on a shared column (like a User ID).

df.pivot_table(): Creates an Excel-style summary table.

5. Exporting Results
df.to_csv(): Saves your cleaned data back to a file.

df.to_json(): Common when sending data to a web application or an AI API.

"""