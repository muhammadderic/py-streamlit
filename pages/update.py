import streamlit as st
from supabase import create_client, Client

def update():
  # Supabase credentials
  url = st.secrets["SUPABASE_URL"]
  key = st.secrets["SUPABASE_KEY"]

  # Initialize Supabase client
  supabase: Client = create_client(url, key)

  # Input fields for user data
  user_id = st.number_input("Enter ID to Update", min_value=1, step=1, format="%d")
  new_name = st.text_input("New Name")
  new_age = st.number_input("New Age", min_value=1, max_value=155, step=1, format="%d")

  # Button to trigger update
  if st.button("Update"):
    # Check if ID exists
    existing_data = supabase.table("people").select("*").eq("id", user_id).execute()

    if not existing_data.data:  # Check if the result is empty
      st.warning(f"No record found for ID {user_id}.")
    else:
      # Prepare the update payload
      update_payload = {}
      if new_name:  # Only update name if provided
        update_payload["name"] = new_name
      if new_age != 1:  # Update age only if a valid input is provided (default is 1 due to min_value)
        update_payload["age"] = new_age

      # Check if there is anything to update
      if update_payload:
        response = supabase.table("people").update(update_payload).eq("id", user_id).execute()
        if response.status_code == 200:  # Success
          st.success(f"Successfully updated ID {user_id} with: {update_payload}.")
        else:  # Handle update errors
          st.error(f"Failed to update ID {user_id}. Please try again.")
      else:
        st.info("No changes made as no new input was provided.")
