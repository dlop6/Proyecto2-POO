import requests
import customtkinter as ctk
import webbrowser




import requests
import webbrowser


class News:
    """
    Clase que representa una fuente de noticias. Permite obtener noticias relacionadas con medicina y salud en inglés
    desde la API de newsdata.io y mostrarlas en una interfaz gráfica de usuario.
    """
    def __init__(self, api_key, root):
        """
        Constructor de la clase News.

        :param api_key: Clave de la API de newsdata.io
        :type api_key: str
        :param root: Ventana principal de la aplicación
        :type root: ctk.CTk
        """
        self.api_key = api_key
        self.root = root
        self.root.grid_columnconfigure(0, weight=1)
    

    def get_news(self):
        """
        Obtiene las noticias de la API de newsdata.io.

        :return: Diccionario con las noticias obtenidas de la API
        :rtype: dict
        """
        query = {"api_key":self.api_key, "q": "medicine AND health", "language": "en" }
        
        
        url = f"https://newsdata.io/api/1/news?apikey={query['api_key']}&q='{query['q']}'&language={query['language']}&size=5"
        response = requests.get(url)

        return response.json()
    
    def news_menu(self):
        """
        Muestra las noticias obtenidas de la API en una interfaz gráfica de usuario.
        """
        news_json = self.get_news()
        
        self.root.geometry("500x600")
        
        self.root.title_label = ctk.CTkLabel(self.root, text="Noticias", font=("Arial", 16, "bold"))
        self.root.title_label.pack(pady=15, padx=10)
        
        for i, article in enumerate(news_json["results"]):
            self.root.title_label = ctk.CTkLabel(self.root, text=article["title"], font=("Arial", 12, "bold"), wraplength=500)
            self.root.title_label.pack(pady=10, padx=10)
            
            self.root.description_button = ctk.CTkButton(self.root, text="Descripción", command=lambda article=article: self.view_article(article))
            self.root.description_button.pack(pady=10, padx=10)
            
    def view_article(self, article):
        """
        Muestra la descripción de una noticia en una ventana emergente.

        :param article: Diccionario con la información de la noticia
        :type article: dict
        """
        new_window = ctk.CTk()
        
        new_window.title_label = ctk.CTkLabel(new_window, text=article["title"], font=("Arial", 12, "bold"))
        new_window.title_label.pack(pady=10, padx=10)
        
        new_window.description_label = ctk.CTkLabel(new_window, text=article["description"], wraplength=500)
        new_window.description_label.pack(pady=10, padx=10)
        
        new_window.link_label = ctk.CTkLabel(new_window, text=f"Más información en: {article['link']}", wraplength=500, text_color="blue")
        new_window.link_label.bind("<Button-1>", lambda e: self.open_link(article["link"]))
        new_window.link_label.pack(pady=10, padx=10)
        
        new_window.back_button = ctk.CTkButton(new_window, text="Atrás", command=new_window.destroy)
        new_window.back_button.pack(pady=10, padx=10)
        
        
        new_window.mainloop()
        
    def open_link(self, link):
        """
        Abre el enlace de una noticia en el navegador web predeterminado.

        :param link: Enlace de la noticia
        :type link: str
        """
        webbrowser.open(link)
        
    
    
def main():
    root = ctk.CTk()
    news = News("pub_32493947bac2cd99a74d4b4821243a7ac98aa", root)
    news.news_menu()
    root.mainloop()    
    
if __name__ == "__main__":
    main()
        
    

    
    





