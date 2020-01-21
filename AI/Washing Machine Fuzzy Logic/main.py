# -*- coding: utf-8 -*-from skfuzzy import control as ctrl
import skfuzzy as fuzz
import numpy as np
from skfuzzy import control as ctrl

class WashingMachine:

    degree_dirt = ctrl.Antecedent(np.arange(0, 101, 1), 'degree_dirt')
    detergent_quantity = ctrl.Antecedent(np.arange(10,91,1),'detergent_quantity')

    wash_time = ctrl.Consequent(np.arange(0, 61, 1), 'wash_time')

    #membership functions
    degree_dirt.automf(3)
    detergent_quantity.automf(3)


    degree_dirt['Low'] = fuzz.trimf(degree_dirt.universe, [0,15,35])
    degree_dirt['Medium'] = fuzz.trimf(degree_dirt.universe, [25,45,65])
    degree_dirt['High'] = fuzz.trimf(degree_dirt.universe, [60,80,100])
    
    detergent_quantity['Little'] = fuzz.trimf(detergent_quantity.universe, [10,20,35])
    detergent_quantity['Few'] = fuzz.trimf(detergent_quantity.universe, [30,40,55])
    detergent_quantity['VeryMuch'] = fuzz.trimf(detergent_quantity.universe, [50,75,90])

    


    # Washing Time
    wash_time['very_short'] = fuzz.trimf(wash_time.universe, [0, 9, 15])
    wash_time['short'] = fuzz.trimf(wash_time.universe, [12, 16, 20])
    wash_time['medium'] = fuzz.trimf(wash_time.universe, [18, 24, 30])
    wash_time['long'] = fuzz.trimf(wash_time.universe, [25, 35, 45])
    wash_time['very_long'] = fuzz.trimf(wash_time.universe, [40, 50, 60])

    # Rules
    rule1 = ctrl.Rule(degree_dirt['High'] & detergent_quantity['Little'] , wash_time['very_long'])
    rule4 = ctrl.Rule(degree_dirt['High'] & detergent_quantity['Few'], wash_time['long'])
    rule7 = ctrl.Rule(degree_dirt['High'] & detergent_quantity['VeryMuch'], wash_time['medium'])


    rule2 = ctrl.Rule(degree_dirt['Medium'] & detergent_quantity['Little'], wash_time['long'])
    rule5 = ctrl.Rule(degree_dirt['Medium'] & detergent_quantity['Few'], wash_time['medium'])
    rule8 = ctrl.Rule(degree_dirt['Medium'] & detergent_quantity['VeryMuch'], wash_time['short'])
    
    rule6 = ctrl.Rule(degree_dirt['Low'] & detergent_quantity['Little'], wash_time['medium']) 
    rule3 = ctrl.Rule(degree_dirt['Low'] & detergent_quantity['Few'], wash_time['short'])    
    rule9 = ctrl.Rule(degree_dirt['Low'] & detergent_quantity['VeryMuch'], wash_time['very_short'])

    washing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
    washing = ctrl.ControlSystemSimulation(washing_ctrl)

    

if __name__ == '__main__':
    det_quantity = float(input("Detergent Quantity : "))
    deg_dirtiness = float(input("Degree Dirtiness :"))
    if det_quantity < 90 and det_quantity > 0 and deg_dirtiness < 100 and deg_dirtiness > 0:
        WashingMachine.washing.input['detergent_quantity'] = det_quantity
        WashingMachine.washing.input['degree_dirt'] = deg_dirtiness
        WashingMachine.washing.compute()          
        wash_time = WashingMachine.washing.output['wash_time']
        print(wash_time)
# Okan Çiftçi 151805041 Fuzzy Logic