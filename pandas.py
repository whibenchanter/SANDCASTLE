import pandas as pd

#데이콘 상~


#1. 대괄호를 이용한 슬라이싱, 'b'부터 'd', 2부터 5이전까지.(옳게 수정하라)
# value_b_to_d = series['b':'e']
# print(value_b_to_d)
# value_2_to_before_5 = series[2 : 5]
# print(value_2_to_before_5)


#2. 데이터 값이 30보다 크거나 같은 값들을 추출하여 2 30 3 40 4 50으로 출력. (옳게 수정하라)
# data = [10, 20, 30, 40, 50]
# series = pd.Series(data, name='MySeries')
# filtered_series = series.iloc[2:5] >=30
# filtered_series


#3. series의 값에서 rank 함수를 이용해 순위. (옳게 수정하라)
# series_rank = series.rank(dtype=int)
# series_rank

#3-1. dtype을 쓰는 경우 (데이터프레임 처음 생성시)
data = [1,2,3]
series = pd.Series(data, dtype='float64')


#4. lambda 썼을때와 안썼을때(lambda의 위대함)
def custom_function(x):
    if x>= 3:
        result = x + 2
    else:
        result = x + 4
    return result
result_series = series.apply(custom_function)
result_series

# =

result_series = series.apply(lambda x: x + 2 if x >= 3 else x + 4)
result_series


#5. 시리즈에서 홀수값을 찾아 제곱한 값을 구하고, 짝수값은 그대로 반환하는 함수를 작성,
#   그리고 apply 함수 사용하여 시리즈르르 result_series에 저장.(옳게 수정하라)
# data = [1, 2, 3, 4, 5, 6]
# series = pd.Series(data)

# def square_odd_or_return_even(x):
#     if x % 2 == 0:
#     else:
#     return x ** 2

# result_series = series.apply(square_odd_or_return_even)
# result_series

#6. 너무 중요해서 넣음. cut 함수를 이용해서 0초과 ~30이하는 Low, 30초과 60이하는 High로 값 변경, 결과는 result_series에 저장.
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
bins = [0, 30, 60]
labels = ['Low', 'High']
result_series = pd.cut(series, bins, labels=labels)
result_series

#1번부터 정답
value_b_to_d = series['b':'d'] #
print(value_b_to_d)

value_2_to_before_5 = series[2 : 5]
print(value_2_to_before_5)

#2답.
data = [10, 20, 30, 40, 50]
series = pd.Series(data, name='MySeries')
filtered_series = series.iloc[2:5] 
filtered_series >=30 #
filtered_series

#3답.
series_rank = series.rank().astype(int)
series_rank

#5답.
data = [1, 2, 3, 4, 5, 6]
series = pd.Series(data)

def square_odd_or_return_even(x):
    if x % 2 == 0:
        return x #
    else: 
        return x ** 2 #

result_series = series.apply(square_odd_or_return_even)
result_series




