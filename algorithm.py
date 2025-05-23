import random

<<<<<<< HEAD
def fitness(board):
    """
    محاسبه تعداد برخوردهای بین وزیرها در یک آرایش خاص.
    هرچه برخورد کمتر، امتیاز بیشتر.
    """
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j]:  # هم‌ستونی
                conflicts += 1
            if abs(board[i] - board[j]) == abs(i - j):  # روی یک قطر
                conflicts += 1
    return 28 - conflicts  # امتیاز نهایی: حداکثر 28 بدون برخورد

def selection(population):
    """
    انتخاب دو فرد برتر بر اساس بیشترین fitness
    """
    sorted_population = sorted(population, key=lambda x: fitness(x), reverse=True)
    return sorted_population[0], sorted_population[1]

# مثال برای تست
if name == "__main__":
    sample_population = [
        [0, 1, 2, 3, 4, 5, 6, 7],
        [0, 4, 7, 5, 2, 6, 1, 3],
        [3, 1, 4, 2, 0, 6, 7, 5]
    ]
    fittest = selection(sample_population)
    print("Best two individuals:", fittest)
=======
def crossover(parent1, parent2):
    """
    ترکیب دو والد برای تولید یک فرزند جدید.
    ژن‌های والد اول تا نقطه‌ای مشخص برداشته می‌شوند، بقیه از والد دوم.
    """
    point = random.randint(1, len(parent1) - 2)
    child = parent1[:point] + parent2[point:]
    return child

def mutation(board, mutation_rate=0.1):
    """
    تغییر تصادفی جای یک وزیر در صفحه.
    با احتمال مشخص mutation انجام می‌شود.
    """
    if random.random() < mutation_rate:
        row = random.randint(0, len(board) - 1)
        new_col = random.randint(0, len(board) - 1)
        board[row] = new_col
    return board

# مثال برای تست
if name == "__main__":
    p1 = [0, 4, 7, 5, 2, 6, 1, 3]
    p2 = [3, 1, 4, 2, 0, 6, 7, 5]
    child = crossover(p1, p2)
    mutated = mutation(child)
    print("Child:", child)
    print("After Mutation:", mutated)
>>>>>>> main
