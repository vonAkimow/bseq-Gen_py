# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:59:20 2021

@author: ak1mo
"""
from b_sequences import BSeq
from corellation import CorellationCalc as cor




length = 17
shifts = [1]
shifters = len(shifts)
# Создание экземпляра класса B-последовательностей
sequence_1 = BSeq(length, shifts, shifters)

# Создание ПСП
bseq = sequence_1.create_b_sequence()
balance = sequence_1.calculate_balance()

print(bseq)
print(f'Сбалансированность 1/0: {balance}')
print(cor.calculate_pacf(bseq[:]))
print(bseq)

