# -*- coding: utf-8 -*-

# 
import matplotlib.pyplot as plt
# Класс инструментов для расчёта и построения графиков КФ
class CorellationCalc:
    def __init__(self):
        pass
    
    # Приватный метод циклического сдвига элементов последовательности
    def __cyclic_right_shift(sequence):
        temp_sequence_1 = sequence[:]
        cor_sequence = [1]
        
        for tau in range(1, len(sequence)):
            # Извлечение последнего элемента и вставка его в начало
            sequence.insert(0, sequence.pop())
            temp_sequence_2 = [x * y for x, y in zip(temp_sequence_1, sequence)]
            cor_sequence.append(round(sum(temp_sequence_2)/len(sequence), 1))
            
        return cor_sequence
    
    # Статический метод расчёта ПАКФ
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
            return CorellationCalc.__cyclic_right_shift(sequence)
        
    # Статический метод построения графика КФ    
    @staticmethod 
    def plot_corellation(sequence, title):
         length = len(sequence)
         plt.ylabel('R (k)', fontsize=14, fontname='Times New Roman')
         plt.xlabel('k', fontsize=14, fontname='Times New Roman')
         plt.grid(True, color='k', linestyle='--', linewidth=0.5)
         #plt.xticks(range(0, length, length % 10))
         plt.title(f'{title}', fontsize=14, fontname='Times New Roman')
         plt.plot(range(0,length), sequence,'r--', linewidth=1.0)
        
         
         
         
         
    
