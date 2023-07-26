# recipe_index.py
# Jordan Maloney
# 2/07/23
# Ver. 0.1.1

# Imports
from dataclasses import dataclass
from PySide6.QtWidgets import *
from PySide6 import QtCore

# Classes
@dataclass
class recipe:
    _name: str
    _course: int
    _allergens: list
    _meats: list
    _instructions: str
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name: str):
        if new_name != "":
            self._name = new_name.title()
        else:
            raise ValueError("Please give the recipe a name.")
    
    
    @property
    def course(self) -> int:
        return self._course
    
    @course.setter
    def course(self, new_course: int):
        if new_course >= 0 and new_course <= 3:
            self._course = new_course
        else:
            raise ValueError("Please enter an integer value from 1 to 4.")
    
    
    @property
    def allergens(self) -> list:
        return self._allergens
    
    @allergens.setter
    def allergens(self, new_allergens: list):
        self._allergens = new_allergens

    
    @property
    def meats(self) -> list:
        return self._meats
    
    @meats.setter
    def meats(self, new_meats: list):
        self._meats = new_meats

    
    @property
    def instructions(self) -> str:
        return self._instructions
    
    @instructions.setter
    def instructions(self, new_instructions: str):
        self._instructions = new_instructions
    

# Widgets
app = QApplication()
main = QMainWindow()
central_widget = QWidget()
horizontal_divider = QHBoxLayout()
divider_widget1 = QWidget()
recipe_box = QVBoxLayout()
recipe_widget1 = QWidget()
recipe_info = QHBoxLayout()
recipe_name = QLabel("Recipe")
recipe_course = QLabel("Course")
recipe_vegan = QLabel("Vegan?")
divider_widget2 = QWidget()
subdivider_divwidget2 = QVBoxLayout()
categories_label = QLabel("Search Filters")
categories_widget = QWidget()
categories_box = QHBoxLayout()
# Course
course_widget = QWidget()
course_vbox = QVBoxLayout()
course_checkbox = QButtonGroup()
course_filter_label = QLabel ("Course")
breakfast_checkbox = QCheckBox("Breakfast")
lunch_checkbox = QCheckBox("Lunch")
dinner_checkbox = QCheckBox("Dinner")
dessert_checkbox = QCheckBox("Dessert")
# Allergens
allergens_widget = QWidget()
allergens_vbox = QVBoxLayout()
allergens_filter_label = QLabel ("Allergens\n(Tick to exclude)")
dairy_checkbox = QCheckBox("Dairy")
nuts_checkbox = QCheckBox("Nuts")
peanuts_checkbox = QCheckBox("Peanuts")
wheat_checkbox = QCheckBox("Wheat")
shellfish_checkbox = QCheckBox("Shellfish")
seafood_checkbox = QCheckBox("Seafood")
egg_checkbox = QCheckBox("Eggs")
soy_checkbox = QCheckBox("Soy")
sesame_checkbox = QCheckBox("Sesame")
uncheck_allergens = QPushButton("Uncheck All")
# Meats
meats_widget = QWidget()
meats_vbox = QVBoxLayout()
meats_filter_label = QLabel("Meat content\n(Tick to exclude)")
beef_checkbox = QCheckBox("Beef")
pork_checkbox = QCheckBox("Pork")
lamb_checkbox = QCheckBox("Lamb")
poultry_checkbox = QCheckBox("Poultry")
uncheck_meats = QPushButton("Uncheck All")
# Add/Edit/Remove Buttons
aer_widget = QWidget()
aer_box = QHBoxLayout()
add_button = QPushButton("Add Recipe")
edit_button = QPushButton("Edit Recipe")
remove_button = QPushButton("Remove Recipe")


# Putting Widgets together
main.setWindowTitle("Recipe Index")
main.setCentralWidget(central_widget)
central_widget.setLayout(horizontal_divider)

# Part that displays recipes
horizontal_divider.addWidget(divider_widget1)
divider_widget1.setLayout(recipe_box)
recipe_box.addWidget(recipe_widget1)
recipe_widget1.setLayout(recipe_info)
recipe_info.addWidget(recipe_name)
recipe_info.addWidget(recipe_course)
recipe_info.addWidget(recipe_vegan)

# Search Filters part
horizontal_divider.addWidget(divider_widget2)
divider_widget2.setLayout(subdivider_divwidget2)
subdivider_divwidget2.addWidget(categories_label)
subdivider_divwidget2.addWidget(categories_widget)
subdivider_divwidget2.addStretch()
categories_widget.setLayout(categories_box)
categories_box.addWidget(course_widget)
course_widget.setLayout(course_vbox)
course_checkbox.addButton(breakfast_checkbox)
course_checkbox.addButton(lunch_checkbox)
course_checkbox.addButton(dinner_checkbox)
course_checkbox.addButton(dessert_checkbox)
course_vbox.addWidget(course_filter_label)
course_vbox.addWidget(breakfast_checkbox)
course_vbox.addWidget(lunch_checkbox)
course_vbox.addWidget(dinner_checkbox)
course_vbox.addWidget(dessert_checkbox)
course_vbox.addStretch()
categories_box.addWidget(allergens_widget)
allergens_widget.setLayout(allergens_vbox)
allergens_vbox.addWidget(allergens_filter_label)
allergens_vbox.addWidget(dairy_checkbox)
allergens_vbox.addWidget(nuts_checkbox)
allergens_vbox.addWidget(peanuts_checkbox)
allergens_vbox.addWidget(wheat_checkbox)
allergens_vbox.addWidget(shellfish_checkbox)
allergens_vbox.addWidget(seafood_checkbox)
allergens_vbox.addWidget(egg_checkbox)
allergens_vbox.addWidget(soy_checkbox)
allergens_vbox.addWidget(sesame_checkbox)
allergens_vbox.addWidget(uncheck_allergens)
allergens_vbox.addStretch()
categories_box.addWidget(meats_widget)
meats_widget.setLayout(meats_vbox)
meats_vbox.addWidget(meats_filter_label)
meats_vbox.addWidget(beef_checkbox)
meats_vbox.addWidget(pork_checkbox)
meats_vbox.addWidget(lamb_checkbox)
meats_vbox.addWidget(poultry_checkbox)
meats_vbox.addWidget(uncheck_meats)
meats_vbox.addStretch()

# Add/Edit/Remove Buttons part
subdivider_divwidget2.addWidget(aer_widget)
aer_widget.setLayout(aer_box)
aer_box.addWidget(add_button)
aer_box.addWidget(edit_button)
aer_box.addWidget(remove_button)





# Code for making buttons with multiple Labels (Reference when making the list of recipes that can be clicked on)
def recipe_box_updater():
    for item in recipe_list:
        button = QPushButton()
        courses = ["Breakfast", "Lunch", "Dinner", "Dessert"]
        button_divider = QHBoxLayout()
        name_label = QLabel(item._name)
        button_divider.addWidget(name_label)
        course_label = QLabel(courses[item._course])
        button_divider.addWidget(course_label)
        if len(item._meats) == 0:
            content_label = QLabel("Yes")
        else:
            content_label = QLabel("No")
        button_divider.addWidget(content_label)
        button.setFixedHeight(40)
        button.setLayout(button_divider)
        recipe_box.addWidget(button)
        this_dict = {
            "name" : item._name,
            "button" : button}
        button_list.append(this_dict)
    recipe_box.addStretch()


def showhide():
    for a in button_list:
        in_list = False
        for b in active_recipe_list:
            if a["name"] == b._name:
                in_list = True
        if in_list == False:
            a["button"].hide()
        else:
            a["button"].show()

# .clicked functions
def course_checked(this_checkbox, course):
    if this_checkbox.isChecked() is True:
        for item in active_course:
            active_course.remove(item)
        active_course.append(course)

    recipe_filter()

def allergen_checked(this_checkbox, allergen):
    # Update list of filtered allergens
    if this_checkbox.isChecked() is True:
        active_allergens.append(allergen)
    elif this_checkbox.isChecked() is False:
        active_allergens.remove(allergen)

    recipe_filter()

def meat_checked(this_checkbox, meat):
    if this_checkbox.isChecked() is True:
        active_meats.append(meat)
    elif this_checkbox.isChecked() is False:
        active_meats.remove(meat)

    recipe_filter()

