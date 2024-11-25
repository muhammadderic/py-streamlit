from streamlit_option_menu import option_menu

from pages.create import create
from pages.read import read
from pages.update import update

def menu():
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Create", "Read", "Update", "Delete"],
    orientation = "horizontal",
    styles = {
      "container": {"padding": "0!important", "background-color": "#000", "font-style": "bold"},
      "nav-link": {"font-size": "25px", "--hover-color": "#1F201F"},
      "nav-link-selected": {"background-color": "#fff", "color": "#000"},
    }
  )

  if selected == "Create":
    create()
  elif selected == "Read":
    read()
  elif selected == "Update":
    update()