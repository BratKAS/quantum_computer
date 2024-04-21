from numpy import pi
from qiskit import QuantumCircuit, execute, Aer
import math


def qft_rotations(circuit, n):
    if n == 0:
        return circuit
    n -= 1
    circuit.h(n)
    for qubit in range(n):
        circuit.cp(pi/2**(n-qubit), qubit, n)
    qft_rotations(circuit, n)


# SWAP-гейты на выходе
def swap_registers(circuit, n): 
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1) 
    return circuit


# Преобразование Фурье
def qft(circuit, n): 
    qft_rotations(circuit, n) 
    swap_registers(circuit, n) 
    return circuit


def set_x_gate(circuit, nums):
    for n in nums:
        circuit.x(n)


# Обратное преобразование
def qft_reverse(circuit, n):
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)
    for j in range(n):
        for m in range(j):
            circuit.cp(-math.pi/float(2**(j-m)), m, j)
        circuit.h(j)
    circuit.name = "QFT†"
    return circuit  # Измерение


def measure_exit(circuit, n):
    for k in range(n):
        circuit.measure(k, k)
    return circuit


N = 1000  # кол-во измерений
# Схема для 3-х кубитов
combinations = ([0, 1, 2], [0, 1], [0, 2], [1, 2], [0], [1], [2], [])

# Прямое квантовое преобразование Фурье (QFT) для всех возможных начальных состояний
for comb in combinations:
    qc = QuantumCircuit(3, 3)
    set_x_gate(qc, comb)
    qc.barrier()
    qft(qc, 3)
    qc.barrier()
    measure_exit(qc, 3)

    name = ''
    for i in range(3):
        if i in comb:
            name += '1'
        else:
            name += '0'
    qc.draw(output='mpl', filename='QFT_' + name)

    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=N).result()
    counts = result.get_counts(qc)
    print(f"QFT: Состояние на входе: {name}, Кол-во измерений: {N}, Результат: {counts}")


# Обратное квантовое преобразование Фурье (QFT†) для всех возможных начальных состояний
for comb in combinations:
    qc = QuantumCircuit(3, 3)
    set_x_gate(qc, comb)
    qc.barrier()
    qft_reverse(qc, 3)
    qc.barrier()
    measure_exit(qc, 3)

    name = ''
    for i in range(3):
        if i in comb:
            name += '1'
        else:
            name += '0'
    qc.draw(output='mpl', filename='QFT†_' + name)

    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=N).result()
    counts = result.get_counts(qc)
    print(f"QFT†: Состояние на входе: {name}, Кол-во измерений: {N}, Результат: {counts}")


# Прямое и обратное квантовое преобразование Фурье (QFT-QFT†) для всех возможных начальных состояний
for comb in combinations:
    qc = QuantumCircuit(3, 3)
    set_x_gate(qc, comb)
    qc.barrier()
    qft(qc, 3)
    qc.barrier()
    qft_reverse(qc, 3)
    qc.barrier()
    measure_exit(qc, 3)

    name = ''
    for i in range(3):
        if i in comb:
            name += '1'
        else:
            name += '0'
    qc.draw(output='mpl', filename='QFT-QFT†' + name)

    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=N).result()
    counts = result.get_counts(qc)
    print(f"QFT-QFT†: Состояние на входе: {name}, Кол-во измерений: {N}, Результат: {counts}")