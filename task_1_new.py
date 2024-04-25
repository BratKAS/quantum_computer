from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram


# 1
# Создаем трехкубитную квантовую схему
scheme3 = QuantumCircuit(3, 1)

# Подаём на вход векторы состояний 0, 1, 0
scheme3.x(1)  # Устанавливаем состояние |1⟩ на втором кубите
scheme3.barrier()

# Применяем гейт Адамара к первому кубиту
scheme3.h(0)
# Применяем гейт Адамара ко второму кубиту
scheme3.h(1)
scheme3.ccx(0, 1, 2)  # Применяем гейт Тофоли к схеме scheme3

# Применяем гейт Адамара к первому кубиту
scheme3.h(0)
# Применяем гейт Адамара ко второму кубиту
scheme3.h(1)

scheme3.measure(2, 0)  # Измеряем состояние кубита и применяем результат в классическом бите

scheme3.draw(output='mpl', filename='scheme3')

print('\nscheme_3')
num_measurements = 1000
result = execute(scheme3, Aer.get_backend('qasm_simulator'), shots=num_measurements).result()
counts = result.get_counts(scheme3)
print(f"Number of measurements: {num_measurements}, Result: {counts}")
plot_histogram(counts, filename='hist_scheme_3')

# 2
# схема логического и (умножение)
scheme_and = QuantumCircuit(3, 1)
scheme_and.h(0)
scheme_and.h(1)

scheme_and.barrier()
# Применяем гейт Тофоли к первому и второму кубитам, результат записываем на третий кубит
scheme_and.ccx(0, 1, 2)

scheme_and.measure(2, 0)

scheme_and.draw(output='mpl', filename='scheme_and')

print('\nscheme_and')
num_measurements = 1000
result = execute(scheme_and, Aer.get_backend('qasm_simulator'), shots=num_measurements).result()
counts = result.get_counts(scheme_and)
print(f"Number of measurements: {num_measurements}, Result: {counts}")
plot_histogram(counts, filename='hist_scheme_and')

# схема логического или (сложения)
scheme_or = QuantumCircuit(3, 1)
scheme_or.h(0)
scheme_or.h(1)

scheme_or.barrier()
scheme_or.x(0)
scheme_or.x(1)
# Применяем гейт Тофоли к первому и второму кубитам, результат записываем на третий кубит
scheme_or.ccx(0, 1, 2)
scheme_or.x(2)

scheme_or.measure(2, 0)

scheme_or.draw(output='mpl', filename='scheme_or')

print('\nscheme_or')
num_measurements = 1000
result = execute(scheme_or, Aer.get_backend('qasm_simulator'), shots=num_measurements).result()
counts = result.get_counts(scheme_or)
print(f"Number of measurements: {num_measurements}, Result: {counts}")
plot_histogram(counts, filename='hist_scheme_or')

# 3
# y = x1 + x2
scheme_xor = QuantumCircuit(3, 1)

scheme_xor.h(0)
scheme_xor.h(1)

scheme_or.barrier()

# Применяем операцию XOR между первым и вторым кубитами
scheme_xor.cx(0, 2)  # Применяем CNOT гейт с первого кубита на третий
scheme_xor.cx(1, 2)  # Применяем CNOT гейт с второго кубита на третий

scheme_xor.measure(2, 0)

scheme_xor.draw(output='mpl', filename='scheme_xor')

print('\nscheme_xor')
num_measurements = 1000
result = execute(scheme_xor, Aer.get_backend('qasm_simulator'), shots=num_measurements).result()
counts = result.get_counts(scheme_xor)
print(f"Number of measurements: {num_measurements}, Result: {counts}")
plot_histogram(counts, filename='hist_scheme_xor')


