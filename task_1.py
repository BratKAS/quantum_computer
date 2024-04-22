from qiskit import QuantumCircuit, execute, Aer
from qiskit.quantum_info import Statevector

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

scheme3.draw(output='mpl', filename='CXEMA_3')

print('\nscheme_3')
for num_measurements in [10000]:
    result = execute(scheme3, Aer.get_backend('qasm_simulator'), shots=num_measurements).result()
    counts = result.get_counts(scheme3)
    print(f"Number of measurements: {num_measurements}, Result: {counts}")

num_measurements = 100
combinations = ([0, 0], [0, 1], [1, 0], [1, 1])
# Создаем трехкубитную квантовую схему для функции y = x1 and x2

for comb in combinations:

    scheme_or = QuantumCircuit(3, 3)
    initial_state = ''
    for i in range(len(comb)):
        if comb[i] == 0:
            initial_state += '0'
        else:
            scheme_or.x(i)
            initial_state += '1'

    scheme_or.barrier()

    # Применяем гейт Тофоли к первому и второму кубитам, результат записываем на третий кубит
    scheme_or.ccx(0, 1, 2)

    # Измеряем состояние кубита и применяем результат в классическом бите
    scheme_or.measure(2, 2)

    scheme_or.draw(output='mpl', filename='CXEMA_and_' + initial_state)

    result = execute(scheme_or, Aer.get_backend('qasm_simulator'), shots=num_measurements).result()
    counts = result.get_counts(scheme_or)
    print(f"AND: Initial State: {initial_state}, Result: {counts}")

# Создаем трехкубитную квантовую схему для функции y = x1 or x2
for comb in combinations:

    scheme_or = QuantumCircuit(3, 3)
    initial_state = ''
    for i in range(len(comb)):
        if comb[i] == 0:
            initial_state += '0'
        else:
            scheme_or.x(i)
            initial_state += '1'

    scheme_or.barrier()
    scheme_or.x(0)
    scheme_or.x(1)
    scheme_or.x(2)

    # Применяем гейт Тофоли к первому и второму кубитам, результат записываем на третий кубит
    scheme_or.ccx(0, 1, 2)

    # Измеряем состояние кубита и применяем результат в классическом бите
    scheme_or.measure(2, 2)

    scheme_or.draw(output='mpl', filename='CXEMA_or_' + initial_state)

    result = execute(scheme_or, Aer.get_backend('qasm_simulator'), shots=num_measurements).result()
    counts = result.get_counts(scheme_or)
    print(f"OR: Initial State: {initial_state}, Result: {counts}")
