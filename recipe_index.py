# recipe_index.py
# Jordan Maloney
# 2/07/23
# Ver. 0.2.0

# Imports
from dataclasses import dataclass
import PySide6.QtGui
from PySide6.QtWidgets import *
from PySide6 import QtCore
import pickle
from pathlib import Path

root = Path("save")
my_path = root / "data.obj"

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

class main_window(QMainWindow):
    def __init__(self, parent=None):
        super(main_window, self).__init__(parent)

    def closeEvent(self, event):
        global saved_changes
        global recipe_list
        if saved_changes != recipe_list:
            alert = QMessageBox.warning(None, "Warning!", "Save changes before quitting?", buttons=QMessageBox.Yes | QMessageBox.No)
            if alert == QMessageBox.Yes:
                fileobj = open(my_path, "wb")
                pickle.dump(recipe_list, fileobj)
                fileobj.close()
                saved_changes.clear()
                for item in recipe_list:
                    saved_changes.append(item)
    def keyPressEvent(self, event):
        if event.modifiers() & QtCore.Qt.ControlModifier:
            if event.key() == QtCore.Qt.Key_S:
                save(recipe_list, saved_changes)


# Widgets
app = QApplication()
main = main_window()
central_widget = QWidget()
horizontal_divider = QHBoxLayout()
divider_widget1 = QWidget()
recipe_box = QVBoxLayout()
recipe_widget1 = QWidget()
recipe_info = QHBoxLayout()
recipe_name = QLabel("Recipe")
recipe_course = QLabel("Course")
recipe_vegan = QLabel("Vegan?")
scroll_widget = QScrollArea()
recipe_area_widget = QWidget()
recipe_area = QVBoxLayout()
divider_widget2 = QWidget()
subdivider_divwidget2 = QVBoxLayout()
save_widget = QWidget()
save_layout = QHBoxLayout()
save_button = QPushButton("Save")
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
meats_filter_label = QLabel("Meat content")
beef_checkbox = QCheckBox("Beef")
pork_checkbox = QCheckBox("Pork")
lamb_checkbox = QCheckBox("Lamb")
poultry_checkbox = QCheckBox("Poultry")
no_meats = QCheckBox("None")
# Add/Edit/Remove Buttons
aer_widget = QWidget()
aer_box = QHBoxLayout()
add_button = QPushButton("Add Recipe")


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
recipe_box.addWidget(scroll_widget)
scroll_widget.setWidget(recipe_area_widget)
recipe_area_widget.setLayout(recipe_area)
scroll_widget.setWidgetResizable(True)

# Search Filters part
horizontal_divider.addWidget(divider_widget2)
divider_widget2.setLayout(subdivider_divwidget2)
subdivider_divwidget2.addWidget(save_widget)
save_widget.setLayout(save_layout)
save_layout.addStretch()
save_layout.addWidget(save_button)
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
course_filter_label.setStyleSheet("font-weight: bold")
course_vbox.addWidget(course_filter_label)
course_vbox.addWidget(breakfast_checkbox)
course_vbox.addWidget(lunch_checkbox)
course_vbox.addWidget(dinner_checkbox)
course_vbox.addWidget(dessert_checkbox)
course_vbox.addStretch()
categories_box.addWidget(allergens_widget)
allergens_widget.setLayout(allergens_vbox)
allergens_filter_label.setStyleSheet("font-weight: bold")
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
meats_filter_label.setStyleSheet("font-weight: bold")
meats_vbox.addWidget(meats_filter_label)
meats_vbox.addWidget(beef_checkbox)
meats_vbox.addWidget(pork_checkbox)
meats_vbox.addWidget(lamb_checkbox)
meats_vbox.addWidget(poultry_checkbox)
meats_vbox.addWidget(no_meats)
meats_vbox.addStretch()

# Add/Edit/Remove Buttons part
subdivider_divwidget2.addWidget(aer_widget)
aer_widget.setLayout(aer_box)
aer_box.addWidget(add_button)

