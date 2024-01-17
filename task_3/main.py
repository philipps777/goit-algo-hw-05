import timeit

from kmp import kmp_search
from bm import boyer_moore_search
from rk import rabin_karp_search


def work_time(algorithm, text, pattern):

    start_time = timeit.default_timer()
    algorithm(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":

    text1 = read_file(
        r"E:\GOIT\Basic Algorithms and Data Structures\HW_5\goit-algo-hw-05\task_3\article_1.txt")
    text2 = read_file(
        r"E:\GOIT\Basic Algorithms and Data Structures\HW_5\goit-algo-hw-05\task_3\article_2.txt")

    present_pattern_article_1 = "Експоненціальний пошук"
    present_pattern_article_2 = "Література "
    fake_pattern_article_1 = "Exponential searc"
    fake_pattern_article_2 = "literature"

    kmp_present_time_article_1 = work_time(
        kmp_search, text1, present_pattern_article_1)
    kmp_present_time_article_2 = work_time(
        kmp_search, text2, present_pattern_article_2)
    kmp_fake_time_article_1 = work_time(
        kmp_search, text1, fake_pattern_article_1)
    kmp_fake_time_article_2 = work_time(
        kmp_search, text2, fake_pattern_article_2)

    bm_present_time_article_1 = work_time(
        boyer_moore_search, text1, present_pattern_article_1)
    bm_present_time_article_2 = work_time(
        boyer_moore_search, text1, present_pattern_article_2)
    bm_fake_time_article_1 = work_time(
        boyer_moore_search, text2, fake_pattern_article_1)
    bm_fake_time_article_2 = work_time(
        boyer_moore_search, text2, fake_pattern_article_2)

    rk_present_time_article_1 = work_time(
        rabin_karp_search, text1, present_pattern_article_1)
    rk_present_time_article_2 = work_time(
        rabin_karp_search, text1, present_pattern_article_2)
    rk_fake_time_article_1 = work_time(
        rabin_karp_search, text2, fake_pattern_article_1)
    rk_fake_time_article_2 = work_time(
        rabin_karp_search, text2, fake_pattern_article_2)

    print(
        f"Кнута-Морріса-Прата для існуючого підрядка в статті 1: {kmp_present_time_article_1} секунд")
    print(
        f"Кнута-Морріса-Прата для існуючого підрядка в статті 2: {kmp_present_time_article_2} секунд")
    print(
        f"Кнута-Морріса-Прата для вигаданого підрядка в статті 1: {kmp_fake_time_article_1} секунд")
    print(
        f"Кнута-Морріса-Прата для вигаданого підрядка в статті 2: {kmp_fake_time_article_2} секунд")

    print(
        f"Боєра-Мура для існуючого підрядка в статті 1: {bm_present_time_article_1} секунд")
    print(
        f"Боєра-Мура для існуючого підрядка в статті 2: {bm_present_time_article_2} секунд")
    print(
        f"Боєра-Мура для вигаданого підрядка в статті 1: {bm_fake_time_article_1} секунд")
    print(
        f"Боєра-Мура для вигаданого підрядка в статті 2: {bm_fake_time_article_2} секунд")

    print(
        f"Рабіна-Карпа для існуючого підрядка в статті 1: {rk_present_time_article_1} секунд")
    print(
        f"Рабіна-Карпа для існуючого підрядка в статті 2: {rk_present_time_article_2} секунд")
    print(
        f"Рабіна-Карпа для вигаданого підрядка в статті 1: {rk_fake_time_article_1} секунд")
    print(
        f"Рабіна-Карпа для вигаданого підрядка в статті 2: {rk_fake_time_article_2} секунд")

    print('')
    print(f"{'| Algorithms': <22} | {'Present pattern': <20} | {'Fake pattern': <20}")
    print(f"|{'-'*21} | {'-'*19}  | {'-'*19}")

    print(" Стаття 1")
    print(f"{'| Кнута-Морріса-Пратта': <20} | {kmp_present_time_article_1:<20.7f} | {kmp_fake_time_article_1:<20.7f}")
    print(f"{'| Боєра-Мура': <22} | {bm_present_time_article_1:<20.7f} | {bm_fake_time_article_1:<20.7f}")
    print(f"{'| Рабіна-Карпа': <22} | {rk_present_time_article_1:<20.7f} | {rk_fake_time_article_1:<20.7f}")

    print(" Стаття 2")
    print(f"{'| Кнута-Морріса-Пратта': <20} | {kmp_present_time_article_2:<20.7f} | {kmp_fake_time_article_2:<20.7f}")
    print(f"{'| Боєра-Мура': <22} | {bm_present_time_article_2:<20.7f} | {bm_fake_time_article_2:<20.7f}")
    print(f"{'| Рабіна-Карпа': <22} | {rk_present_time_article_2:<20.7f} | {rk_fake_time_article_2:<20.7f}")
