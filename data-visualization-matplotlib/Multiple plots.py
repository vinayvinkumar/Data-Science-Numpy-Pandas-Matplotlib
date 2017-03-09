## 2. Matplotlib Classes ##

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

## 4. Adding Data ##

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])

plt.show()

## 5. Formatting And Spacing ##

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

## 6. Comparing Across More Years ##

fig = plt.figure(figsize=(12,12))

for i in range(5):
    ax = fig.add_subplot(5,1,i+1)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    ax.plot(subset['DATE'], subset['VALUE'])

plt.show()

## 7. Overlaying Line Charts ##

unrate['MONTH'] = unrate['DATE'].dt.month
plt.figure(figsize=(6,3))
plt.plot(unrate[0:12]['MONTH'],unrate[0:12]['VALUE'],c="red")
plt.plot(unrate[12:24]['MONTH'],unrate[12:24]['VALUE'],c="blue")
plt.show()

## 8. Adding More Lines ##

plt.figure(figsize=(10,6))
plt.plot(unrate[0:12]['MONTH'],unrate[0:12]['VALUE'],C="red")
plt.plot(unrate[12:24]['MONTH'],unrate[12:24]['VALUE'],C="blue")
plt.plot(unrate[24:36]['MONTH'],unrate[24:36]['VALUE'],C="green")
plt.plot(unrate[36:48]['MONTH'],unrate[36:48]['VALUE'],C="orange")
plt.plot(unrate[48:60]['MONTH'],unrate[48:60]['VALUE'],C="black")
plt.show()

## 9. Adding A Legend ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc="upper left")
plt.show()

## 10. Final Tweaks ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent") 

plt.show()