# Code for making buttons with multiple Labels (Reference when making the list of recipes that can be clicked on)
def recipe_box_updater():
    for item in recipe_list:
        button = QPushButton()
        courses = ["Breakfast", "Lunch", "Dinner", "Dessert"]
        course_colours = ["effb6d", "04dd00", "ff4700", "00ccff"]
        button.setStyleSheet("background-color: #{}".format(course_colours[item._course]))
        button_divider = QHBoxLayout()
        name_label = QLabel(item._name)
        button_divider.addWidget(name_label)
        course_label = QLabel(courses[item._course])
        button_divider.addWidget(course_label)
        if len(item._meats) != 0:
            content_label = QLabel("No")
        elif "Dairy" in item._allergens:
            content_label = QLabel("No")
        elif "Shellfish" in item._allergens:
            content_label = QLabel("No")
        elif "Seafood" in item._allergens:
            content_label = QLabel("No")
        elif "Egg" in item._allergens:
            content_label = QLabel("No")
        else:
            content_label = QLabel("Yes")
        button_divider.addWidget(content_label)
        button.setFixedHeight(40)
        button.setLayout(button_divider)
        recipe_area.addWidget(button)
        this_dict = {
            "name" : item._name,
            "button" : button}
        button_list.append(this_dict)
    for item in button_list:
        button_connector(item)
    recipe_area.addStretch()

def button_connector(item):
    item["button"].clicked.connect(lambda:view_recipe(item["name"]))

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
    no_meats.setCheckState(QtCore.Qt.CheckState.Unchecked)
    if "None" in active_meats:
        active_meats.remove("None")

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
            if len(active_meats) >= 1:
                if active_meats[0] == "None":
                    if len(item._meats) >= 1:
                        active = False
                else:
                    meat_clear = False
                    for item_2 in item._meats:
                        for item_3 in template._meats:
                            if item_2 == item_3:
                                meat_clear = True
                    if meat_clear is False:
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
                if len(active_meats) >= 1:
                    if active_meats[0] == "None":
                        if len(item._meats) >= 1:
                            meat_clear = False
                    else:
                        meat_clear = False
                        for item_2 in item._meats:
                            for item_3 in template._meats:
                                if item_2 == item_3:
                                    meat_clear = True
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
            if len(active_meats) >= 1:
                if active_meats[0] == "None":
                    if len(item._meats) >= 1:
                        active = False
                else:
                    meat_clear = False
                    for item_2 in item._meats:
                        for item_3 in template._meats:
                            if item_2 == item_3:
                                meat_clear = True
                    if meat_clear is False:
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
                if len(active_meats) >= 1:
                    if active_meats[0] == "None":
                        if len(item._meats) >= 1:
                            meat_clear = False
                    else:
                        meat_clear = False
                        for item_2 in item._meats:
                            for item_3 in template._meats:
                                if item_2 == item_3:
                                    meat_clear = True
                if allergen_clear is True and meat_clear is True:
                    active_recipe_list.append(item)
    showhide()

def uncheck_checkboxes(box_list, meat_check):
    for item in box_list:
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
    if meat_check is True:
        active_meats.clear()
        if no_meats.checkState() == QtCore.Qt.CheckState.Checked:
            active_meats.append("None")
    recipe_filter()

def view_recipe(name):
    recipe_window = QDialog()
    for item in recipe_list:
        if item._name == name:
            recipe_window.setWindowTitle(item._name)
            window_header = QLabel(item._name)
            window_body = QScrollArea()
            window_body_text = QLabel(item._instructions)
            window_body_text.setWordWrap(True)
    recipe_win_layout = QVBoxLayout()
    button_widget = QWidget()
    button_layout = QHBoxLayout()
    edit_button = QPushButton("Edit")
    delete_button = QPushButton("Delete")
    recipe_window.setLayout(recipe_win_layout)
    recipe_win_layout.addWidget(window_header)
    recipe_win_layout.addWidget(window_body)
    window_body.setWidget(window_body_text)
    recipe_win_layout.addWidget(button_widget)
    button_widget.setLayout(button_layout)
    button_layout.addStretch()
    button_layout.addWidget(edit_button)
    button_layout.addWidget(delete_button)
    for item in recipe_list:
        if item._name == name:
            this_recipe = item
    edit_button.clicked.connect(lambda:edit_recipe(this_recipe, recipe_window))
    delete_button.clicked.connect(lambda:delete_recipe(this_recipe, recipe_window))
    recipe_window.setFixedSize(recipe_window.width(), recipe_window.height())
    recipe_window.exec()


