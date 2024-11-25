import pandas as pd
import streamlit as st
from supabase import create_client, Client

def read():
  url = st.secrets["SUPABASE_URL"]
  key = st.secrets["SUPABASE_KEY"]

  # Initialize Supabase client
  supabase: Client = create_client(url, key)

  # Fetch data from Supabase
  listData = supabase.table("people").select("*").execute().data

  # Create a DataFrame with all rows
  df = pd.DataFrame(columns=['No', 'Name', 'Age'])

  for i in range(0, len(listData)):
    df.loc[i] = [listData[i]['id'], listData[i]['name'], listData[i]['age']]

  # Alternate (line: 15-19)
  # df = pd.DataFrame(listData)  # Automatically converts JSON-like data to a DataFrame

  # Display the DataFrame
  st.dataframe(df)