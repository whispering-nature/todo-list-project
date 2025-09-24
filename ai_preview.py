import numpy as np
python_list=[1,2,3,4,5]
numpy_array=np.array(python_list)
print(f"这是一个普通的Python列表: {python_list}")
print(f"这是一个NumPy数组: {numpy_array}")
print(f"NumPy数组的类型是: {type(numpy_array)}")
print("\n--- 体验矢量化 ---")
doubled_array = numpy_array * 2
print(f"NumPy数组乘以2的结果: {doubled_array}")
doubled_list = []
for item in python_list:
    doubled_list.append(item * 2)
print(f"Python列表乘以2的结果: {doubled_list}")
print("\n--- 体验强大的内置函数 ---")
print(f"数组中所有元素的和: {np.sum(numpy_array)}")
print(f"数组中所有元素的平均值: {np.mean(numpy_array)}")