def add_recipe():
    class changes_window(QDialog):
        def __init__(self, parent=None):
            super(changes_window, self).__init__(parent)

        def closeEvent(self, event):
            cancellation = False
            cancellation = close_clicked()
            if cancellation is True:
                event.ignore()

        def keyPressEvent(self, event):
            if event.key() == QtCore.Qt.Key_Escape:
                close_function()

    add_window = changes_window()
    add_window.setWindowTitle("Add Recipe")
    add_layout = QVBoxLayout()
    add_name_widget = QWidget()
    add_name = QHBoxLayout()
    add_name_text = QLabel("Recipe Name:")
    add_name_input = QLineEdit()
    add_course_widget = QWidget()
    add_course = QHBoxLayout()
    add_course_text = QLabel("Course:")
    add_course_input = QComboBox()
    add_allergens_widget = QWidget()
    add_allergens = QHBoxLayout()
    add_allergens_text = QLabel("Allergens:")
    add_dairy = QCheckBox("Dairy")
    add_nuts = QCheckBox("Nuts")
    add_peanuts = QCheckBox("Peanuts")
    add_wheat = QCheckBox("Wheat")
    add_shellfish = QCheckBox("Shellfish")
    add_seafood = QCheckBox("Seafood")
    add_egg = QCheckBox("Eggs")
    add_soy = QCheckBox("Soy")
    add_sesame = QCheckBox("Sesame")
    add_meats_widget = QWidget()
    add_meats = QHBoxLayout()
    add_meats_text = QLabel("Meats:")
    add_beef = QCheckBox("Beef")
    add_pork = QCheckBox("Pork")
    add_lamb = QCheckBox("Lamb")
    add_poultry = QCheckBox("Poultry")
    add_desc_widget = QWidget()
    add_description = QHBoxLayout()
    add_desc_text = QLabel("Description:")
    add_desc_input = QTextEdit()
    buttons_widget = QWidget()
    buttons = QHBoxLayout()
    confirm = QPushButton("Create")
    cancel = QPushButton("Cancel")

    add_window.setLayout(add_layout)
    add_layout.addWidget(add_name_widget)
    add_name_widget.setLayout(add_name)
    add_name.addWidget(add_name_text)
    add_name.addWidget(add_name_input)
    add_name_input.setPlaceholderText("Enter the recipe's name here")
    add_layout.addWidget(add_course_widget)
    add_course_widget.setLayout(add_course)
    add_course.addWidget(add_course_text)
    add_course.addWidget(add_course_input)
    add_course_input.addItem("Breakfast")
    add_course_input.addItem("Lunch")
    add_course_input.addItem("Dinner")
    add_course_input.addItem("Dessert")
    add_course_input.setPlaceholderText("Click to expand")
    add_course_input.setCurrentIndex(-1)
    add_course.addStretch()
    add_layout.addWidget(add_allergens_widget)
    add_allergens_widget.setLayout(add_allergens)
    add_allergens.addWidget(add_allergens_text)
    add_allergens.addWidget(add_dairy)
    add_allergens.addWidget(add_nuts)
    add_allergens.addWidget(add_peanuts)
    add_allergens.addWidget(add_wheat)
    add_allergens.addWidget(add_shellfish)
    add_allergens.addWidget(add_seafood)
    add_allergens.addWidget(add_egg)
    add_allergens.addWidget(add_soy)
    add_allergens.addWidget(add_sesame)
    add_allergens.addStretch()
    add_layout.addWidget(add_meats_widget)
    add_meats_widget.setLayout(add_meats)
    add_meats.addWidget(add_meats_text)
    add_meats.addWidget(add_beef)
    add_meats.addWidget(add_pork)
    add_meats.addWidget(add_lamb)
    add_meats.addWidget(add_poultry)
    add_meats.addStretch()
    add_layout.addWidget(add_desc_widget)
    add_desc_widget.setLayout(add_description)
    add_description.addWidget(add_desc_text)
    add_description.addWidget(add_desc_input)
    add_desc_input.setPlaceholderText("Enter ingredients & recipe here")
    add_layout.addWidget(buttons_widget)
    buttons_widget.setLayout(buttons)
    buttons.addStretch()
    buttons.addWidget(confirm)
    buttons.addWidget(cancel)
    add_layout.addStretch()

    add_allergens_list = []
    add_meats_list = []

    def add_category_list(item, itembox, category):
        if itembox.isChecked() is True:
            category.append(item)
        elif itembox.isChecked() is False:
            category.remove(item)
    
    add_dairy.stateChanged.connect(lambda:add_category_list("Dairy", add_dairy, add_allergens_list))
    add_nuts.stateChanged.connect(lambda:add_category_list("Nuts", add_nuts, add_allergens_list))
    add_peanuts.stateChanged.connect(lambda:add_category_list("Peanuts", add_peanuts, add_allergens_list))
    add_wheat.stateChanged.connect(lambda:add_category_list("Wheat", add_wheat, add_allergens_list))
    add_shellfish.stateChanged.connect(lambda:add_category_list("Shellfish", add_shellfish, add_allergens_list))
    add_seafood.stateChanged.connect(lambda:add_category_list("Seafood", add_seafood, add_allergens_list))
    add_egg.stateChanged.connect(lambda:add_category_list("Egg", add_egg, add_allergens_list))
    add_soy.stateChanged.connect(lambda:add_category_list("Soy", add_soy, add_allergens_list))
    add_sesame.stateChanged.connect(lambda:add_category_list("Sesame", add_sesame, add_allergens_list))
    add_beef.stateChanged.connect(lambda:add_category_list("Beef", add_beef, add_meats_list))
    add_pork.stateChanged.connect(lambda:add_category_list("Pork", add_pork, add_meats_list))
    add_lamb.stateChanged.connect(lambda:add_category_list("Lamb", add_lamb, add_meats_list))
    add_poultry.stateChanged.connect(lambda:add_category_list("Poultry", add_poultry, add_meats_list))

    def create_clicked():
        valid = True
        original = True
        for item in recipe_list:
            if item._name == add_name_input.text():
                original = False
        if original is False:
            valid = False
            error = "A recipe with that name already exists."
        elif len(add_name_input.text()) == 0:
            valid = False
            error = "You must assign the recipe a name."
        elif add_course_input.currentIndex() == -1:
            valid = False
            error = "You must assign the recipe a course."
        elif len(add_desc_input.toPlainText()) == 0:
            valid = False
            error = "You must assign the recipe a description."
        if valid is False:
            alert = QMessageBox.critical(None, "Error!", error, buttons=QMessageBox.Ok)
        elif valid is True:
            alert = QMessageBox.question(None, "Create?", "Are you sure you would like to create this recipe?", buttons=QMessageBox.Yes | QMessageBox.No)
            if alert == QMessageBox.Yes:
                create_recipe()
                add_name_input.setText("")
                add_course_input.setCurrentIndex(-1)
                add_allergens_list.clear()
                add_meats_list.clear()
                add_desc_input.setPlainText("")
                add_window.close()

    def close_clicked():
        changes = False
        if add_name_input.text() != "":
            changes = True
        if add_course_input.currentIndex() != -1:
            changes = True
        if len(add_allergens_list) != 0:
            changes = True
        if len(add_meats_list) != 0:
            changes = True
        if len(add_desc_input.toPlainText()) != 0:
            changes = True
        if changes is False:
            add_window.close()
        if changes is True:
            alert = QMessageBox.warning(None, "Warning!", "Changes made will not be saved. Close Recipe Maker?", buttons=QMessageBox.Yes | QMessageBox.No)
            if alert == QMessageBox.Yes:
                add_window.close()
            elif alert == QMessageBox.No:
                try:
                    return True
                except:
                    pass
    
    def close_function():
        add_window.close()

    def create_recipe():
        item = recipe(add_name_input.text(), add_course_input.currentIndex(), add_allergens_list[:], add_meats_list[:], add_desc_input.toPlainText())
        recipe_list.append(item)
        button = QPushButton()
        courses = ["Breakfast", "Lunch", "Dinner", "Dessert"]
        course_colours = ["effb6d", "04dd00", "ff4700", "00ccff"]
        button.setStyleSheet("background-color: #{}".format(course_colours[item._course]))
        button_divider = QHBoxLayout()
        name_label = QLabel(item._name)
        button_divider.addWidget(name_label)
        course_label = QLabel(courses[item._course])
        button_divider.addWidget(course_label)
        if len(item._meats) != 0:
            content_label = QLabel("No")
        elif "Dairy" in item._allergens:
            content_label = QLabel("No")
        elif "Shellfish" in item._allergens:
            content_label = QLabel("No")
        elif "Seafood" in item._allergens:
            content_label = QLabel("No")
        elif "Egg" in item._allergens:
            content_label = QLabel("No")
        else:
            content_label = QLabel("Yes")
        button_divider.addWidget(content_label)
        button.setFixedHeight(40)
        button.setLayout(button_divider)
        recipe_area.insertWidget((recipe_area.count()-1), button)
        this_dict = {
            "name" : item._name,
            "button" : button}
        button_list.append(this_dict)
        button_list[button_list.index(this_dict)]["button"].clicked.connect(lambda:view_recipe(button_list[button_list.index(this_dict)]["name"]))
        recipe_filter()

    confirm.clicked.connect(create_clicked)
    cancel.clicked.connect(close_function)
    add_window.setFixedSize(add_window.width(), add_window.height())
    add_window.exec()

