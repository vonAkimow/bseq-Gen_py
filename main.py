# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:59:20 2021

@author: ak1mo
"""
from b_sequences import BSeq as bprs
from corellation import CorellationCalc as cor

# Для генерации М-последовательностей
from scipy.signal import max_len_seq


# Параметры последовтельности
length = 17
shifts = [1, 2]
shifters = len(shifts)

# Создание экземпляра класса B-последовательностей
b_obj = bprs(length, shifts, shifters)

# Создание ПСП
bseq = b_obj.create_b_sequence()
mseq = list(max_len_seq(4)[0])


# Расчёт сбалансированности и ПАКФ
balance = b_obj.calculate_balance()
pacf = cor.calculate_pacf(bseq[:])

print(list(mseq))
print(bseq)
print(f'Сбалансированность 1/0: {balance}')
print(f'Max = {max(pacf[1:])}, Min = {min(pacf)}.\n')
cor.plot_corellation(pacf, f'ПАКФ B-последовательности_{length}, {shifts}')