def recipe_filter():
    if len(active_course) == 1:
        template = recipe("Template", active_course[0], active_allergens, active_meats, "")
        for item in active_recipe_list[:]:
            active = True # Item is active
            if item._course != template._course:
                active = False
            for item_2 in item._allergens:
                for item_3 in template._allergens:
                    if item_2 == item_3:
                        active = False
            for item_2 in item._meats:
                for item_3 in template._meats:
                    if item_2 == item_3:
                        active = False
            if active is False:
                active_recipe_list.remove(item)
        for item in recipe_list[:]:
            active = False
            for item_2 in active_recipe_list[:]:
                if item == item_2:
                    active = True
            if active is False:
                course_clear = True
                allergen_clear = True
                meat_clear = True
                if item._course != template._course:
                    course_clear = False
                for item_2 in item._allergens:
                    for item_3 in template._allergens:
                        if item_2 == item_3:
                            allergen_clear = False
                for item_2 in item._meats:
                    for item_3 in template._meats:
                        if item_2 == item_3:
                            meat_clear = False
                if course_clear is True and allergen_clear is True and meat_clear is True:
                    active_recipe_list.append(item)

    else:
        template = recipe("Template", 1, active_allergens, active_meats, "")
        for item in active_recipe_list[:]:
            active = True # Item is active
            for item_2 in item._allergens:
                for item_3 in template._allergens:
                    if item_2 == item_3:
                        active = False
            for item_2 in item._meats:
                for item_3 in template._meats:
                    if item_2 == item_3:
                        active = False
            if active is False:
                active_recipe_list.remove(item)
        for item in recipe_list[:]:
            active = False
            for item_2 in active_recipe_list[:]:
                if item == item_2:
                    active = True
            if active is False:
                allergen_clear = True
                meat_clear = True
                for item_2 in item._allergens:
                    for item_3 in template._allergens:
                        if item_2 == item_3:
                            allergen_clear = False
                for item_2 in item._meats:
                    for item_3 in template._meats:
                        if item_2 == item_3:
                            meat_clear = False
                if allergen_clear is True and meat_clear is True:
                    active_recipe_list.append(item)
    showhide()

def uncheck_checkboxes(box_list):
    for item in box_list:
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)

# Recipe List (Temporary)
spag_bol = recipe("Spaghetti Bolognese", 2, ["Dairy", "Wheat"], ["Beef"], "Lorem Ipsum Dolor Sit Amet" )
cereal = recipe("Cereal", 0, ["Dairy"], [], "Lorem Ipsum Dolor Sit Amet")
recipe_list = [spag_bol, cereal]
active_recipe_list = []
active_course = []
active_allergens = []
active_meats = []
for item in recipe_list:
    active_recipe_list.append(item)
button_list = []
breakfast_checkbox.stateChanged.connect(lambda:course_checked(breakfast_checkbox, 0))
lunch_checkbox.stateChanged.connect(lambda:course_checked(lunch_checkbox, 1))
dinner_checkbox.stateChanged.connect(lambda:course_checked(dinner_checkbox, 2))
dessert_checkbox.stateChanged.connect(lambda:course_checked(dessert_checkbox, 3))
dairy_checkbox.stateChanged.connect(lambda:allergen_checked(dairy_checkbox, "Dairy"))
nuts_checkbox.stateChanged.connect(lambda:allergen_checked(nuts_checkbox, "Nuts"))
peanuts_checkbox.stateChanged.connect(lambda:allergen_checked(peanuts_checkbox, "Peanuts"))
wheat_checkbox.stateChanged.connect(lambda:allergen_checked(wheat_checkbox, "Wheat"))
shellfish_checkbox.stateChanged.connect(lambda:allergen_checked(shellfish_checkbox, "Shellfish"))
seafood_checkbox.stateChanged.connect(lambda:allergen_checked(seafood_checkbox, "Seafood"))
egg_checkbox.stateChanged.connect(lambda:allergen_checked(egg_checkbox, "Egg"))
soy_checkbox.stateChanged.connect(lambda:allergen_checked(soy_checkbox, "Soy"))
sesame_checkbox.stateChanged.connect(lambda:allergen_checked(sesame_checkbox, "Sesame"))
uncheck_allergens.clicked.connect(lambda:uncheck_checkboxes([dairy_checkbox, nuts_checkbox, peanuts_checkbox, wheat_checkbox, shellfish_checkbox, seafood_checkbox, egg_checkbox, soy_checkbox, sesame_checkbox]))
beef_checkbox.stateChanged.connect(lambda:meat_checked(beef_checkbox, "Beef"))
pork_checkbox.stateChanged.connect(lambda:meat_checked(pork_checkbox, "Pork"))
lamb_checkbox.stateChanged.connect(lambda:meat_checked(lamb_checkbox, "Lamb"))
poultry_checkbox.stateChanged.connect(lambda:meat_checked(poultry_checkbox, "Poultry"))
uncheck_meats.clicked.connect(lambda:uncheck_checkboxes([beef_checkbox, pork_checkbox, lamb_checkbox, poultry_checkbox]))

# App Execution
recipe_box_updater()
main.showMaximized()
app.exec()