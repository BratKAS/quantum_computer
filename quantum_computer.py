from qiskit import QuantumCircuit, execute, Aer

# 1
scheme_1_1 = QuantumCircuit(2, 2)  # Создаем квантовую схему с 2 кубитами
scheme_1_1.x(1)  # Применяем вентиль X для установки состояния |1) на втором кубите
scheme_1_1.measure([0, 1], [0, 1])  # Измеряем состояние кубитов и применяем результат в классических битах
scheme_1_1.draw(output='mpl', filename='CXEMA_1_1')

print('\nscheme_1_1')
for num_measurements in [1000]:
    result = execute(scheme_1_1, Aer.get_backend('qasm_simulator'), shots=num_measurements).result()
    counts = result.get_counts(scheme_1_1)
    print(f"Number of measurements: {num_measurements}, Result: {counts}")

# 2
scheme_1_2 = QuantumCircuit(1, 1)  # Создаем квантовую схему с 1 кубитом
scheme_1_2.h(0)  # Применяем вентиль H для установки состояния 1/sqrt(2) * (0, 1) на кубите
scheme_1_2.measure(0, 0)  # Измеряем состояние кубита и применяем результат в классическом бите
scheme_1_2.draw(output='mpl', filename='CXEMA_1_2')

print('\nscheme_1_2')
for num_measurements in [1, 2, 8, 1024, 10000]:
    result = execute(scheme_1_2, Aer.get_backend('qasm_simulator'), shots=num_measurements).result()
    counts = result.get_counts(scheme_1_2)
    print(f"Number of measurements: {num_measurements}, Result: {counts}")

# 3
scheme_1_3 = QuantumCircuit(2, 2)  # Создаем квантовую схему с 2 кубитами
scheme_1_3.x(1)  # Применяем вентиль X для установки состояния |1) на втором кубите
scheme_1_3.h(0)  # Применяем вентиль h для первого кубита
scheme_1_3.cx(0, 1)
scheme_1_3.measure([0, 1], [0, 1])  # Измеряем состояние кубитов и применяем результат в классических битах
scheme_1_3.draw(output='mpl', filename='CXEMA_1_3')

print('\nscheme_1_3')
for num_measurements in [1000]:
    result = execute(scheme_1_3, Aer.get_backend('qasm_simulator'), shots=num_measurements).result()
    counts = result.get_counts(scheme_1_3)
    print(f"Number of measurements: {num_measurements}, Result: {counts}")
