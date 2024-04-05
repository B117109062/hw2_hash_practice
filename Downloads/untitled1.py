# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_1toTg-ENsb8ooXZ3Gxm6P7RZIl0I8Fh
"""

file_path="hw2_data.txt"
def count_unique_words(file_path):
  unique_words = set()
  with open(file_path,'r',encoding='utf-8')as file:
    for line in file:
      words=line.split()
      for word in words:
        if word.isalpha():
         unique_words.add(word.lower())
  return len(unique_words)
result=count_unique_words(file_path)
print("不:",result)

file_path="hw2_data.txt"
def count_words(file_path):
  word_counts={}
  with open(file_path,'r',encoding='utf-8')as file:
    for line in file:
      words=line.lower().split()
      for word in words:
        if word.isalpha():
          if word in word_counts:
            word_counts[word]+=1
          else:
            word_counts[word]=1
  return word_counts
word_counts=count_words(file_path)
print("無:")
for word,count in word_counts.items():
  print(f"{word}:{count}")