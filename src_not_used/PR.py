from rdflib import URIRef


class PR:
    pass
#     url = 'http://example.org/'
#     priority = URIRef(url + 'priority')
#     left_side = URIRef(url + 'left_side')
#     right_side = URIRef(url + 'right_side')
#     operation = URIRef(url + 'operation')
#     child = URIRef(url + 'child')
#     variable_x = URIRef(url + 'variable_x')
#     variable_y = URIRef(url + 'variable_y')
#     variable_z = URIRef(url + 'variable_z')
#
#     rule_human_socrates = URIRef(url + 'rule_human_socrates')
#     human = URIRef(url + 'human')
#     socrates = URIRef(url + 'socrates')
#     platon = URIRef(url + 'platon')
#     rule_human_mortal = URIRef(url + 'rule_human_mortal')
#     # rule_human_mortal_left = URIRef(url + 'rule_human_mortal_left')
#     mortal = URIRef(url + 'mortal')
#     # rule_human_mortal_right01 = URIRef(url + 'rule_human_mortal_right01')
#     # rule_human_mortal_right01_child = URIRef(url + 'rule_human_mortal_right01_child')
#
#     one = URIRef(url + 'one')
#     two = URIRef(url + 'two')
#     three = URIRef(url + 'three')
#     four = URIRef(url + 'four')
#     five = URIRef(url + 'five')
#     six = URIRef(url + 'six')
#     seven = URIRef(url + 'seven')
#     eight = URIRef(url + 'eight')
#     nine = URIRef(url + 'nine')
#     ten = URIRef(url + 'ten')
#
#     next_number = URIRef(url + 'next_number')
#     rule_next_number_x_y = URIRef(url + 'rule_next_number_x_y')
#     # rule_next_number_x_y_left = URIRef(url + 'rule_next_number_x_y_left')
#     # rule_next_number_x_y_right01 = URIRef(url + 'rule_next_number_x_y_right01')
#     # rule_next_number_x_y_right01_child = URIRef(url + 'rule_next_number_x_y_right01_child')
#     next_number_1_2 = URIRef(url + 'next_number_1_2')
#     next_number_2_3 = URIRef(url + 'next_number_2_3')
#     next_number_3_4 = URIRef(url + 'next_number_3_4')
#     next_number_4_5 = URIRef(url + 'next_number_4_5')
#     next_number_5_6 = URIRef(url + 'next_number_5_6')
#     next_number_6_7 = URIRef(url + 'next_number_6_7')
#     next_number_7_8 = URIRef(url + 'next_number_7_8')
#     next_number_8_9 = URIRef(url + 'next_number_8_9')
#     next_number_9_10 = URIRef(url + 'next_number_9_10')
#
#     add_number = URIRef(url + 'add_number')
#
#     rule_add_number_x_1_z = URIRef(url + 'rule_add_number_x_1_z')
#     # rule_add_number_x_1_z_left = URIRef(url + 'rule_add_number_x_1_z_left')
#     # rule_add_number_x_1_z_right01 = URIRef(url + 'rule_add_number_x_1_z_right01')
#     # rule_add_number_x_1_z_right01_child = URIRef(url + 'rule_add_number_x_1_z_right01_child')
#
#     rule_add_number_x_y_z = URIRef(url + 'rule_add_number_x_y_z')
#     # rule_add_number_x_y_z_left = URIRef(url + 'rule_add_number_x_y_z_left')
#     # rule_add_number_x_y_z_right01 = URIRef(url + 'rule_add_number_x_y_z_right01')
#     # rule_add_number_x_y_z_right01_child = URIRef(url + 'rule_add_number_x_y_z_right01_child')
#     # rule_add_number_x_y_z_right02 = URIRef(url + 'rule_add_number_x_y_z_right02')
#     # rule_add_number_x_y_z_right02_child = URIRef(url + 'rule_add_number_x_y_z_right02_child')
#     # rule_add_number_x_y_z_right03 = URIRef(url + 'rule_add_number_x_y_z_right03')
#     # rule_add_number_x_y_z_right03_child = URIRef(url + 'rule_add_number_x_y_z_right03_child')
#
#     father = URIRef(url+'father')
#     mother = URIRef(url+'mother')
#     grandfather = URIRef(url+'grandfather')
#     # child_is = URIRef(url+'child_is')
#     # father_is = URIRef(url+'father_is')
#     # mother_is = URIRef(url+'mother_is')
#     grandfather_father_father = URIRef(url+'grandfather_father_father')
#     # grandfather_father_father_left = URIRef(url+'grandfather_father_father_left')
#     # grandfather_father_father_right = URIRef(url+'grandfather_father_father_right')
#     # grandfather_father_father_right01 = URIRef(url+'grandfather_father_father_right01')
#     # grandfather_father_father_right01_child = URIRef(url+'grandfather_father_father_right01_child')
#     # grandfather_father_father_right02 = URIRef(url+'grandfather_father_father_right02')
#     # grandfather_father_father_right02_child = URIRef(url+'grandfather_father_father_right02_child')
#     grandfather_mother_father = URIRef(url+'grandfather_mother_father')
#     # grandfather_mother_father_left = URIRef(url+'grandfather_mother_father_left')
#     # grandfather_mother_father_right = URIRef(url+'grandfather_mother_father_right')
#     # grandfather_mother_father_right01 = URIRef(url+'grandfather_mother_father_right01')
#     # grandfather_mother_father_right01_child = URIRef(url+'grandfather_mother_father_right01_child')
#     # grandfather_mother_father_right02 = URIRef(url+'grandfather_mother_father_right02')
#     # grandfather_mother_father_right02_child = URIRef(url+'grandfather_mother_father_right02_child')
#
#     taro = URIRef(url+'taro')
#     jiro = URIRef(url+'jiro')
#     ichiro = URIRef(url+'ichiro')
#     hana = URIRef(url+'hana')
#     rule_father_jiro_taro = URIRef(url+'rule_father_jiro_taro')
#     rule_mother_jiro_hana = URIRef(url+'rule_mother_jiro_hana')
#     rule_father_hana_ichiro = URIRef(url+'rule_father_hana_ichiro')
#
#     knows = URIRef(url+'knows')
#     knows_direct = URIRef(url+'knows_direct')
#     knows_indirect = URIRef(url+'knows_indirect')
#     knows_indirect1 = URIRef(url+'knows_indirect1')
#     knows_indirect2 = URIRef(url+'knows_indirect2')
#     andy = URIRef(url+'andy')
#     bob = URIRef(url+'bob')
#     chris = URIRef(url+'chris')
#     david = URIRef(url+'david')
#     edgar = URIRef(url+'edgar')
