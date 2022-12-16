# module for manipulating Bb pools

import xml.etree.ElementTree as ET
import copy
import sys
import zipfile as zipfile

class setup_pool:
    def __init__(self, num_quest=10):
        self.num_quest = num_quest
        self.my_script = '<p><script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"></script></p>'
        self.tree = ET.ElementTree(file='../template/res00001.dat')
        root = self.tree.getroot()
        for item in root.findall(".//*[item]"):
            section = item
    
        # make a copy of original question(s)
        self.template = []
        for elem in self.tree.iter(tag='item'):
            self.template.append(copy.deepcopy(elem))
            section.remove(elem) # delete template
        self.section = section

    def create_question(self):
        return copy.deepcopy(self.template)

    def set_question_text(self, question, text):
        question[0][1][0][0][0][0][0][0].text = text + self.my_script

    def set_question_answer(self, question, answer):
        question[0][2][1][0][2].text = str('{:f}'.format(answer))

    def set_question_accuracy(self, question, answer, error):
        question[0][2][1][0][0].text = str('{:f}'.format(answer-error))
        question[0][2][1][0][1].text = str('{:f}'.format(answer+error))

    def set_question(self, question):
        self.section.append(question[0])

    def package_pool(self):
        """
        need to rename pool list to res00001.dat and zip with all other files in ../template
        """
        print("Packaging not sorted yet")
