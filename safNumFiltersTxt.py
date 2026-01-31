import re
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, \
    QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Safaricom Phone Number Search")
        self.setGeometry(100, 100, 500, 300)

        # Set a fixed window size
        self.setFixedSize(500, 300)

        # Create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Set the background color to light gray
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(211, 211, 211))  # Light gray background
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))  # Black text
        self.setPalette(palette)

        # Add a label and text box for file selection
        file_label = QLabel("Select a .txt file to search:")
        self.file_entry = QLineEdit()
        file_button = QPushButton("Browse")
        file_button.clicked.connect(self.select_file)

        # Style the buttons to be green
        file_button.setStyleSheet("background-color: green; color: white;")

        # Add a button to start the search
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_numbers)
        search_button.setStyleSheet("background-color: green; color: white;")

        # Add a label to display the search results
        self.result_label = QLabel()
        self.result_label.setWordWrap(True)  # Allow wrapping of text

        # Add a button to export the matches to a new file
        self.export_button = QPushButton("Export")
        self.export_button.setEnabled(False)
        self.export_button.clicked.connect(self.export_matches)
        self.export_button.setStyleSheet("background-color: green; color: white;")

        # Add some spacing between widgets for better aesthetics
        layout.addSpacing(20)
        layout.addWidget(file_label)
        layout.addWidget(self.file_entry)
        layout.addWidget(file_button)
        layout.addSpacing(10)
        layout.addWidget(search_button)
        layout.addSpacing(10)
        layout.addWidget(self.export_button)
        layout.addSpacing(20)
        layout.addWidget(self.result_label)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

        # Add a status bar
        self.statusBar().showMessage("Program developed by Mufasa Tech")

    def select_file(self):
        # Open a file dialog to select the file
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a .txt file to search", "", "Text files (*.txt)")
        if file_path:
            self.file_entry.setText(file_path)

    def search_numbers(self):
        # Get the file path from the text box
        file_path = self.file_entry.text()

        # Open the text file
        try:
            with open(file_path, 'r') as f:
                file_contents = f.read()
                print(f"Original File contents:\n{file_contents}")  # Debug print
        except FileNotFoundError:
            QMessageBox.warning(self, "File not found", "The selected file could not be found.")
            return

        # Remove all whitespaces (spaces, tabs, newlines)
        file_contents_no_whitespace = re.sub(r'\s+', '', file_contents)
        print(f"File contents without whitespaces:\n{file_contents_no_whitespace}")  # Debug print

        # Define the regular expression pattern for Safaricom phone numbers
        pattern = r'(\+?2547([0-2]|9)\d{7})'

        # Use the re.findall() method to extract all matches from the file contents
        matches = re.findall(pattern, file_contents_no_whitespace)

        # Remove duplicates by converting to a set and format the matches
        matches = set(match[0] for match in matches)  # Extract the full match from the tuples returned

        # Format the matches with commas
        if matches:
            formatted_matches = ", ".join(sorted(matches))  # Sort the matches for better readability
        else:
            formatted_matches = ""

        # Display the matches in the result label
        if formatted_matches:
            self.result_label.setText("Matched Safaricom phone numbers:\n" + formatted_matches)
            QMessageBox.information(self, "Matches Found", formatted_matches)
        else:
            self.result_label.setText("No Safaricom phone numbers found.")
            QMessageBox.information(self, "No Matches", "No Safaricom phone numbers found in the file.")

        # Enable the export button if there are matches
        if matches:
            self.export_button.setEnabled(True)
        else:
            self.export_button.setEnabled(False)

    def export_matches(self):
        # Get the file path to export to
        export_path, _ = QFileDialog.getSaveFileName(self, "Export matches to a new file", "", "Text files (*.txt)")
        if not export_path:
            return

        # Get the matches to export from the result label
        matches = self.result_label.text().split("\n")[1]  # Get the second line which contains the matches

        # Write the matches to the new file
        with open(export_path, 'w') as f:
            f.write(matches)

        # Show a message box confirming the export
        QMessageBox.information(self, "Export successful",
                                f"{len(matches.split(','))} matches were exported to {export_path}.")


# Application runner
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
