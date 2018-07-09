from sklearn import tree

# Learn the correct foreground color based on a 
# background color
# --------------

# features: background ( RGB colors / hexadecimals)
x = [ 
  ['330033'], ['3a9325'], ['2a49be'], ['347bd2'], ['72a387'], ['f7ff6f'], 
  ['f8f9f8'], ['ffffff'], ['ebed35'], ['f24421'], ['edb336'], ['df67df']
]

# hexadecimal converter
def hex2dec(hexval):
  if type(hexval) != list:
    return [int(hexval, 16)]
  else:
    for x in hexval:
      return [int(hexval[0], 16)]

# convert the background values into decimal format
x = list(map(hex2dec, x))

# labels: foreground color to be used ( white / black )
y = ['White', 'White', 'White', 'White', 'White', 'White', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black']

# using the decision tree classifier
clf = tree.DecisionTreeClassifier()

clf = clf.fit(x, y)

# given background
bg = '000'

# make our prediction
prediction = clf.predict([ hex2dec(bg) ])

# show the results
print '%s text would appear more legible on a background with a #%s color' %(prediction[0], bg)
