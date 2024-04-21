from qiskit import QuantumCircuit, execute, Aer

# 1
scheme3 = QuantumCircuit(3, 3)  # Создаем квантовую схему с 3 кубитами
scheme3.h(0)
scheme3.h(1)
scheme3.ccx(0, 1, 2)  # Добавляем гейт Тоффоли

scheme3.draw(output='mpl', filename='CXEMA_3')