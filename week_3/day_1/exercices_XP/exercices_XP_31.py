#question 1
""" What is Data Analysis?
Data analysis is the process of collecting, organizing, and examining data to find useful information and patterns. It helps turn raw data into meaningful insights that support decision-making.

Why is Data Analysis Important?
Data analysis is important because it helps organizations understand information and make better decisions. In today’s digital world, large amounts of data are generated every day, and analyzing this data helps improve efficiency, predict trends, and solve problems.

Areas Where Data Analysis is Applied
Data analysis is widely used in many fields today. In business, companies analyze sales and customer data to improve products and marketing strategies. In healthcare, doctors and researchers study patient data to understand diseases and improve treatments. In education, schools analyze student performance data to improve teaching methods and learning outcomes. """

#exercice 2
import pandas as pd


sleep_data = pd.read_csv("sleep_data.csv")
sleep_data.head()

mental_health_data = pd.read_csv("mental_health_data.csv")
mental_health_data.head()

credit_data = pd.read_csv("credit_data.csv")
credit_data.head()

#exercice 3

def identify_types(df):
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            print(column, "- Quantitative (numerical values)")
        else:
            print(column, "- Qualitative (categories or text)")

print("Sleep Dataset:")
identify_types(sleep_data)

print("\nMental Health Dataset:")
identify_types(mental_health_data)

print("\nCredit Card Dataset:")
identify_types(credit_data)

#exercice 4
# load the iris dataset
iris = pd.read_csv("Iris.csv")

# display first rows
print(iris.head())

# display data types
print("\nData types:")
print(iris.dtypes)

#exercice 5

# load the dataset
sleep_data = pd.read_csv("sleep_data.csv")

# display the first rows
print(sleep_data.head())

# display column names
print("\nColumns in the dataset:")
print(sleep_data.columns)

#exercice 6
""" A company’s financial reports stored in an Excel file – Structured data
The data is organized in rows and columns with a clear format, making it easy to analyze.

Photographs uploaded to a social media platform – Unstructured data
Images do not follow a predefined structure like tables or databases.

A collection of news articles on a website – Unstructured data
Articles consist mostly of free text, which does not follow a fixed data structure.

Inventory data in a relational database – Structured data
The data is organized into tables with defined fields and relationships.

Recorded interviews from a market research study – Unstructured data
Audio recordings do not have a predefined structure and require processing to analyze. """

#exercice 7

""" Blog posts about travel experiences – Use text analysis to extract information such as destination, dates, and activities, and store it in a table.

Audio recordings of customer service calls – Use speech-to-text transcription, then extract key fields like issue type, call duration, and resolution.

Handwritten notes from a brainstorming session – Use OCR (Optical Character Recognition) to convert handwriting into text, then organize ideas into categories.

Video tutorial on cooking – Transcribe the video and extract structured information such as recipe name, ingredients, and steps. """

#exercice 8

# load the dataset
train_data = pd.read_csv("train.csv")

# display the first rows
print(train_data.head())

#exercice 9
data = {
    "Name": ["Sixtine", "Ruben", "Yael"],
    "Age": [17, 18, 16],
    "City": ["Tel-Aviv", "Jerusalem", "Brussels"]
}

df = pd.DataFrame(data)

# export to Excel
df.to_excel("data.xlsx", index=False)

# export to JSON
df.to_json("data.json", orient="records")

print(df)

#exercice 9

# JSON dataset URL
url = "https://jsonplaceholder.typicode.com/posts"

# read the JSON data
data = pd.read_json(url)

# display the first five entries
print(data.head())