import streamlit as st
from st_supabase_connection import SupabaseConnection

st.title("Hello Deric")
st.write("This is a simple example of a Streamlit app.")

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="mytable", ttl="10m").execute()

# Print results.
for row in rows.data:
    st.write(f"{row['name']} has a :{row['pet']}:")