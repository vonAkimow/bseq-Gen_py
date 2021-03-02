# -*- coding: utf-8 -*-

# 
import matplotlib.pyplot as plt

class CorellationCalc:
    def __init__(self):
        pass
    
    @staticmethod
    def calculate_pacf(sequence):
        try:
            length = len(sequence)
            if length < 3:
                raise ValueError
        except ValueError:
            return f'#ERROR:  {sequence} - too short sequence!\n'
        else:
            # Замена '0' на '-1' в исходной последовательности
            for index, element in enumerate(sequence):
                if element == 0:
                    sequence[index] = -1
            return sequence
        
        
        
'''
# Построение графика последовательности
plt.ylabel(f'b ({length})', fontsize=14, fontname='Times New Roman')
plt.xlabel('k', fontsize=14, fontname='Times New Roman')
plt.grid(True, color='k', linestyle='--', linewidth=0.5)
plt.title(f'B-Sequence {length}, shifts:{shifts}', 
          fontsize=14, fontname='Times New Roman')
plt.plot(range(0,length), bseq,'rH--', linewidth=2.0)
'''