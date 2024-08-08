# 18. Draw a scatterplot that shows the relationship between rollnos and marks of students (given below)in a class.
#rollnos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# marks = [22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]


from matplotlib import pyplot
rollnos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
marks = [22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]
fig,ax = pyplot.subplots(1,1)

ax.scatter(rollnos, marks)
ax.set_title("Scatter Plot")
ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
ax.set_yticks([25,50,75,100])
ax.set_xlabel('rollnos')
ax.set_ylabel('marks')
pyplot.show()
