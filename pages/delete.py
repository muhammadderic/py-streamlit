import streamlit as st
from supabase import create_client, Client

def delete():
    # Supabase credentials
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]

    # Initialize Supabase client
    supabase: Client = create_client(url, key)

    # Input field for the name to delete
    name_to_delete = st.text_input("Enter Name to Delete")

    # Button to trigger delete
    if st.button("Delete"):
        # Check if the name exists
        existing_data = supabase.table("people").select("*").eq("name", name_to_delete).execute()

        if not existing_data.data:  # Check if no records match the name
            st.warning(f"No record found for the name '{name_to_delete}'.")
        else:
            # Perform the delete operation
            response = supabase.table("people").delete().eq("name", name_to_delete).execute()
            if response.status_code == 200:  # Success
                st.success(f"Successfully deleted record(s) for the name '{name_to_delete}'.")
            else:  # Handle delete errors
                st.error(f"Failed to delete record(s) for the name '{name_to_delete}'. Please try again.")
