word = input("please enter the word")

# word1 = input("please enter the word")
vowels = {'a', 'e', 'i', 'o', 'u'}
result = {}
# s=word1.split()
# result = {'a': 100, 'e': 23, 'i': 67, 'o': 2200, 'u': 34}
#
# k = result.get(100) #"""key recovery using get from dictionary"""
# print(k)
# ********************************
# for c in word:
#     if c in vowels:
#         # result.values(c)
#         result[c] = result.get(c, 0) + 1  # assign a value in the result[c] variable. means result[key]
#         print(sorted(result))
# for k, v in sorted(result.items()):
#     print(k, "is times", v)
# #****************************************
print(word[::-1])
'''reverse oder'''
i = len(word) - 1
print(i)

r = ''
k = []
while i >= 0:
    r = r + word[i]
    # k.append(s[i])
    i = i - 1
print("before reverse :", word)
print(r)
# r=' '.join(k)
print(r)
# print("before reverse : ",word1)
# print(k)
# ss=' '.join(k)
# print(ss)