def edit_recipe(item, recipe_window):
    class changes_window(QDialog):
        def __init__(self, parent=None):
            super(changes_window, self).__init__(parent)

        def closeEvent(self, event):
            cancellation = False
            cancellation = close_clicked()
            if cancellation is True:
                event.ignore()

        def keyPressEvent(self, event):
            if event.key() == QtCore.Qt.Key_Escape:
                close_function()

    edit_window = changes_window()
    edit_window.setWindowTitle("Edit Recipe")
    edit_layout = QVBoxLayout()
    edit_name_widget = QWidget()
    edit_name = QHBoxLayout()
    edit_name_text = QLabel("Recipe Name:")
    edit_name_input = QLineEdit()
    edit_course_widget = QWidget()
    edit_course = QHBoxLayout()
    edit_course_text = QLabel("Course:")
    edit_course_input = QComboBox()
    edit_allergens_widget = QWidget()
    edit_allergens = QHBoxLayout()
    edit_allergens_text = QLabel("Allergens:")
    edit_dairy = QCheckBox("Dairy")
    edit_nuts = QCheckBox("Nuts")
    edit_peanuts = QCheckBox("Peanuts")
    edit_wheat = QCheckBox("Wheat")
    edit_shellfish = QCheckBox("Shellfish")
    edit_seafood = QCheckBox("Seafood")
    edit_egg = QCheckBox("Eggs")
    edit_soy = QCheckBox("Soy")
    edit_sesame = QCheckBox("Sesame")
    edit_meats_widget = QWidget()
    edit_meats = QHBoxLayout()
    edit_meats_text = QLabel("Meats:")
    edit_beef = QCheckBox("Beef")
    edit_pork = QCheckBox("Pork")
    edit_lamb = QCheckBox("Lamb")
    edit_poultry = QCheckBox("Poultry")
    edit_desc_widget = QWidget()
    edit_description = QHBoxLayout()
    edit_desc_text = QLabel("Description:")
    edit_desc_input = QTextEdit()
    buttons_widget = QWidget()
    buttons = QHBoxLayout()
    confirm = QPushButton("Save Changes")
    cancel = QPushButton("Cancel")

    edit_window.setLayout(edit_layout)
    edit_layout.addWidget(edit_name_widget)
    edit_name_widget.setLayout(edit_name)
    edit_name.addWidget(edit_name_text)
    edit_name.addWidget(edit_name_input)
    edit_name_input.setPlaceholderText("Enter the recipe's name here")
    edit_name_input.setText(item._name)
    edit_layout.addWidget(edit_course_widget)
    edit_course_widget.setLayout(edit_course)
    edit_course.addWidget(edit_course_text)
    edit_course.addWidget(edit_course_input)
    edit_course_input.addItem("Breakfast")
    edit_course_input.addItem("Lunch")
    edit_course_input.addItem("Dinner")
    edit_course_input.addItem("Dessert")
    edit_course_input.setPlaceholderText("Click to expand")
    edit_course_input.setCurrentIndex(item._course)
    edit_course.addStretch()
    edit_layout.addWidget(edit_allergens_widget)
    edit_allergens_widget.setLayout(edit_allergens)
    edit_allergens.addWidget(edit_allergens_text)
    edit_allergens.addWidget(edit_dairy)
    edit_allergens.addWidget(edit_nuts)
    edit_allergens.addWidget(edit_peanuts)
    edit_allergens.addWidget(edit_wheat)
    edit_allergens.addWidget(edit_shellfish)
    edit_allergens.addWidget(edit_seafood)
    edit_allergens.addWidget(edit_egg)
    edit_allergens.addWidget(edit_soy)
    edit_allergens.addWidget(edit_sesame)
    edit_allergens.addStretch()
    edit_layout.addWidget(edit_meats_widget)
    edit_meats_widget.setLayout(edit_meats)
    edit_meats.addWidget(edit_meats_text)
    edit_meats.addWidget(edit_beef)
    edit_meats.addWidget(edit_pork)
    edit_meats.addWidget(edit_lamb)
    edit_meats.addWidget(edit_poultry)
    edit_meats.addStretch()
    edit_layout.addWidget(edit_desc_widget)
    edit_desc_widget.setLayout(edit_description)
    edit_description.addWidget(edit_desc_text)
    edit_description.addWidget(edit_desc_input)
    edit_desc_input.setPlaceholderText("Enter ingredients & recipe here")
    edit_desc_input.setPlainText(item._instructions)
    edit_layout.addWidget(buttons_widget)
    buttons_widget.setLayout(buttons)
    buttons.addStretch()
    buttons.addWidget(confirm)
    buttons.addWidget(cancel)
    edit_layout.addStretch()

    edit_allergens_list = item._allergens
    edit_meats_list = item._meats

    def checkbox_defaulter(checkbox, item, list):
        for item_2 in list:
            if item_2 == item:
                checkbox.setCheckState(QtCore.Qt.CheckState.Checked)
    
    checkbox_defaulter(edit_dairy, "Dairy", edit_allergens_list)
    checkbox_defaulter(edit_nuts, "Nuts", edit_allergens_list)
    checkbox_defaulter(edit_peanuts, "Peanuts", edit_allergens_list)
    checkbox_defaulter(edit_wheat, "Wheat", edit_allergens_list)
    checkbox_defaulter(edit_shellfish, "Shellfish", edit_allergens_list)
    checkbox_defaulter(edit_seafood, "Seafood", edit_allergens_list)
    checkbox_defaulter(edit_egg, "Egg", edit_allergens_list)
    checkbox_defaulter(edit_soy, "Soy", edit_allergens_list)
    checkbox_defaulter(edit_sesame, "Sesame", edit_allergens_list)
    checkbox_defaulter(edit_beef, "Beef", edit_meats_list)
    checkbox_defaulter(edit_pork, "Pork", edit_meats_list)
    checkbox_defaulter(edit_lamb, "Lamb", edit_meats_list)
    checkbox_defaulter(edit_poultry, "Poultry", edit_meats_list)

    def add_category_list(item, itembox, category):
        if itembox.isChecked() is True:
            category.append(item)
        elif itembox.isChecked() is False:
            category.remove(item)
    
    edit_dairy.stateChanged.connect(lambda:add_category_list("Dairy", edit_dairy, edit_allergens_list))
    edit_nuts.stateChanged.connect(lambda:add_category_list("Nuts", edit_nuts, edit_allergens_list))
    edit_peanuts.stateChanged.connect(lambda:add_category_list("Peanuts", edit_peanuts, edit_allergens_list))
    edit_wheat.stateChanged.connect(lambda:add_category_list("Wheat", edit_wheat, edit_allergens_list))
    edit_shellfish.stateChanged.connect(lambda:add_category_list("Shellfish", edit_shellfish, edit_allergens_list))
    edit_seafood.stateChanged.connect(lambda:add_category_list("Seafood", edit_seafood, edit_allergens_list))
    edit_egg.stateChanged.connect(lambda:add_category_list("Egg", edit_egg, edit_allergens_list))
    edit_soy.stateChanged.connect(lambda:add_category_list("Soy", edit_soy, edit_allergens_list))
    edit_sesame.stateChanged.connect(lambda:add_category_list("Sesame", edit_sesame, edit_allergens_list))
    edit_beef.stateChanged.connect(lambda:add_category_list("Beef", edit_beef, edit_meats_list))
    edit_pork.stateChanged.connect(lambda:add_category_list("Pork", edit_pork, edit_meats_list))
    edit_lamb.stateChanged.connect(lambda:add_category_list("Lamb", edit_lamb, edit_meats_list))
    edit_poultry.stateChanged.connect(lambda:add_category_list("Poultry", edit_poultry, edit_meats_list))

    def create_clicked():
        valid = True
        original = True
        for item_2 in recipe_list:
            if item_2._name == edit_name_input.text() and item_2 != item:
                original = False
        if original is False:
            valid = False
            error = "A recipe with that name already exists."
        elif len(edit_name_input.text()) == 0:
            valid = False
            error = "You must assign the recipe a name."
        elif edit_course_input.currentIndex() == -1:
            valid = False
            error = "You must assign the recipe a course."
        elif len(edit_desc_input.toPlainText()) == 0:
            valid = False
            error = "You must assign the recipe a description."
        if valid is False:
            alert = QMessageBox.critical(None, "Error!", error, buttons=QMessageBox.Ok)
        elif valid is True:
            alert = QMessageBox.question(None, "Save Changes?", "Are you sure you would like to save these changes?", buttons=QMessageBox.Yes | QMessageBox.No)
            if alert == QMessageBox.Yes:
                change_recipe()
                edit_name_input.setText(item._name)
                edit_course_input.setCurrentIndex(item._course)
                edit_allergens_list = item._allergens
                edit_meats_list = item._meats
                edit_desc_input.setPlainText(item._instructions)
                edit_window.close()
                recipe_window.close()

    def close_clicked():
        changes = False
        if edit_name_input.text() != item._name:
            changes = True
        if edit_course_input.currentIndex() != item._course:
            changes = True
        if len(edit_allergens_list) != len(item._allergens):
            changes = True
        if len(edit_meats_list) != len(item._meats):
            changes = True
        if len(edit_desc_input.toPlainText()) != len(item._instructions):
            changes = True
        if changes is False:
            edit_window.close()
        if changes is True:
            alert = QMessageBox.warning(None, "Warning!", "Changes made will not be saved. Close Recipe Editor?", buttons=QMessageBox.Yes | QMessageBox.No)
            if alert == QMessageBox.Yes:
                edit_window.close()
            elif alert == QMessageBox.No:
                try:
                    return True
                except:
                    pass
    
    def close_function():
        edit_window.close()

    def change_recipe():
        new_item = recipe(edit_name_input.text(), edit_course_input.currentIndex(), edit_allergens_list[:], edit_meats_list[:], edit_desc_input.toPlainText())
        recipe_list[recipe_list.index(item)] = new_item
        for item_2 in active_recipe_list:
            if item_2 == item:
                active_recipe_list.remove(item)
        button = QPushButton()
        courses = ["Breakfast", "Lunch", "Dinner", "Dessert"]
        course_colours = ["effb6d", "04dd00", "ff4700", "00ccff"]
        button.setStyleSheet("background-color: #{}".format(course_colours[new_item._course]))
        button_divider = QHBoxLayout()
        name_label = QLabel(new_item._name)
        button_divider.addWidget(name_label)
        course_label = QLabel(courses[new_item._course])
        button_divider.addWidget(course_label)
        if len(new_item._meats) != 0:
            content_label = QLabel("No")
        elif "Dairy" in new_item._allergens:
            content_label = QLabel("No")
        elif "Shellfish" in new_item._allergens:
            content_label = QLabel("No")
        elif "Seafood" in new_item._allergens:
            content_label = QLabel("No")
        elif "Egg" in new_item._allergens:
            content_label = QLabel("No")
        else:
            content_label = QLabel("Yes")
        button_divider.addWidget(content_label)
        button.setFixedHeight(40)
        button.setLayout(button_divider)
        for old_button in button_list:
            if old_button["name"] == item._name:
                replace_button = old_button["button"]
        recipe_area.replaceWidget(replace_button, button)
        replace_button.hide()
        this_dict = {
            "name" : new_item._name,
            "button" : button}
        for old_dict in button_list:
            if old_dict["name"] == item._name:
                button_list[button_list.index(old_dict)] = this_dict

        button_list[button_list.index(this_dict)]["button"].clicked.connect(lambda:view_recipe(button_list[button_list.index(this_dict)]["name"]))
        recipe_filter()

    confirm.clicked.connect(create_clicked)
    cancel.clicked.connect(close_function)
    edit_window.setFixedSize(edit_window.width(), edit_window.height())
    edit_window.exec()

