#!/usr/bin/env python
# coding: utf-8

# In[2]:


from IPython.display import YouTubeVideo
YouTubeVideo('lyDLAutA88s', width=800, height=300)


# In[ ]:


# 1. Посмотрите видео Дэвида Бизли про всроенные инструменты Python
# 2. Попробуйте используя встроенные инструменты Python проанализировать таблицу из файла "Vacancy.csv"
# 3. Попробуйте ответить на вопросы:
# Сколько вакансий, которые вам нравятся?
# Насколько свежие эти вакансии?
# Сколько вакансий с позициями на которых вы работаете?
# Сколько вакансий для аналатика данных?
# Сколько вакансий для аналитика данных с использованием Python?

# В задании важно не использовать pandas и numpy, а встроенные инструменты python
# Counter, CSV, defaultdict, sorted


# In[1]:


import csv


# In[4]:


import sys


# In[5]:


csv.field_size_limit(sys.maxsize)


# In[6]:


vacs = list(csv.DictReader(open('Vacancy.csv')))


# In[ ]:





# In[4]:


vacs[10]


# In[14]:


import csv
csv.field_size_limit(100000000)
with open('vacancy.csv', 'rt', encoding='utf-8') as file:
    vacs = list(csv.DictReader(file))
    print(*vacs[0].items(), sep='\n')


# In[ ]:





# In[49]:


# Сколько вакансий, которые вам нравятся?
vacs_i_like2 = [(row['id'], row['vactitle'], row['vacdescription']) for row in vacs if 'data analyst' in row['vactitle'].lower() and 'python' in row['vacdescription'].lower() and 'sql' in row['vacdescription'].lower()]
print(len(vacs_i_like2))
for vac in vacs_i_like2:
    print('-------', vac[0], vac[1], *vac[2].split(';'), sep='\n')


# In[60]:


# Насколько свежие эти вакансии?
freshness = [(row['id'], row['created_at']) for row in vacs             if 'data analyst' in row['vactitle'].lower()              and 'python' in row['vacdescription'].lower()             and 'sql' in row['vacdescription'].lower()]

print(sorted(filter(lambda str: '2021' in str[1], freshness)))

for vac in freshness:
    if '2021' in vac[1]:
        print(*vac, sep='\n')


# In[62]:


# Сколько вакансий с позициями на которых вы работаете?
my_vacs = [(row['id'], row['vactitle'], row['vacdescription']) for row in vacs if 'аудитор' in row['vactitle'].lower()]
print(len(my_vacs))
for vac in my_vacs:
    print('-------', vac[0], vac[1], *vac[2].split(';'), sep='\n')


# In[72]:


# Сколько вакансий для аналатика данных?
vacs_analyst = [row['id'] for row in vacs                if 'data analyst' in row['vactitle'].lower()]
print('Сколько вакансий для аналатика данных?', len(vacs_analyst), '\n')

# Сколько вакансий для аналитика данных с использованием Python?
vacs_analyst_python = [row['id'] for row in vacs                if 'data analyst' in row['vactitle'].lower()                and 'python' in row['vacdescription'].lower()]
print('Сколько вакансий для аналитика данных с использованием Python?', len(vacs_analyst_python))


# In[ ]:




