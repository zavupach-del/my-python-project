def count_steps(max_steps: int) -> int:
    steps_done = 0

    for i in range(1, max_steps + 1):
        steps_done += 1

        if i % 5 == 0:
            break
    
    return steps_done

print(count_steps(3))
print(count_steps(5))
print(count_steps(10))