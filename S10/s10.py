import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)
inputFC = arcpy.GetParameterAsText(1)

# get spatial reference for the input feature class
inDescribe = arcpy.Describe(inputFC)
inspace = inDescribe.SpatialReference
inputSRName = inspace.Name

# create a list of FC
listFeaturC = arcpy.ListFeatureClasses()

for j in listFeaturC:
    featurecDescribe = arcpy.Describe(j)
    fcSR = featurecDescribe.SpatialReference
    fcSRName = fcSR.Name

    if fcSRName != inputSRName:
        print "Coordinate system has been changed to " + str(inputSRName)
        arcpy.AddMessage("Coordinate system has been changed to " + str(inputSRName))
    else:
        print "Coordinate system has not been changed to any system"
        arcpy.AddMessage("Coordinate system has not been changed to any system")

    if fcSRName == inputSRName:
        continue
    else:
        # create output feature class path and it's name
        outFS = j[:-4] + "_projected.shp"
        arcpy.Project_management(fc, outFS, inspace)
        print outFS
        arcpy.AddMessage(str(outFS))
