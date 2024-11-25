import os
import streamlit as st
from supabase import create_client, Client

def create():
  url = st.secrets["SUPABASE_URL"]
  key = st.secrets["SUPABASE_KEY"]

  url: str = os.environ.get("SUPABASE_URL")
  key: str = os.environ.get("SUPABASE_KEY")

  supabase: Client = create_client(url, key)

  name = st.text_input("Name")
  age = st.number_input("Age", min_value=1, max_value=155, step=1, format="%d")

  if st.button("Submit"):
    data = supabase.table("people").insert({"name": name, "age": age}).execute()