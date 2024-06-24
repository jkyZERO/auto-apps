import sys
import webbrowser
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QTabWidget
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auto Apps")

        # Устанавливаем размер окна
        self.resize(400,20)

        # Создаем главный виджет и табуляцию
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.tabs = QTabWidget()

        # Создаем вкладки
        self.programming_tab = QWidget()
        self.games_tab = QWidget()
        self.other_tab = QWidget()
        self.drivers_tab = QWidget()

        self.tabs.addTab(self.programming_tab, "Программирование")
        self.tabs.addTab(self.games_tab, "Игры")
        self.tabs.addTab(self.other_tab, "Другое")
        self.tabs.addTab(self.drivers_tab, "Драйвера")

        # Создаем лэйаут для главного виджета
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        main_widget.setLayout(main_layout)

        # Определяем кнопки для каждой вкладки
        self.programming_buttons = self.load_buttons('programming')
        self.games_buttons = self.load_buttons('games')
        self.other_buttons = self.load_buttons('other')
        self.drivers_buttons = self.load_buttons('drivers')

        # Создаем кнопки для вкладки "Программирование"
        self.create_buttons(self.programming_tab, self.programming_buttons)
        # Создаем кнопки для вкладки "Игры"
        self.create_buttons(self.games_tab, self.games_buttons)
        # Создаем кнопки для вкладки "Другое"
        self.create_buttons(self.other_tab, self.other_buttons)
        # Создаем кнопки для вкладки "Драйвера"
        self.create_buttons(self.drivers_tab, self.drivers_buttons)

    def load_buttons(self, category):
        try:
            with open('config.json', 'r') as file:
                data = json.load(file)
                return data.get(category, {})
        except FileNotFoundError:
            QMessageBox.critical(self, "Ошибка", "Не найден файл конфигурации 'config.json'.")
            return {}

    def create_buttons(self, tab, buttons):
        layout = QVBoxLayout()
        for name, url in buttons.items():
            button = QPushButton(name)
            button.clicked.connect(lambda checked, name=name, url=url: self.open_url(name, url))
            layout.addWidget(button)
        tab.setLayout(layout)

    def open_url(self, name, url):
        webbrowser.open(url)
        QMessageBox.information(self, "Информация", f"Начинаем загрузку: {name}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
