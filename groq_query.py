
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  
    temperature=0.0,
)

import re

def extract_sql(text):
    match = re.search(r"```sql\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()

    match = re.search(r"(SELECT[\s\S]*?;)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    return None


def translate_to_sql(user_query):
    prompt = f"""
    You are a product recomendation guy and have to create query which find  similar products to query
    Also read schema  and according to it create a proper query by using resoning on schema and query relation
    also capture the semantic of the query what user want 
    if a query have to check multiple condition then use OR instead of AND
    Convert the following natural language request into an SQL query.
    Table: products
    Columns:     id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        price REAL,
        brand TEXT
    Return ONLY SQL.

    User request: "{user_query}"
"""
    result = llm.invoke(prompt)
    return extract_sql(result.content.strip())