def delete_recipe(item, recipe_window):
    confirmation = QMessageBox.warning(None, "Confirmation", "Are you sure you would like to delete this recipe? This cannot be undone.", buttons=QMessageBox.Yes | QMessageBox.No)
    if confirmation == QMessageBox.Yes:
        for item_2 in button_list[:]:
            if item_2["name"] == item._name:
                button_to_remove = item_2["button"]
                button_list.remove(item_2)
        recipe_area.removeWidget(button_to_remove)
        button_to_remove.hide()
        recipe_list.remove(item)
        for item_2 in active_recipe_list[:]:
            if item_2 == item:
                active_recipe_list.remove(item)
        recipe_window.close()



# Recipe List (Temporary)
spag_bol = recipe("Spaghetti Bolognese", 2, ["Dairy", "Wheat"], ["Beef"], "Lorem ipsum dolor sit amet")
cereal = recipe("Cereal", 0, ["Dairy"], [], "Lorem Ipsum Dolor Sit Amet")
def load():
    try:
        fileobj = open(my_path, "rb")
        recipe_list = pickle.load(fileobj)
        fileobj.close()
    except:
        recipe_list = []
    return recipe_list
def save(s, saved_changes):
    if saved_changes != recipe_list:
        query = QMessageBox.question(None, "Save?", "Save Changes?", buttons=QMessageBox.Yes | QMessageBox.No)
        if query == QMessageBox.Yes:
            fileobj = open(my_path, "wb")
            pickle.dump(recipe_list, fileobj)
            fileobj.close()
            saved_changes.clear()
            for item in recipe_list:
                saved_changes.append(item)
recipe_list = load()
saved_changes = recipe_list[:]
save_button.clicked.connect(lambda: save(recipe_list, saved_changes))
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
uncheck_allergens.clicked.connect(lambda:uncheck_checkboxes([dairy_checkbox, nuts_checkbox, peanuts_checkbox, wheat_checkbox, shellfish_checkbox, seafood_checkbox, egg_checkbox, soy_checkbox, sesame_checkbox], False))
beef_checkbox.clicked.connect(lambda:meat_checked(beef_checkbox, "Beef"))
pork_checkbox.clicked.connect(lambda:meat_checked(pork_checkbox, "Pork"))
lamb_checkbox.clicked.connect(lambda:meat_checked(lamb_checkbox, "Lamb"))
poultry_checkbox.clicked.connect(lambda:meat_checked(poultry_checkbox, "Poultry"))
no_meats.clicked.connect(lambda:uncheck_checkboxes([beef_checkbox, pork_checkbox, lamb_checkbox, poultry_checkbox], True))
add_button.clicked.connect(add_recipe)

# App Execution
recipe_box_updater()
main.showMaximized()
app.exec()