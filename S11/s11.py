import arcpy

shp = arcpy.GetParameterAsText(0)
zipshp = arcpy.GetParameterAsText(1)
arcpy.env.workspace = arcpy.GetParameterAsText(2)
distance = arcpy.GetParameterAsText(3)
fieldsname = arcpy.GetParameterAsText(4)
fieldvalue = arcpy.GetParameterAsText(5)
arcpy.env.overwriteOutput = True

# make layers, select attributes
arcpy.MakeFeatureLayer_management(shp, 'facilitiesss')
arcpy.MakeFeatureLayer_management(zipshp, 'zip')
arcpy.AddMessage('Layer was created')
arcpy.SelectLayerByLocation_management('facilitiesss', 'WITHIN_A_DISTANCE', 'zip', distance + ' meters',
                                       'NEW_SELECTION')
arcpy.SelectLayerByAttribute_management('facilitiesss', 'SUBSET_SELECTION', "{} = '{}'".format(fieldsname, fieldvalue))
arcpy.AddMessage(
    "Selecting objects within '{}' meters with '{}' values in the field '{}'".format(distance, fieldvalue, fieldsname))

# create a new feature class similar to facilities.shp in your directory
newshp = "facilities_Distance_{}.shp".format(distance)
arcpy.CreateFeatureclass_management(arcpy.env.workspace, newshp, "POINT", spatial_reference="facilitiesss")

# create new fields
insertfields = ['ADDRESS', 'NAME', 'FACILITY', 'XY']
for f in insertfields:
    arcpy.AddField_management(newshp, f, "TEXT")
searchfields = ['ADDRESS', 'NAME', 'FACILITY', 'SHAPE@XY']
with arcpy.da.InsertCursor(newshp, searchfields) as cursorI, arcpy.da.SearchCursor("facilitiesss",
                                                                                   searchfields) as cursorS:
    for row in cursorS:
        cursorI.insertRow(row)
arcpy.AddMessage("Created file. Created fields and records: {}".format(newshp))

# in facilities_Distance_3000.shp created new field is COLLEGE_NAME
fieldnew = fieldvalue[:6] + 'NAME'
arcpy.AddField_management(newshp, fieldnew, "DOUBLE")

fac_idval = []
with arcpy.da.SearchCursor("facilitiesss", 'FAC_ID') as cursorSS:
    for row in cursorSS:
        fac_idval.append(row)

i = 0
with arcpy.da.UpdateCursor(newshp, fieldnew) as cursorU:
    for row in cursorU:
        row = fac_idval[i]
        cursorU.updateRow(row)
        i += 1
arcpy.AddMessage('Created field {} and updated in a file {}'.format(fieldnew, newshp))
