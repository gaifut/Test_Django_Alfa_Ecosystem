def repetitive_n_str(n):
    final_answer = ''
    for i in range(n):
        final_answer += (str(i)*i)
    return final_answer
