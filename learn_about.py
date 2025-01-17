import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class letslearn(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Let's Learn")         # this makes and names the first window
        dimension = self.get_dimension()
        self.setGeometry(0,0, dimension.width(), dimension.height())        

        layout = QVBoxLayout()

        # Add title to ask users to pick a topic to learn about
        title_name = QLabel("What would you like to learn about?")
        title_name.setAlignment(Qt.AlignCenter)
        font_of_the_title = QFont("Arial", 30, QFont.Bold) # font and size
        title_name.setFont(font_of_the_title)
        layout.addWidget(title_name)
        
        
        button_layout = QHBoxLayout()

        sumutran_tigers_button = QPushButton("Sumatran Tigers") #made a button, the name that is in the speech marks
        sumutran_tigers_button.clicked.connect(self.show_sumatran_tiger_info)  #this connects the button to the function below which will have the information gethered 
        button_layout.addWidget(sumutran_tigers_button) # adds widget to button_layout

        javan_rhino_button = QPushButton("Javan Rhinoceros")
        javan_rhino_button.clicked.connect(self.show_javan_rhino_info)
        button_layout.addWidget(javan_rhino_button)

        komodo_button = QPushButton("Komodo")
        komodo_button.clicked.connect(self.show_komodo_info)
        button_layout.addWidget(komodo_button)

        online_safety_button = QPushButton("Online Safety")
        online_safety_button.clicked.connect(self.display_online_safety)
        button_layout.addWidget(online_safety_button)

        # This adds the button layout to the main layout
        layout.addLayout(button_layout)

        # Center align the button layout
        layout.setAlignment(button_layout, Qt.AlignCenter)

        self.setLayout(layout)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        layout.addWidget(self.text_edit)

    def get_dimension(self):
        screen_dimensions = QApplication.primaryScreen()
        return screen_dimensions.size()

    def show_sumatran_tiger_info(self):
        information = """What are Sumatran tigers?
                        Sumatran tigers are a subspecies of tigers, and they are only found in Sumatra, which is an island in Indonesia with a population of 500-600 tigers, the smallest among tigers in the world. They used to be found on islands all over Indonesia, but only the ones in Sumatra survive. You can tell a Sumatran tiger from a normal tiger as they have heavy black lines over their orange coats.

                        What is their habitat like?
                        The Sumatran Island is a very biodiverse island where many species cohabitate and survive. These include the Sumatran tiger, Rhinos, Orangutans, and Elephants, among other species that live together in the wild. Helping protect the Sumatran tigers and their habitat will also positively affect the other species living on the island.

                        What are the threats reducing their population?
                        One of the main threats is illegal wildlife trade. A survey made by Traffic shows that 80% of their deaths in the wild are caused by poachers killing them. Despite efforts to stop them, poachers continue until this day. Another problem that they are facing is the loss of habitat because of human expansion. For example, their habitat has been cleared for more agriculture like oil palm and other plantations. More settlements have also been made on Sumatra Island which has reduced their habitat. Illegal timber harvesting is also a big problem. All of these have meant that Sumatra Forest has reduced from around 50% to 26%.

                        What is/can be done to help?
                        Organizations like World Wildlife are trying to save and make sure the habitat space of Sumatran tigers is not being reduced too much. For example, they saved 100,000 acres of forest and are managing it, which was initially intended to be cut down and used for logging.
                        Information gathered from - worldwildlife.org, londonzoo.org"""

        # Set font size to 14
        font = QFont("Arial", 16)
        self.text_edit.setFont(font)
        self.text_edit.setPlainText(information)

    def show_javan_rhino_info(self):
        information = """What are Javan rhinos?
                        Javan rhinos used to live throughout India and Southeast Asia, but they have all been poached except for the ones in Java in the Ujung Kulon National Park. They are the most endangered of the rhino species, and their current population is under 100, about 70 rhinos. The rhinos are grey, and their single horn can be up to 10 in length.

                        What is their habitat like?
                        The Javan rhino can inhabit a couple of different types of habitats, including forests, marshy areas, and regions of thick bushes and bamboos.

                        What are the threats reducing their population?
                        One of the major threats to Javan rhinos has been and continues to this day is illegal wildlife trade. They were killed, and their horns were treated as trophies by trophy hunters. Their horn is a highly prized commodity in traditional Asian medicine. The coastal Ujung Kulon National Park is vulnerable to tsunamis and rising sea levels, which could have very bad consequences and even extinction. Disease is also a problem where 4 rhinos are thought to have died from various diseases in the last couple of years.

                        What is/can be done to help?
                        One thing that can be done to help that can reduce the chance of extinction is to make a second habitat for the Javan rhinos. World Wild Life and its partners are looking to do this and have identified a site. They are now waiting to conduct a study of the area to see if it is feasible. They also need the support of the local communities so that they can help set up a protected zone in the habitat and have a buffer zone that keeps off negative factors. An external threat is poachers; the people in the buffer zone will need to guard themselves against potential attacks. Another thing that can help is improving the quality of the current habitat so that it has the resources to hold more rhinos, as it is believed that the current habitat is holding the max number of rhinos that it can hold.

                        Information gathered from - worldwildlife.org"""

        # change the font and size of it 
        font = QFont("Arial", 16)
        self.text_edit.setFont(font)
        self.text_edit.setPlainText(information)

    def show_komodo_info(self): #information displayed after clicking a button
        information = """What is the Komodo?   
                        The Komodo dragon is known as the world's largest lizard species today, and they are suspected to have lived for millions of years. It is said that it can grow nearly 10 feet long and weighs an average of 150 pounds. The biggest ones are said to weigh up to 300 pounds. There is an estimated 4 to 5 thousand Komodo dragons out there living in the wild. They can be found on some Indonesian islands like Rintja, Padar, Flores, and Komodo island.

                        What is their habitat like?
                        Usually, Komodo dragon's main habitat is said to be tropical savanna forests. They, however, live in a range of habitats from the beach to ridge top. They can eat almost any type of meat and usually scavenge for carcasses and hunt many animals with their sharp, curved, and long teeth.

                        What are the threats reducing their population?
                        Rising sea levels are expected to submerge parts of the islands Komodo dragons live in during the next century, which will increase habitat loss. Overhunting of the prey that Komodo eat by humans like deer has made it harder for Komodo to increase their numbers and made survival harder. Humans might also kill them as they are dangerous to both them and cattle, so the higher the population on these islands, the more likely a conflict will occur.

                        What is/can be done?
                        So far, to ensure the survival of Komodo dragons, the Komodo National Park has been created. Here it is illegal to hunt them or damage their habitat. In places where the Komodo lives, there are also patrols to watch out so that hunters do not enter and hunt them and sell them. Another thing that can be done is limit the expansion of agriculture and settlements on these islands so that the living space of Komodo does not decrease and they can sustain a higher population.

                        Information gathered - worldwildlife.org, nationalzoo.si.edu, homework.study.com"""

        # Set font size to 18
        font = QFont("Arial", 16)
        self.text_edit.setFont(font)
        self.text_edit.setPlainText(information)
    
    def display_online_safety(self): 
        information = """online safety is a very important issue for all people using the internet. You are connected to so many people around the world and you don't know which ones will have ill intentions towards you. On the surface they might appear a certain way but in reality, be a completely different person. With more and more people being online and also spending an increasing amount of time online, safety is a big issue.
                        Child safety is on the internet is especially important as they might more easily get manipulated as might not be aware of the dangers out there if they have not been talked to about what to look out for and what not to do.
                        To ensure safety online, you first need to know what to look out for. Here are some threats you could face online
                        . One of the main things to do to keep safe is to not reveal too much personal information about yourself. For example, don't reveal where you live or your real name so it could be used to find out your real identity. People online could also potentially pose as real institutions to try and make you reveal personal information which is called phishing.
                        . Cyberbullying is also a major concern as it could be very harmful to children who are experiencing bullying for the very first time or even adults if they are going through a tough period of their life. To stop this, you could report this to your school to get help or let your parent know. If you are a parent, you have to keep check of what your kid is doing online as a lot of people have access to the internet which could be used to form their viewpoints and how they think from an early time in their life. 
                        . Identity theft is another malicious thing that could occur online. If enough information about you is available for everyone to see, like a lot of pictures along with your name and other details, other people could potentially pretend it is you. For example, they could pose as you to get a loan from the bank or make purchases with credit cards which could financially ruin somebody. One way you could mitigate the risk of this happening, is by having strong passwords which are unique on each site so that if they break one password, they can't break into them all. Even if the password is strong, it is still advised to have multiple as they might be able to pose as you and call up the companies to change the password.
                        . Finally, there is the most common threat which is malicious malware which could end up on your computer in various ways. One of these ways, is by clicking on links which will install these on your computer. They could do multiple things, form installing spy malware which can spy on what you're doing with your camera to potentially gaining access to our files. After, they might ask for ransom if you want them back or they'll delete them. 

                        Overall, there are many dangerous, but these can be reduced in various ways. These are having a strong unique password, setting parental controls so children can't access dangerous or graphic sites or having a strong anti-virus. Keeping anonymity can also be very helpful as well as only talking to people you trust like family and friends.
                        """

        font = QFont("Arial", 16)
        self.text_edit.setFont(font)
        self.text_edit.setPlainText(information)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    letslearn = letslearn()
    letslearn.show()
    sys.exit(app.exec_())