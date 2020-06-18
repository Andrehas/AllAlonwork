import arcpy
arcpy.env.overwriteOutput = True

inputFeatureclass = arcpy.GetParameterAsText(0)           # rec_sites.shp
fileheight = arcpy.GetParameterAsText(1)
newFiles = arcpy.GetParameterAsText(2)  # resultFile = "#"
newFields = arcpy.GetParameterAsText(3)   # newFields = '#'

if newFields == '#' or not newFields:
    newFields = 'HEIGHT'

# Changes occured in the input or a new file is created the user decides
if newFiles == "#" or not newFiles:
    newFiles = inputFeatureclass
    arcpy.AddMessage("Changes occured in the input file")
else:
    arcpy.CopyFeatures_management(inputFeatureclass, newFiles)
    arcpy.AddMessage("A new file has been created with changes")

# check coordinate systems for coincidence
if arcpy.Describe(newFiles).spatialReference.name == arcpy.Describe(fileheight).spatialReference.name:
    arcpy.AddMessage("Coordinate systems coincide")
else:
    projectnion = arcpy.Describe(fileheight).spatialReference.name
    arcpy.Project_management(newFiles, newFiles, projectnion)
    arcpy.AddMessage("The coordinate systems did not match. Reprojected")

# determine the value of heights in the specified coordinates
height = []
with arcpy.da.SearchCursornewFiles, 'SHAPE@XY') as cursor:
    for row in cursor:
        evel = arcpy.GetCellValue_management(fileheight, str(row[0][0])+' '+str(row[0][1]))
        height.append(evel.getOutput(0))
arcpy.AddMessage("The values of heights by coordinates are determined")

# Create a new Field
arcpy.AddField_management(newFiles, newFields, "SHORT")
with arcpy.da.UpdateCursor(newFiles, newFields) as cursor:
    i = 0
    for row in cursor:
        row[0] = height[i]
        cursor.updateRow(row)
        i += 1
arcpy.AddMessage("Created {} field and height data is recorded".format(newFields))
