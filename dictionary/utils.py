import json
import os


def main_menu():
    print("\n=== Main Menu ===")

    menu_items = {
        "1" : "Search",
        "2" : "Add to Favorites",
        "3" : "View Search Histories",
        "0" : "Exit Program"
    }

    for ind, menu in menu_items.items():
        print(f"{ind}. {menu}")
    print("-" * 25)


def load_vocabs():
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, 'data', 'vocab_list.json')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = json.load(file)
        return words
    
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def favorite_menu():
    print("\n=== Favorite Menu ===")

    favorite_items = {
        "1" : "Add to Favorites",
        "2" : "View Favorites",
        "3" : "Remove Favorites",
        "4" : "Clear Favorites",
        "0" : "Return Back"
    }

    for ind, val in favorite_items.items():
        print(f"{ind}. {val}")
    print("-" * 25)


def save_favorites(fav_list, filename='favorites.json'):
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(fav_list, file, ensure_ascii=False, indent=2)
    

def load_favorites(filename="favorites.json"):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            favorite = json.load(file)
        return favorite

    except (FileNotFoundError, json.JSONDecodeError):
        return []
    

def history_menu():
    print("\n=== History Menu ===")

    history_items = {
        "1" : "View Histories",
        "2" : "Clear Histories",
        "0" : "Return Back"
    }

    for key, val in history_items.items():
        print(f"{key}. {val}")
    print("-" * 25)
    

def save_history(search_list, filename="search_history.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(search_list, file, ensure_ascii=False, indent=2)


def load_history(filename="search_history.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            history = json.load(file)
        return history

    except (FileNotFoundError, json.JSONDecodeError):
        return []
    