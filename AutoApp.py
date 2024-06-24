import sys
import webbrowser
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QTabWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auto Apps")

        # Устанавливаем размер окна
        self.resize(400, 200)

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
        self.programming_buttons = {
            "PyCharm 2024.1.3": "https://download.jetbrains.com/python/pycharm-community-2024.1.3.exe?_gl=1*1d9ckfr*_gcl_au*NDkyNzAyNjE3LjE3MTg5ODczNzc.*_ga*MTk5NDE5NDg0Ni4xNzE4OTg3MzUx*_ga_9J976DJZ68*MTcxOTE3OTgzNC4yLjEuMTcxOTE3OTg2OC4yNi4wLjA.&_ga=2.3583728.1762200236.1719179835-1994194846.1718987351",
            "WebStorm 2024.1.5": "https://download.jetbrains.com/webstorm/WebStorm-2024.1.5.exe?_gl=1*uafgyl*_gcl_au*NDkyNzAyNjE3LjE3MTg5ODczNzc.*_ga*MTk5NDE5NDg0Ni4xNzE4OTg3MzUx*_ga_9J976DJZ68*MTcxOTE3OTgzNC4yLjEuMTcxOTE3OTг2OC4yNi4wLjA.&_ga=2.209184594.1762200236.1719179835-1994194846.1718987351",
            "VS Code 1.90": "https://code.visualstudio.com/Download",
            "Git 2.45.2": "https://github.com/git-for-windows/git/releases/download/v2.45.2.windows.1/Git-2.45.2-64-bit.exe"
        }

        self.games_buttons = {
            "Discord": "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64",
            "Steam": "https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe",
            "Epic Games": "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi",
            "Rage MP": "https://rage.mp/ru#"
        }

        self.other_buttons = {
            "Spotify": "https://download.scdn.co/SpotifySetup.exe",
            "BoosterX": "https://download.boosterx.org/BoosterX.exe",
            "Google": 'https://www.google.com/intl/ru/chrome/next-steps.html?statcb=1&installdataindex=empty&defaultbrowser=0',
            "Opera GX": 'https://www.opera.com/ru/computer/thanks?ni=eapgx&os=windows'
        }

        self.drivers_buttons = {
            "NVIDIA": "https://www.nvidia.com/Download/index.aspx",
            "AMD": "https://www.amd.com/en/support"
        }

        # Создаем кнопки для вкладки "Программирование"
        self.create_buttons(self.programming_tab, self.programming_buttons)
        # Создаем кнопки для вкладки "Игры"
        self.create_buttons(self.games_tab, self.games_buttons)
        # Создаем кнопки для вкладки "Другое"
        self.create_buttons(self.other_tab, self.other_buttons)
        # Создаем кнопки для вкладки "Драйвера"
        self.create_buttons(self.drivers_tab, self.drivers_buttons)

    def create_buttons(self, tab, buttons):
        layout = QVBoxLayout()
        for name, url in buttons.items():
            button = QPushButton(name)
            button.clicked.connect(lambda checked, url=url: self.open_url(url))
            layout.addWidget(button)
        tab.setLayout(layout)

    def open_url(self, url):
        webbrowser.open(url)
        QMessageBox.information(self, "Информация", f"Начинаем загрузку: {url.split('/')[-1]}")

    def button_clicked(self):
        button = self.sender()
        button_name = button.text()
        url = self.button_actions.get(button_name)

        if url:
            webbrowser.open(url)
            QMessageBox.information(self, "Информация", f"Начинаем загрузку: {button_name}")
        else:
            QMessageBox.warning(self, "Ошибка", f"Не найдена ссылка для: {button_name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
