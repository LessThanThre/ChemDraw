# main.py

from view.app_view import AppView
from viewmodel.app_viewmodel import AppViewModel

def main():
    # Инициализируем AppView без связывания ViewModel
    app_view = AppView()
    
    # Создаем экземпляр AppViewModel и связываем его с canvas_view
    app_view_model = AppViewModel(app_view.canvas_view)
    app_view.canvas_view.set_view_model(app_view_model)  # Устанавливаем ViewModel

    # Теперь можно вызвать bind_events, так как view_model уже задан
    app_view.canvas_view.bind_events()
    
    app_view.run()

if __name__ == "__main__":
    main()
