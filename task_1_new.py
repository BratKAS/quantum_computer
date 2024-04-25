from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram


# Создаем трехкубитную квантовую схему
scheme3 = QuantumCircuit(3, 3)

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

scheme3.measure(2, 2)  # Измеряем состояние кубита и применяем результат в классическом бите

scheme3.draw(output='mpl', filename='scheme3')

print('\nscheme_3')
num_measurements = 1000
result = execute(scheme3, Aer.get_backend('qasm_simulator'), shots=num_measurements).result()
counts = result.get_counts(scheme3)
print(f"Number of measurements: {num_measurements}, Result: {counts}")
plot_histogram(counts, filename='hist_scheme_3')

# схема логического и (умножение)
scheme_and = QuantumCircuit(3, 3)
scheme_and.h(0)
scheme_and.h(1)

scheme_and.barrier()
# Применяем гейт Тофоли к первому и второму кубитам, результат записываем на третий кубит
scheme_and.ccx(0, 1, 2)

scheme_and.measure(2, 2)

# y =

scheme_and.draw(output='mpl', filename='scheme_and')

print('\nscheme_and')
num_measurements = 1000
result = execute(scheme_and, Aer.get_backend('qasm_simulator'), shots=num_measurements).result()
counts = result.get_counts(scheme_and)
print(f"Number of measurements: {num_measurements}, Result: {counts}")
plot_histogram(counts, filename='hist_scheme_and')

# схема логического или (сложения)
scheme_or = QuantumCircuit(3, 3)
scheme_or.h(0)
scheme_or.h(1)

scheme_or.barrier()
scheme_or.x(0)
scheme_or.x(1)
# Применяем гейт Тофоли к первому и второму кубитам, результат записываем на третий кубит
scheme_or.ccx(0, 1, 2)
scheme_or.x(2)

scheme_or.measure(2, 2)

scheme_or.draw(output='mpl', filename='scheme_or')

print('\nscheme_or')
num_measurements = 1000
result = execute(scheme_or, Aer.get_backend('qasm_simulator'), shots=num_measurements).result()
counts = result.get_counts(scheme_or)
print(f"Number of measurements: {num_measurements}, Result: {counts}")
plot_histogram(counts, filename='hist_scheme_or')
