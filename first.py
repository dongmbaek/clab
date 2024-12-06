import sys

def sum_of_numbers(n):
    return n * (n + 1) // 2  # 수학적 공식을 이용한 합 계산

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("사용법: python script.py <n>")
    else:
        try:
            n = int(sys.argv[1])
            if n < 1:
                print("n은 1 이상의 정수여야 합니다.")
            else:
                result = sum_of_numbers(n)
                print(f"1에서 {n}까지의 합은 {result}입니다.")
        except ValueError:
            print("유효한 정수를 입력하세요.")
