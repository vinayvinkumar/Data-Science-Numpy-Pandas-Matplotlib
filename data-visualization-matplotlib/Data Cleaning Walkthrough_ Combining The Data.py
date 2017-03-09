## 2. Condensing class size ##

class_size = data["class_size"]
class_size = class_size[class_size['GRADE '] == '09-12']
class_size = class_size[class_size['PROGRAM TYPE'] == 'GEN ED']
print(class_size.head())

## 3. Computing average class sizes ##

import numpy
class_size = class_size.groupby("DBN").agg(numpy.mean)
class_size.reset_index(inplace=True)
data["class_size"] = class_size
print(data["class_size"].head())

## 4. Condensing demographics ##

a = (data["demographics"]['schoolyear'] == 20112012)
data["demographics"] = data["demographics"][a]
print(data["demographics"].head())

## 5. Condensing graduation ##

data['graduation'] = data['graduation'][data['graduation']['Cohort'] == '2006']
data['graduation'] = data['graduation'][data['graduation']['Demographic'] == 'Total Cohort']
print(data['graduation'].head())

## 9. Performing the inner joins ##

combined = combined.merge(data['class_size'],on="DBN",how='inner')
combined = combined.merge(data['demographics'],on="DBN",how='inner')
combined = combined.merge(data['survey'],on="DBN",how='inner')
combined = combined.merge(data['hs_directory'],on="DBN",how='inner')
print(combined.head())
print(combined.shape)

## 10. Filling in missing values ##

combined = combined.fillna(combined.mean())
combined = combined.fillna(0)

print(combined.head(5))

## 11. Adding a school district column ##

def extrac(str):
    return str[0:2]

combined['school_dist'] = combined['DBN'].apply(extrac)
print(school_dist.head())
