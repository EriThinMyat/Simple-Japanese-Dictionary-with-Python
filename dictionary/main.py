from utils import load_vocabs, main_menu, favorite_menu, save_favorites, load_favorites, history_menu, save_history, load_history

class JapDictionary:

    def __init__(self):
        self.vocab_list = load_vocabs() or []
        self.history = load_history() or []
        self.favorite = load_favorites() or []


    def get_choice(self, prompt = "Choose... "):
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input.")
            return None
        

    def matched_vocab(self, vocab: dict, keyword: str) -> bool: 
        return (keyword in vocab['word'] or 
                keyword in vocab['reading'] or 
                keyword.lower() in vocab['meaning'].lower())


    def choose(self) -> None:
        while True:
            main_menu()
            user_input = self.get_choice()

            if user_input == 0:
                save_history(self.history)
                save_favorites(self.favorite)
                break
            elif user_input == 1:
                self.show_vocabs()
            elif user_input == 2:
                self.choose_favorites()
            elif user_input == 3:
                self.choose_history()
            else:
                print("Invalid choice.")


    def display_vocab(self, vocab: dict) -> None:
        print(f"Word: {vocab['word']}")
        print(f"Hiragana: {vocab['reading']}")
        print(f"Meaning: {vocab['meaning']}")
        print(f"-" * 25)


    def show_vocabs(self) -> None:
        while True:
            keyword = input("Search a word... ").strip()
            if keyword.lower() == "q" or keyword == "":
                break

            found = False
            updated = False
            for vocab in self.vocab_list:
                if self.matched_vocab(vocab, keyword):
                    found = True
                    self.display_vocab(vocab)
                    if not any(v['word'] == vocab['word'] for v in self.history):
                        self.history.append(vocab)
                        updated = True

            if updated:
                save_history(self.history)
    
            if not found:
                print("No matching vocabulary found.")
        

    def add_favorites(self) -> None:
        while True:
            choice = input("Choose word to add favorites... ").strip().lower()
            if choice.lower() == "q" or choice == "":
                break

            matched = False
            for i, vocab in enumerate(self.history, 1):
                if self.matched_vocab(vocab, choice):
                    if vocab not in self.favorite:
                        self.favorite.append(vocab)
                        save_favorites(self.favorite)
                        print(f"Add to Favorites")
                        print(f"{i}.")
                        self.display_vocab(vocab)
                    else:
                        print(f"{vocab['word']} is already in favorites.")
                    matched = True
            if not matched:
                print("Vocab not found in search history.")

        
    def choose_favorites(self) -> None:
        while True:
            favorite_menu()
            choose = self.get_choice()

            if choose == 0:
                break
            elif choose == 1:
                self.add_favorites()
            elif choose == 2:
                self.show_favorites()
            elif choose == 3:
                self.remove_favorites()
            elif choose == 4:
                self.clear_favorites()


    def empty_favorites(self) -> bool:
        if not self.favorite:
            print("You haven't added any favorites yet.")
            return True
        return False


    def show_favorites(self) -> None:
        if self.empty_favorites():
            return
        
        print("\n=== Favorites ===\n")
        for vocab in self.favorite:
            self.display_vocab(vocab)

        
    def remove_favorites(self) -> None:
        if self.empty_favorites():
            return
        
        word = input("Enter word or hiragana to remove from favorite... ").strip()

        if word.lower() == "q" or word == "":
            return
        
        removed = False
        for vocab in self.favorite[:]:
            if self.matched_vocab(vocab, word):
                self.favorite.remove(vocab)
                save_favorites(self.favorite)
                print(f"Removed vocabulary from favorite: {vocab['word']} - {vocab['reading']} - {vocab['meaning']}")
                removed = True
                break
        if not removed:
            print("Vocabulary not found in favorite.")


    def clear_favorites(self) -> None:
        if self.empty_favorites():
            return
        
        confirm = input("Are you sure to clear all favorites? (y/n): ").strip().lower()
        if confirm == "y":
            self.favorite.clear()
            save_favorites(self.favorite)
            print("All favorites cleared.")


    def choose_history(self) -> None:
        while True:
            history_menu()
            choose = self.get_choice()

            if choose == 0:
                break
            elif choose == 1:
                self.show_history()
            elif choose == 2:
                self.clear_history()
            else:
                print("Invalid input.")
    

    def empty_history(self) -> bool:
        if not self.history:
            print("No search history yet.")
            return True
        return False
    

    def show_history(self) -> None:
        if self.empty_history():
            return
        
        print("\n=== Search Histories ===")
        for index, vocab in enumerate(self.history, 1):
            print(f"{index}.")
            self.display_vocab(vocab)


    def clear_history(self) -> None:
        if self.empty_history():
            return
        
        confirm = input("Are you sure to clear all favorites? (y/n): ").strip().lower()
        if confirm == "y":
            self.history.clear()
            save_history(self.history)
            print("All search histories cleared.")


    def search_vocabs(self) -> None:
        self.choose()



if __name__ == "__main__":
    vocabs = JapDictionary()
    vocabs.search_vocabs()