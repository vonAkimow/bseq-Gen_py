# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:41:29 2021
@author: ak1mo
"""


# Класс Pseudo random sequences
class BSeq:
    # Приватная переменная
    __min_prime_value = 2

    # Конструктор класса
    def __init__(self, number=17, shift_array=[0], shift_registers=1):
        self.number = number  # Простое число
        self.shift_array = shift_array  # Сдвиг
        self.shift_registers = shift_registers  # Количество сдвиговых регистров

    # Метод создания B-последовательности
    def create_b_sequence(self):
        try:
            if len(self.shift_array) != self.shift_registers:
                raise ValueError
            if (self.shift_registers < 1) or (self.shift_registers > 4):
                raise ValueError
        except ValueError:
            return f'#ERROR:  {self.shift_registers} - a wrong number of shift registers or shifts!\n'
        else:
            # Создание последовательности простых чисел
            return self.__sum_mod_2(self.__create_prime_sequence())

    # Метод подсчёта сбалансированности последовательности
    def calculate_balance(self):
        sequence = self.create_b_sequence()     
        return sequence.count(1), len(sequence) - sequence.count(1)

    # Приватный метод проверки числа на простоту
    def __is_prime(prime_number):

        if prime_number == 2:
            return True

        if prime_number > 1:
            for value in range(BSeq.__min_prime_value, prime_number):
                if (prime_number % value) == 0:
                    return False
            return True
        else:
            return False

    # Приватный метод сложения последовательностей
    def __sum_mod_2(self, sequence):
        # Копирование последовательности
        base_sequence = sequence[:]
       # print(f'Prime sequence:\n {base_sequence}')
        for counter in range(0, self.shift_registers):
            # Суммирование по модулю 2 (Xor)
            temp_sequence = [x ^ y for x, y in zip(base_sequence, self.__shift_sequence(sequence[:], counter))]
            base_sequence = temp_sequence[:]
            #print(f'Base_sequence_{counter}:\n {base_sequence}')
        return base_sequence

    # Приватный метод: сдвиг последовательности на shifts элементов
    def __shift_sequence(self, sequence, index):
        try:
            shift = self.shift_array[index]

            if (shift > self.number) or (shift < 0):
                raise ValueError
        except ValueError:
            return f'#ERROR:  {shift} - invalid shift value!\n'
        else:
            for shift in range(0, shift):
                del sequence[len(sequence) - 1]
                sequence.insert(0, 0)
            return sequence

    # Приватный метод создания проследовательности простых чисел
    def __create_prime_sequence(self):
        try:
            if not BSeq.__is_prime(self.number):
                raise ValueError
        except ValueError:
            return f'#ERROR:  {self.number} - does not prime number!\n'
        else:
            tmp_seq = [1 if BSeq.__is_prime(value) else 0
                       for value in range(1, self.number + 1)]
            return tmp_seq







