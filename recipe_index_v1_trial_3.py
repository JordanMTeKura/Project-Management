# recipe_index.py
# Jordan Maloney
# 22/06/23
# Ver. 0.0.1

# Imports
from PySide6.QtWidgets import *
from dataclasses import dataclass

# Classes


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
# Course
course_widget = QWidget()
course_vbox = QHBoxLayout()
course_checkbox = QButtonGroup()
course_filter_label = QLabel ("Course")
breakfast_checkbox = QCheckBox("Breakfast")
lunch_checkbox = QCheckBox("Lunch")
dinner_checkbox = QCheckBox("Dinner")
dessert_checkbox = QCheckBox("Dessert")
# Allergens
allergens_widget = QWidget()
allergens_vbox = QHBoxLayout()
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
horizontal_divider.addStretch()
horizontal_divider.addWidget(divider_widget2)
divider_widget2.setLayout(subdivider_divwidget2)
subdivider_divwidget2.addWidget(categories_label)
subdivider_divwidget2.addWidget(course_widget)
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
subdivider_divwidget2.addWidget(allergens_widget)
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
allergens_vbox.addStretch()
subdivider_divwidget2.addStretch()

# Add/Edit/Remove Buttons part
subdivider_divwidget2.addWidget(aer_widget)
aer_widget.setLayout(aer_box)
aer_box.addWidget(add_button)
aer_box.addWidget(edit_button)
aer_box.addWidget(remove_button)

# Code for making buttons with multiple Labels (Reference when making the list of recipes that can be clicked on)
button = QPushButton()
button_divider = QHBoxLayout()
name_label = QLabel("Spaghetti Bolognese")
button_divider.addWidget(name_label)
course_label = QLabel("Dinner")
button_divider.addWidget(course_label)
content_label = QLabel("No")
button_divider.addWidget(content_label)
button.setFixedHeight(40)
button.setLayout(button_divider)
recipe_box.addWidget(button)

recipe_box.addStretch()

# App Execution
main.showMaximized()
app.exec()
