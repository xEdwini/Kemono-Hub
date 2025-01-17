import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

# Your questions_data list
questions_data = [
    # Sumatran Tigers
    Question("What island is the Sumatran tiger found on?", ["a) Java", "b) Bali", "c) Sumatra", "d) Sulawesi"], "c"),
    Question("How can you tell a Sumatran tiger apart from other tigers?", ["a) It's larger", "b) It's white", "c) Heavy black stripes", "d) It has no stripes"], "c"),
    # Javan Rhinoceros
    Question("Where do the last Javan rhinos live?", ["a) Bali", "b) Java", "c) Sumatra", "d) Borneo"], "b"),
    Question("What is the color of Javan rhinos?", ["a) White", "b) Black", "c) Gray", "d) Pink"], "c"),
    # Komodo Dragons
    Question("What is the Komodo dragon's habitat?", ["a) Tropical forests", "b) Savanna", "c) Beaches", "d) All of the above"], "d"),
    Question("How many Komodo dragons are estimated to be in the wild?", ["a) 100-200", "b) 300-400", "c) 4000-5000", "d) More than 6000"], "c"),
    # General Conservation
    Question("What is the primary cause of habitat loss for these species?", ["a) Deforestation", "b) Pollution", "c) Climate change", "d) Overfishing"], "a"),
    Question("What organization is helping to protect Sumatran tigers?", ["a) WWF", "b) Greenpeace", "c) Oceana", "d) Sierra Club"], "a"),
    # Specific Actions
    Question("What conservation action is being taken for the Sumatran tiger?", ["a) Anti-poaching patrols", "b) Captive breeding", "c) Habitat restoration", "d) All of the above"], "d"),
    Question("What is a proposed solution to help the Javan rhino?", ["a) Building more parks", "b) Creating a second habitat", "c) Relocation to zoos", "d) Strict hunting laws"], "b"),
    # Threats
    Question("What is a significant threat to the Sumatran tiger?", ["a) Illegal wildlife trade", "b) Natural predators", "c) Disease", "d) All of the above"], "a"),
    Question("Which species is affected by rising sea levels?", ["a) Sumatran tiger", "b) Javan rhino", "c) Komodo dragon", "d) Bali myna"], "c"),
    # Identification
    Question("Which species is known for heavy black stripes on its coat?", ["a) Javan rhino", "b) Sumatran tiger", "c) Komodo dragon", "d) Bali myna"], "b"),
    Question("Which animal is the world's largest lizard?", ["a) Crocodile", "b) Iguana", "c) Monitor lizard", "d) Komodo dragon"], "d"),
    # Additional Questions
    Question("What animal is only found on the island of Sumatra?", ["a) Orangutan", "b) Sumatran tiger", "c) Javan rhino", "d) Komodo dragon"], "b"),
    Question("What feature distinguishes the Javan rhino?", ["a) Two horns", "b) Armored skin", "c) Single horn", "d) Large size"], "c"),
    Question("What diet is common among Komodo dragons?", ["a) Herbivorous", "b) Carnivorous", "c) Omnivorous", "d) Insectivorous"], "b"),
    Question("What factor contributes to the declining numbers of Sumatran tigers?", ["a) Habitat loss", "b) Lack of prey", "c) Disease", "d) All of the above"], "d"),
    Question("Which organization has protected 100,000 acres of forest for Sumatran tigers?", ["a) World Wildlife Fund", "b) National Geographic", "c) Conservation International", "d) The Nature Conservancy"], "a"),
    Question("What does the Ujung Kulon National Park primarily protect?", ["a) Sumatran tigers", "b) Bali mynas", "c) Javan eagles"], "d")
]

class QuizWindow(QWidget):
    def __init__(self, questions):
        super().__init__()
        dimension = self.get_dimension()
        self.setGeometry(0,0, dimension.width(), dimension.height())
        self.questions = questions
        random.shuffle(self.questions)
        self.score = 0
        self.current_question_index = 0
        self.initUI()
        self.display_question()

    def get_dimension(self):
        screen_dimensions = QApplication.primaryScreen()
        return screen_dimensions.size()

    def initUI(self):
        self.setWindowTitle('Conservation Quiz')
        self.layout = QVBoxLayout()
        
        self.question_label = QLabel(self)
        self.layout.addWidget(self.question_label)
        
        self.option_buttons = []
        for _ in range(4):
            button = QPushButton(self)
            button.clicked.connect(self.check_answer)
            self.layout.addWidget(button)
            self.option_buttons.append(button)

        self.setLayout(self.layout)
        #self.setGeometry(300, 300, 400, 200)

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.setText(question.prompt)
            for i, option in enumerate(question.options):
                self.option_buttons[i].setText(option)
        else:
            QMessageBox.information(self, 'Quiz Completed', f'Your final score is {self.score}/{len(self.questions)}')
            #self.close()

    def check_answer(self):
        sender = self.sender()
        selected_answer = sender.text()[0].lower()
        correct_answer = self.questions[self.current_question_index].answer
        if selected_answer == correct_answer:
            self.score += 1
        self.current_question_index += 1
        self.display_question()

'''def run_quiz():
    app = QApplication(sys.argv)
    quiz_window = QuizWindow(questions_data)
    quiz_window.showMaximized()
    sys.exit(app.exec_())'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    quiz_window = QuizWindow(questions_data)
    quiz_window.showMaximized()
    sys.exit(app.exec_())
