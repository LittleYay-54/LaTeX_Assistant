from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QPushButton, QWidget, QLineEdit,
                             QLabel, QGridLayout, QRadioButton, QApplication)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LaTeX Assistant")
        self.setGeometry(300, 300, 300, 150)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.widgets = []
        self.home()

    def clear_widgets(self):
        for widget in self.widgets:
            widget.deleteLater()
        self.widgets = []


    def home(self):
        self.clear_widgets()
        matrix_button = QPushButton("Matrix Tool")
        matrix_button.clicked.connect(self.enter_matrix_tool)
        self.layout.addWidget(matrix_button)
        self.widgets.append(matrix_button)

    def enter_matrix_tool(self):
        self.clear_widgets()
        home_button = QPushButton("Home")
        home_button.clicked.connect(self.home)
        self.layout.addWidget(home_button)
        self.widgets.append(home_button)

        row_label = QLabel("Rows?")
        self.layout.addWidget(row_label)
        self.widgets.append(row_label)
        row_text_field = QLineEdit()
        self.layout.addWidget(row_text_field)
        self.widgets.append(row_text_field)

        column_label = QLabel("Columns?")
        self.layout.addWidget(column_label)
        self.widgets.append(column_label)
        column_text_field = QLineEdit()
        self.layout.addWidget(column_text_field)
        self.widgets.append(column_text_field)

        create_matrix_button = QPushButton("Create Matrix")
        create_matrix_button.clicked.connect(lambda: self.create_matrix(row_text_field.text(), column_text_field.text()))
        self.layout.addWidget(create_matrix_button)
        self.widgets.append(create_matrix_button)

    def create_matrix(self, rows_str, columns_str):
        if not rows_str.isdigit() or not columns_str.isdigit():
            self.enter_matrix_tool()
            error_label = QLabel("Please enter only natural numbers")
            error_label.setStyleSheet("color: red")
            self.layout.addWidget(error_label)
            self.widgets.append(error_label)
            return
        self.clear_widgets()
        home_button = QPushButton("Home")
        home_button.clicked.connect(self.home)
        self.layout.addWidget(home_button)
        self.widgets.append(home_button)

        rows, columns = int(rows_str), int(columns_str)
        grid_layout = QGridLayout()
        fields = []
        for i in range(rows):
            row_fields = []
            for j in range(columns):
                field = QLineEdit()
                field.setFixedWidth(50)
                grid_layout.addWidget(field, i, j)
                row_fields.append(field)
                self.widgets.append(field)
            fields.append(row_fields)
        self.layout.addLayout(grid_layout)
        self.widgets.append(grid_layout)

        bmatrix_button = QRadioButton("bmatrix")
        self.layout.addWidget(bmatrix_button)
        self.widgets.append(bmatrix_button)
        pmatrix_button = QRadioButton("pmatrix")
        self.layout.addWidget(pmatrix_button)
        self.widgets.append(pmatrix_button)
        vmatrix_button = QRadioButton("vmatrix")
        self.layout.addWidget(vmatrix_button)
        self.widgets.append(vmatrix_button)

        clipboard_button = QPushButton("Copy to Clipboard")
        clipboard_button.clicked.connect(lambda: self.copy_to_clipboard([bmatrix_button.isChecked(), pmatrix_button.isChecked(), vmatrix_button.isChecked()],fields))
        self.layout.addWidget(clipboard_button)
        self.widgets.append(clipboard_button)

    def copy_to_clipboard(self, button_statuses, fields):
        matrix_type = ""
        if button_statuses[0]:
            matrix_type = "bmatrix"
        if button_statuses[1]:
            matrix_type = "pmatrix"
        if button_statuses[2]:
            matrix_type = "vmatrix"
        if matrix_type == "":
            # error message
            if isinstance(self.widgets[-1], QLabel):
                self.widgets[-1].setText("Please select one of the options")
                self.widgets[-1].setStyleSheet("color: red")
            else:
                status_label = QLabel("Please select one of the options")
                status_label.setStyleSheet("color: red")
                self.layout.addWidget(status_label)
                self.widgets.append(status_label)
            return
        latex_string = f"\\begin{{{matrix_type}}}\n"
        for row in fields:
            for entry in row:
                latex_string += entry.text() + " & "
            latex_string += "\\\\\n"
        latex_string += f"\\end{{{matrix_type}}}\n"

        clipboard = QApplication.clipboard()
        clipboard.setText(latex_string)
        # success message
        if isinstance(self.widgets[-1], QLabel):
            self.widgets[-1].setText("Copied to clipboard!")
            self.widgets[-1].setStyleSheet("color: green")
        else:
            status_label = QLabel("Copied to clipboard!")
            status_label.setStyleSheet("color: green")
            self.layout.addWidget(status_label)
            self.widgets.append(status_label)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
