import requests
import customtkinter as ctk
import webbrowser




class News:
    def __init__(self, api_key, root):
        self.api_key = api_key
        self.root = root
        self.root.grid_columnconfigure(0, weight=1)
    

    def get_news(self):
        query = {"api_key":self.api_key, "q": "medicine AND health", "language": "en" }
        
        
        url = f"https://newsdata.io/api/1/news?apikey={query['api_key']}&q='{query['q']}'&language={query['language']}&size=5"
        response = requests.get(url)

        return response.json()
    
    def news_menu(self):
        news_json = self.get_news()
        
        self.root.geometry("500x600")
        
        self.root.title_label = ctk.CTkLabel(self.root, text="Noticias", font=("Arial", 16, "bold"))
        self.root.title_label.pack(pady=15, padx=10)
        
        for i, article in enumerate(news_json["results"]):
            self.root.title_label = ctk.CTkLabel(self.root, text=article["title"], font=("Arial", 12, "bold"), wraplength=500)
            self.root.title_label.pack(pady=10, padx=10)
            
            self.root.description_button = ctk.CTkButton(self.root, text="Description", command=lambda article=article: self.view_article(article))
            self.root.description_button.pack(pady=10, padx=10)
            
        
        
        
            
    def view_article(self, article):
        new_window = ctk.CTk()
        
        new_window.title_label = ctk.CTkLabel(new_window, text=article["title"], font=("Arial", 12, "bold"))
        new_window.title_label.pack(pady=10, padx=10)
        
        new_window.description_label = ctk.CTkLabel(new_window, text=article["description"], wraplength=500)
        new_window.description_label.pack(pady=10, padx=10)
        
        new_window.link_label = ctk.CTkLabel(new_window, text=f"Más información en: {article['link']}", wraplength=500, text_color="blue")
        new_window.link_label.bind("<Button-1>", lambda e: self.open_link(article["link"]))
        new_window.link_label.pack(pady=10, padx=10)
        
        new_window.back_button = ctk.CTkButton(new_window, text="Back", command=new_window.destroy)
        new_window.back_button.pack(pady=10, padx=10)
        
        
        new_window.mainloop()
        
    def open_link(self, link):
        webbrowser.open(link)
        
    
    
def main():
    root = ctk.CTk()
    news = News("pub_32493947bac2cd99a74d4b4821243a7ac98aa", root)
    news.news_menu()
    root.mainloop()    
    
if __name__ == "__main__":
    main()
        
    

    
    





