
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QCheckBox, QPushButton, QMessageBox, QGridLayout, QWidget


class Avtoriz2(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" Социальный опрос")
        self.answers = []
    
        self.top = QLabel("Выбирите возраст")
        self.label = QCheckBox("8-12")
        self.label_1 = QCheckBox("13-16")
        self.label_2 = QCheckBox("17-21")
        self.label_3 = QCheckBox("22-27")
        self.label_4 = QCheckBox("28-34")
        self.label_5 = QCheckBox("35-44")
        self.label_6 = QCheckBox("45-50")
        
        self.top_2 = QLabel("Выбирите пол")
        self.label_7= QCheckBox("Мужской")
        self.label_8 = QCheckBox("Женский")
        self.label_9 = QCheckBox("Другое")

        self.submit_button = QPushButton("Отправить")
        self.submit_button.clicked.connect(self.submit_survey)

        layout = QVBoxLayout()
        layout.addWidget (self.top)
        layout.addWidget (self.label)
        layout.addWidget (self.label_1)
        layout.addWidget (self.label_2)
        layout.addWidget (self.label_3)
        layout.addWidget (self.label_4)
        layout.addWidget (self.label_5)
        layout.addWidget (self.label_6)
        layout.addWidget (self.top_2)
        layout.addWidget (self.label_7)
        layout.addWidget (self.label_8)
        layout.addWidget (self.label_9)
        layout.addWidget(self.submit_button)
        
        self.setLayout(layout)
        
    def submit_survey(self):
        age = []
        if self.label.isChecked():
            age.append("8-12")
        if self.label_1 .isChecked():
            age.append("13-16")
        if self.label_2.isChecked():
            age.append("17-21")
        if self.label_3.isChecked():
            age.append("22-27")
        if self.label_4.isChecked():
            age.append("28-34")
        if self.label_5.isChecked():
            age.append("35-44")
        if self.label_6.isChecked():
            age.append("45-50")
            
        gender = []
        if self.label_7.isChecked():
            gender.append("Мужской")
        if self.label_8.isChecked():
            gender.append("Женский")
        if self.label_9.isChecked():
            gender.append("Другой")

        if not age:
            age = "Не выбрано"
        if not gender:
            gender = "Не выбрано"

        QMessageBox.information(self, "Результаты опроса", f"Ваш возраст: {', '.join(age)}\nВаш пол: {', '.join(gender)}")


        